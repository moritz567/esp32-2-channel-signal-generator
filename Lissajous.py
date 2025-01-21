import sys
import os
from os import path

import http.client, urllib

import locale

import colorama
from colorama import Fore

import json

from PySide6 import QtCore
from PySide6.QtGui import QAction, QIcon, QCursor, QPalette
from PySide6.QtCore import Qt, Signal, Slot, QSize, QTimer
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QWidget
)

from Hauptfenster_ui import Ui_Hauptfenster_QMW
from Temp_Stammdaten_ui import Ui_Temp_Stammdaten_Form

#basedir = path.dirname(__file__) #irgendwas mit Path hat sich geändert, jz abspath verwenden
bundle_dir = path.abspath(path.dirname(__file__))


ESP32_vendor_ID = 4292 #finds Silicon Labs CP210x USB to UART Bridge (USB connector of ESP32)
ESP32_product_ID = 60000

terminator_char = "\n"

colorama.init(autoreset=True)

print(Fore.YELLOW + "version: 1.0")

try:
    from ctypes import windll
    myappid = 'Musch.'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class Hauptfenster(QMainWindow, Ui_Hauptfenster_QMW):
    def __init__(self):
        super(Hauptfenster, self).__init__()
        self.setupUi(self)

        self.UI_Settings()




        self.Einstellungen_Menu = QMenu("Einstellungen")
        self.Main_Menu.addMenu(self.Einstellungen_Menu)
        self.Einstellungen_Menu.setEnabled(True)
        self.Einstellungen_Menu.setCursor(Qt.PointingHandCursor)


        self.Temperatur_Action = QAction("Temperaturen")
        self.Einstellungen_Menu.addAction(self.Temperatur_Action)
        self.Temperatur_Action.setEnabled(True)
        #self.Temperatur_Action.triggered.connect(self.Einstellungen_Temperatur_Fenster)
        

        self.B_send.clicked.connect(self.console_send)
        self.TB_refresh_ports.clicked.connect(self.Ports_abfragen)

        self.connect_B_Signal = self.B_connect.clicked.connect(self.Arduino_verbinden)


        self.TB_refresh_ports.setIcon(QIcon(path.join(bundle_dir, "icons", "icon_aktualisieren.png")))
        self.TB_refresh_ports.setAutoRaise(True)
 
        self.TB_refresh_ports.setIconSize(QSize(22, 22))

        self.RB_autoupdate.toggled.connect(self.update_auto_manual_send)


        self.arduino_port = QSerialPort()
        self.arduino_port.readyRead.connect(self.readSerial)
        self.arduino_port.errorOccurred.connect(self.Port_error)
        self.Ports_abfragen()
        #self.Arduino_verbinden()

        self.SB_val_F2.setPrefix("Wert: ")

        self.VS_F1.valueChanged.connect(self.refresh_SBF1_start_Timer)
        self.VS_F2.valueChanged.connect(self.refresh_SBF2_start_Timer)
        self.VS_P.valueChanged.connect(self.refresh_SBP_start_Timer)
        self.VS_A1.valueChanged.connect(self.refresh_SBA1_start_Timer)
        self.VS_A2.valueChanged.connect(self.refresh_SBA2_start_Timer)

        self.Timer_Interval = 1000
        self.F1_Timer = QTimer()
        self.F1_Timer.timeout.connect(self.send_all_val)
        self.F1_Timer.setInterval(self.Timer_Interval)
        self.F1_Timer.setSingleShot(True)

        self.F2_Timer = QTimer()
        self.F2_Timer.timeout.connect(self.send_all_val)
        self.F2_Timer.setInterval(self.Timer_Interval)
        self.F2_Timer.setSingleShot(True)

        self.P_Timer = QTimer()
        self.P_Timer.timeout.connect(self.send_all_val)
        self.P_Timer.setInterval(self.Timer_Interval)
        self.P_Timer.setSingleShot(True)

        self.A1_Timer = QTimer()
        self.A1_Timer.timeout.connect(self.send_all_val)
        self.A1_Timer.setInterval(self.Timer_Interval)
        self.A1_Timer.setSingleShot(True)

        self.A2_Timer = QTimer()
        self.A2_Timer.timeout.connect(self.send_all_val)
        self.A2_Timer.setInterval(self.Timer_Interval)
        self.A2_Timer.setSingleShot(True)

        self.SB_val_F1.editingFinished.connect(self.refresh_VSF1_from_SB)
        self.SB_val_F2.editingFinished.connect(self.refresh_VSF2_from_SB)
        self.SB_val_P.editingFinished.connect(self.refresh_VSP_from_SB)
        self.SB_val_A1.editingFinished.connect(self.refresh_VSA1_from_SB)
        self.SB_val_A2.editingFinished.connect(self.refresh_VSA2_from_SB)

        self.B_update.clicked.connect(self.send_all_val_from_Bupdate)

        self.SB_val_F1.setValue(self.VS_F1.value())
        self.SB_val_F2.setValue(self.VS_F2.value())
        self.SB_val_P.setValue(self.VS_P.value())
        self.SB_val_A1.setValue(self.VS_A1.value())
        self.SB_val_A2.setValue(self.VS_A2.value())

    def UI_Settings(self):
        self.setWindowTitle("Lissajousprojektor")
        self.setMinimumSize(550, 670)
        self.setGeometry(0, 0, 600, 670)

        # self.LE_send.setVisible(False)
        # self.B_send.setVisible(False)

        # self.textEditSerial.setReadOnly(True)

        self.B_update.setCursor(Qt.PointingHandCursor)

        self.need_check1 = False
        self.need_check2 = False

        self.warning1_send = False
        self.warning2_send = False

        self.arduino_is_available = False
        self.arduino_is_connected = False
        self.arduino_says_connected = False

        self.first_value_received = False

        #self.Temps_laden()
        self.Start_Temp_recieved = False
        self.connection_Info_send = False

        self.TextEdit_Text = ""

    def refresh_SBF1_start_Timer(self): 
        self.SB_val_F1.setValue(self.VS_F1.value())
        self.F1_Timer.start()
    
    def refresh_SBF2_start_Timer(self): 
        self.SB_val_F2.setValue(self.VS_F2.value())
        self.F2_Timer.start()

    def refresh_SBP_start_Timer(self): 
        self.SB_val_P.setValue(self.VS_P.value())
        self.P_Timer.start()

    def refresh_SBA1_start_Timer(self): 
        self.SB_val_A1.setValue(self.VS_A1.value())
        self.A1_Timer.start()

    def refresh_SBA2_start_Timer(self): 
        self.SB_val_A2.setValue(self.VS_A2.value())
        self.A2_Timer.start()


    def refresh_VSF1_from_SB(self): 
        self.VS_F1.setValue(self.SB_val_F1.value())
        self.F1_Timer.start()

    def refresh_VSF2_from_SB(self): 
        self.VS_F2.setValue(self.SB_val_F2.value())
        self.F2_Timer.start()

    def refresh_VSP_from_SB(self): 
        self.VS_P.setValue(self.SB_val_P.value())
        self.P_Timer.start()

    def refresh_VSA1_from_SB(self): 
        self.VS_A1.setValue(self.SB_val_A1.value())
        self.A1_Timer.start()

    def refresh_VSA2_from_SB(self): 
        self.VS_A2.setValue(self.SB_val_A2.value())
        self.A2_Timer.start()

            
    def send_all_val_from_Bupdate(self):
        self.send_all_val(B_send="Button")

    def send_all_val(self, B_send=None):
        if self.RB_autoupdate.isChecked() or B_send is not None:
            print(Fore.GREEN, "F1: " + str(self.VS_F1.value()))
            print(Fore.GREEN, "F2: " + str(self.VS_F2.value()))
            print(Fore.GREEN, "P: " + str(self.VS_P.value()))
            print(Fore.GREEN, "A1: " + str(self.VS_A1.value()))
            print(Fore.GREEN, "A2: " + str(self.VS_A2.value()))

            self.send_String = str(self.VS_F1.value()) +","+ str(self.VS_F2.value()) +","+ str(self.VS_P.value())+","+ str(self.VS_A1.value()) +","+ str(self.VS_A2.value())

            self.send_Serial(self.send_String, "")
        else:
            pass
            print("Autoupdate not activated")
    
    def update_auto_manual_send(self, checked) -> None:
        #enable/disable update button based on RadioButton State
        if checked:
            self.B_update.setEnabled(False)
        else:
            self.B_update.setEnabled(True)


    @Slot()
    def Temps_laden(self):
        #CB leeren
        return
        self.CB_Temp_Goal.clear()

        with open(path.join(bundle_dir, "settings.json"), "r", encoding='utf-8') as f:
            self.settings_data = json.load(f)
        f.close()

        self.Temps_List = self.settings_data["Temps"] #Json Dict mit Key "Temps" aufrufen -> Liste mit Temps
        
        for self.temp in self.Temps_List:
            self.CB_Temp_Goal.addItem(str(self.temp))

    def Einstellungen_Temperatur_Fenster(self):
        self.Temp_Fenster = Temp_Stammdaten_Fenster()
        # self.Temp_Fenster.Temps_gespeichert.connect(self.Temps_laden)
        
    def Ports_abfragen(self):
        if self.arduino_is_connected == False:
            #Combobox leeren
            self.item_count = self.CB_Port.count()
            for i in range(self.item_count):
                self.CB_Port.removeItem(i)

            for port in QSerialPortInfo.availablePorts():
                if port.hasVendorIdentifier() and port.hasProductIdentifier():
                    
                    # if port.vendorIdentifier() == arduino_nano_vendor_ID and port.productIdentifier() == arduino_nano_product_ID: #nur in CB aufnehmen wenn Arduino Nano ist
                    self.CB_Port.addItem((port.portName()))
                    #Ports print
                    # print("Port_name: ", port.portName())
                    # print("vendorIdentifier: ", port.vendorIdentifier())
                    # print("productIdentifier: ", port.productIdentifier())
                    # print("description: ", port.description())


                    
    def Arduino_verbinden(self):
        if self.CB_Port.count() == 0:
            return
        
        self.arduino_port_name = self.CB_Port.currentText()
        
        try:
            #Port Konfigurieren
            self.arduino_port.setPortName(self.arduino_port_name)
            self.arduino_port.setBaudRate(QSerialPort.Baud115200)
            self.arduino_port.setDataBits(QSerialPort.Data8)
            self.arduino_port.setParity(QSerialPort.NoParity)
            self.arduino_port.setStopBits(QSerialPort.OneStop)
            self.arduino_port.setFlowControl(QSerialPort.NoFlowControl)
            
            #Port Öffnen
            self.arduino_port.open(QSerialPort.ReadWrite)

            # print("port.isOpen:", self.arduino_port.isOpen()) #debug
            # print("port.openMode:", self.arduino_port.openMode()) #debug
            # print("port.error:", self.arduino_port.error()) #debug
            if self.arduino_port.isOpen():
                #print("verbunden") #debug
                self.arduino_is_connected = True
                self.L_Connection_Status.setText("verbunden")

                self.B_connect.disconnect(self.connect_B_Signal)
                self.B_connect.setText("trennen")
                self.CB_Port.setEnabled(False)
                self.TB_refresh_ports.setEnabled(False)
                self.connect_B_Signal = self.B_connect.clicked.connect(self.Arduino_trennen)

                self.arduino_port.clear(QSerialPort.Direction.AllDirections)
            else:
                self.arduino_verbindungs_Warnung = QMessageBox(QMessageBox.Warning, "Warnung", "Es konnte keine Verbindung hergestellt werden", QMessageBox.Ok)
                self.arduino_verbindungs_Warnung.setDefaultButton(QMessageBox.Ok)
                self.arduino_verbindungs_Warnung.exec()

        except:
            self.arduino_verbindungs_Warnung = QMessageBox(QMessageBox.Warning, "Warnung", "Es konnte keine Verbindung hergestellt werden", QMessageBox.Ok)
            self.arduino_verbindungs_Warnung.setDefaultButton(QMessageBox.Ok)
            self.arduino_verbindungs_Warnung.exec()

    def Arduino_trennen(self):
        self.arduino_port.close()
        self.arduino_is_connected = False
        self.arduino_says_connected = True

        self.first_value_received = False
        self.connection_Info_send = False

        self.Start_Temp_recieved = False
        

        self.B_connect.disconnect(self.connect_B_Signal)
        
        self.connect_B_Signal = self.B_connect.clicked.connect(self.Arduino_verbinden)

        #Gui
        self.L_Connection_Status.setText("getrennt")
        self.B_connect.setText("verbinden")
        self.CB_Port.setEnabled(True)
        self.TB_refresh_ports.setEnabled(True)

        # self.CB_Temp_Goal.setStyleSheet("QComboBox { color: black;}")

    def Port_error(self):
        #print("errrorr") #debug
        #print(self.arduino_port.error()) #debug
        try: #mit manchen Fehler funktioniert es nicht ..max recursion depth exceeded
            if self.arduino_port.error() != QSerialPort.NoError:
                self.Arduino_trennen()
        except:
            pass
    



    def readSerial(self):
     
        #Serial Buffer auslesen
        # while self.arduino_port.bytesAvailable() > 0:
        #     self.first_value_received = True

        #     try:
        #         self.Data = self.arduino_port.readLine()#return QBytearray
        #         self.pyData = self.Data.data().decode('ascii')
        #     except:
        #         continue

        #     self.pyData = self.pyData.strip('\r')
        #     self.pyData = self.pyData.strip('\n')

        #     #print(Fore.GREEN + "data", self.pyData) #debug
      
        #     self.arduino_operator = self.pyData[0]

        #     self.data_Text = self.pyData[1:]
        #     self.data_Text = self.data_Text.strip('\r')
        #     self.data_Text = self.data_Text.strip('\n')
            
            
        #     #Status Meldung Temperatur
        #     if self.arduino_operator == "T":
        #         self.Temp1 = float(self.data_Text)
        #         self.L_Temp_Current_1.setText(self.data_Text + " °C")
        #         self.need_check1 = True

        #     elif self.arduino_operator == "B":
        #         self.Temp2 = float(self.data_Text)
        #         self.L_Temp_Current_2.setText(self.data_Text + " °C")
        #         self.need_check2 = True

        #     if self.need_check1 == True and self.need_check2 == True:
                
        #         self.need_check1 = False
        #         self.need_check2 = False
        #         self.check_sensors()


        ###TEST###
        def read():
            while self.arduino_port.bytesAvailable() > 0:
                try:
                    self.Data = self.arduino_port.readLine()#return QBytearray
                    self.pyData = self.Data.data().decode('utf-8')
                except:
                    continue

                # self.pyData = self.pyData.strip('\r')
                # self.pyData = self.pyData.strip('\n')

                print(Fore.GREEN + "data", self.pyData) #debug
                self.TextEdit_Text += self.pyData

                self.textEditSerial.setText(self.TextEdit_Text)
                self.textEditSerial.verticalScrollBar().setValue(self.textEditSerial.verticalScrollBar().maximum())
                #40,40,0,255,255

        
        if self.arduino_port.bytesAvailable() > 0:
            self.first_value_received = True

            self.incoming_Serial_Timer = QTimer()
            self.incoming_Serial_Timer.timeout.connect(read)
            self.incoming_Serial_Timer.setInterval(300)
            self.incoming_Serial_Timer.setSingleShot(True)
            self.incoming_Serial_Timer.start()
        
            

    def send_pushover(self, sensor):
        self.pushover_title = "Sensor " + str(sensor) + " zu warm!"

        if sensor == 1:
            self.pushover_message = "Sensor " + str(sensor) + " ist zu warm! (" + self.L_Temp_Current_1.text()+ ")"
        elif sensor == 2:
            self.pushover_message = "Sensor " + str(sensor) + " ist zu warm! (" + self.L_Temp_Current_2.text()+ ")"
        

        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
        "token": "a87pj7ukd6eff5tqbn7c93g7uhhqmh",
        "user": "ukpgc86wuzvko9php4rw1nkreq2dir",
        "message": self.pushover_message,
        "title": self.pushover_title,
        "priority": "2",
        "retry": "100",
        "expire": "5"
        }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()

        print("warning_send")

    def console_send(self):
        self.send_Serial("", self.LE_send.text())


    def send_Serial(self, text, command):
        if self.arduino_port.isWritable():
            self.arduino_port.writeData(command + text + terminator_char, (len(text) + len(command)))
            print("Send: ", command + text, (len(text) + len(command))) #debug
            
        

    


class Temp_Stammdaten_Fenster(QWidget, Ui_Temp_Stammdaten_Form):
    Temps_gespeichert = Signal()
    def __init__(self, *args, obj=None, **kwargs):
        super(Temp_Stammdaten_Fenster, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Temperaturen festlegen")
        self.show()


        self.B_Plus.clicked.connect(self.Item_hinzufuegen)
        self.B_speichern.clicked.connect(self.Speichern)
        self.B_abbrechen.clicked.connect(self.Abbrechen)

        self.Temp_LW.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Temp_LW.customContextMenuRequested.connect(self.contextMenuEvent_Item)

        self.B_Plus.setIcon(QIcon(path.join(bundle_dir, "icons", "icon_plus.png")))
        self.B_Plus.setAutoRaise(True)
        self.B_Plus.setIconSize(QSize(40, 40))

        #Hintergrundfarbe weiß
        self.pal = QPalette()
        self.pal.setColor(QPalette.Window, Qt.white)
        self.Temp_LW.setAutoFillBackground(True)
        self.Temp_LW.setPalette(self.pal)

        self.Temp_LW.setSortingEnabled(True)

        self.loaddata()
        

    def loaddata(self):
        with open(path.join(bundle_dir, "settings.json"), "r", encoding='utf-8') as f:
            self.settings_data = json.load(f)

        f.close()

        self.Temps_List = self.settings_data["Temps"] #Json Dict mit Key "Temps" aufrufen -> Liste mit Temps
        #self.SP_Offset.setValue(int(self.Temp_Offset_str))

        print(self.settings_data)
        
        for self.temp in self.Temps_List:
            
            self.Item = QListWidgetItem(str(self.temp))
            self.Item.setFlags(self.Item.flags() | QtCore.Qt.ItemIsEditable)
            self.Temp_LW.addItem(self.Item)
        
    def contextMenuEvent_Item(self, event):
        self.evennnt = event
        self.menu = QMenu(self)

        self.selected_Item = self.Temp_LW.currentItem()

        self.entfernen_Action = QAction('entfernen', self)
        self.menu.addAction(self.entfernen_Action)
        self.entfernen_Action.triggered.connect(self.Item_Entfernen)
        
        self.menu.popup(QCursor.pos())
        

    def Item_Entfernen(self):
        self.Warndialog = QMessageBox(QMessageBox.Warning, "Warnung", "Soll die Temperatur wirklich entfernt werden?", QMessageBox.Cancel | QMessageBox.Ok)
        self.Warndialog.setDefaultButton(QMessageBox.Cancel)
        self.ret = self.Warndialog.exec()

        if self.ret == QMessageBox.Ok:
            
            self.selected_row = self.Temp_LW.row(self.selected_Item)
            self.Temp_LW.takeItem(self.selected_row)


    def Item_hinzufuegen(self):
        self.Item = QListWidgetItem(str(""))
        self.Item.setFlags(self.Item.flags() | QtCore.Qt.ItemIsEditable) #editable Flag zu bestehenden hinzufügen

        self.Temp_LW.addItem(self.Item)

        self.Temp_LW.setCurrentItem(self.Item)

    def Speichern(self):
        self.Temps_List = []
        self.item_count = self.Temp_LW.count()
        for self.index in range(self.item_count):
            
            try:
                self.current_temp = int(self.Temp_LW.item(self.index).text())
                if self.current_temp < 100 and self.current_temp >= 0:
                    self.Temps_List.append(int(self.current_temp))
            except:
                pass
            
        print(self.Temps_List)
        self.settings_data["Temps"] = self.Temps_List #settings_data Dict wurde aus JSON File geholt und
        #der Key "Temps" wird mit der neuen ausgelesenen Liste überschrieben
       
        with open(path.join(bundle_dir, "settings.json"), "w", encoding='utf-8') as f:
            json.dump(self.settings_data, f, ensure_ascii=False, indent=4)

        f.close()
        self.Temps_gespeichert.emit()

        self.close()

    def Abbrechen(self):
        self.close()


        


  


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

app = QApplication(sys.argv)
try:
    app.setWindowIcon(QIcon(path.join(bundle_dir, "icons", "icon_B.png")))
except:
    print(Fore.RED + "Window Icon not found")
Hauptfenster_Called = Hauptfenster()
Hauptfenster_Called.show()

#app.setStyle("Fusion")
app.exec()