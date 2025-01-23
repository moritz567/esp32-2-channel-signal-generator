import sys
import os, math
from os import path

import http.client, urllib

import colorama
from colorama import Fore

import json

from PySide6 import QtCore
from PySide6.QtGui import QAction, QIcon, QCursor, QPalette, QColor
from PySide6.QtCore import Qt, Signal, Slot, QSize, QTimer
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QPushButton,
    QAbstractItemView,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QWidget
)

from Hauptfenster_hor_ui import Ui_Hauptfenster_QMW
from Presets_ui import Ui_Presets_Form

# print("1: ", (2*1.7 + 5*3.5 + 7*2.1 + 7*3.4 + 4*2.1 + 4*1)/(2+5+7+7+4+4))
# print("2: ", (5*2.9 + 2*1.6 + 5*1.3 + 7*2.7)/(5+2+5+7))

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


        self.Presets_Action = QAction("Presets")
        self.Einstellungen_Menu.addAction(self.Presets_Action)
        self.Presets_Action.setEnabled(True)
        self.Presets_Action.triggered.connect(self.Einstellungen_Presets_Fenster)
        

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

        self.Timer_Interval = 1500
        self.timer_setup()
        
        self.setup_Slider_Signals()

        self.tabWidget.setCurrentIndex(1) #standart direkte Eingabe Tab
        self.Signal_B_update = self.B_update.clicked.connect(self.send_all_val_Schwingkreis_from_Bupdate)

        self.tabWidget.currentChanged.connect(self.update_tab_changed) #wenn Tab gewechselt wurde

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
        self.SB_F.setSuffix(" Hz")
        self.SB_U.setSuffix(" V")
        self.SB_C.setSuffix(" nF")
        self.SB_L.setSuffix(" mH")
        self.SB_R.setSuffix(" Ohm")

        self.textEditSerial.setReadOnly(True)

        self.TW_presets.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.TW_presets.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.TW_presets.setSelectionMode(QAbstractItemView.SingleSelection)

        self.B_update.setCursor(Qt.PointingHandCursor)
        self.VS_A1.setCursor(Qt.PointingHandCursor)

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

    def loaddata_Schwingkreis(self):
        print("Loading")
        with open(path.join(bundle_dir, "settings.json"), "r", encoding='utf-8') as f:
            self.settings_data = json.load(f)

        f.close()

        self.TW_presets.setRowCount(0)

        self.Preset_List = self.settings_data["Presets"] #Json Dict mit Key "Temps" aufrufen -> Liste mit Preset-dicts
        print("settings_data", self.settings_data)

        self.Index_List = "F", "U", "C", "L", "R"
        row = 0
        for self.preset in self.Preset_List:
            print(self.preset)

            self.TW_presets.insertRow(row)

            self.Cell_Item = QPushButton(self.preset["name"])
            self.Cell_Item.clicked.connect(self.update_values_from_TW)
            self.TW_presets.setCellWidget(row, 0, self.Cell_Item)

            col=1
            while col < self.TW_presets.columnCount():


                self.Item = QTableWidgetItem()
                self.Item.setText(str(self.preset[self.Index_List[col-1]]))
                self.Item.setTextAlignment(Qt.AlignCenter)
                self.Item.setFlags(self.Item.flags() ^ QtCore.Qt.ItemIsEditable)

                if (row % 2) == 0:
                    self.Item.setBackground(QColor("#f763ab"))

                else:
                    self.Item.setBackground(QColor("#88fa16"))

                self.TW_presets.setItem(row, col, self.Item)
                
                col += 1


            # self.Item = QTableWidgetItem()
            # self.Item.setText(str(self.preset["U"]))
            # self.Item.setTextAlignment(Qt.AlignCenter)
            # self.Item.setFlags(self.Item.flags() ^ QtCore.Qt.ItemIsEditable)
            # self.TW_presets.setItem(row, 2, self.Item)

            # self.Item = QTableWidgetItem()
            # self.Item.setText(str(self.preset["C"]))
            # self.Item.setTextAlignment(Qt.AlignCenter)
            # self.Item.setFlags(self.Item.flags() ^ QtCore.Qt.ItemIsEditable)
            # self.TW_presets.setItem(row, 3, self.Item)

            # self.Item = QTableWidgetItem()
            # self.Item.setText(str(self.preset["L"]))
            # self.Item.setTextAlignment(Qt.AlignCenter)
            # self.Item.setFlags(self.Item.flags() ^ QtCore.Qt.ItemIsEditable)
            # self.TW_presets.setItem(row, 4, self.Item)

            # self.Item = QTableWidgetItem()
            # self.Item.setText(str(self.preset["R"]))
            # self.Item.setTextAlignment(Qt.AlignCenter)
            # self.Item.setFlags(self.Item.flags() ^ QtCore.Qt.ItemIsEditable)
            # self.TW_presets.setItem(row, 5, self.Item)

            row+=1
            

    def update_values_from_TW(self): #update values on Sliders if preset is selected
        self.HS_F.setValue(int(self.TW_presets.item(self.TW_presets.currentRow(), 1).text()))
        self.HS_U.setValue(int(self.TW_presets.item(self.TW_presets.currentRow(), 2).text()))
        self.HS_C.setValue(int(self.TW_presets.item(self.TW_presets.currentRow(), 3).text()))
        self.HS_L.setValue(int(self.TW_presets.item(self.TW_presets.currentRow(), 4).text()))
        self.HS_R.setValue(int(self.TW_presets.item(self.TW_presets.currentRow(), 5).text()))

    def update_tab_changed(self):
        print("tab changed")
        if self.tabWidget.currentIndex() == 0: #direkt
            self.B_update.clicked.disconnect()
            self.B_update.clicked.connect(self.send_all_val_from_Bupdate)

        elif self.tabWidget.currentIndex() == 1: #Schwingkreis
            self.B_update.clicked.disconnect()
            self.B_update.clicked.connect(self.send_all_val_Schwingkreis_from_Bupdate)

            self.loaddata_Schwingkreis()



    ###direkte Eingabe###
    def refresh_SBF1_start_Timer(self): 
        self.SB_val_F1.setValue(self.VS_F1.value())
        self.direct_Timer.start()
    
    def refresh_SBF2_start_Timer(self): 
        self.SB_val_F2.setValue(self.VS_F2.value())
        self.direct_Timer.start()

    def refresh_SBP_start_Timer(self): 
        self.SB_val_P.setValue(self.VS_P.value())
        self.direct_Timer.start()

    def refresh_SBA1_start_Timer(self): 
        self.SB_val_A1.setValue(self.VS_A1.value())
        self.direct_Timer.start()

    def refresh_SBA2_start_Timer(self): 
        self.SB_val_A2.setValue(self.VS_A2.value())
        self.direct_Timer.start()


    def refresh_VSF1_from_SB(self): 
        self.VS_F1.setValue(self.SB_val_F1.value())

    def refresh_VSF2_from_SB(self): 
        self.VS_F2.setValue(self.SB_val_F2.value())

    def refresh_VSP_from_SB(self): 
        self.VS_P.setValue(self.SB_val_P.value())

    def refresh_VSA1_from_SB(self): 
        self.VS_A1.setValue(self.SB_val_A1.value())

    def refresh_VSA2_from_SB(self): 
        self.VS_A2.setValue(self.SB_val_A2.value())

    

    ###Schwingkreis###!!!
    def refresh_SBF(self): 
        self.SB_F.setValue(self.HS_F.value())
        self.Schwingkreis_Timer.start()
    
    def refresh_SBU(self): 
        self.SB_U.setValue(self.HS_U.value())
        self.Schwingkreis_Timer.start()

    def refresh_SBC(self): 
        self.SB_C.setValue(self.HS_C.value())
        self.Schwingkreis_Timer.start()

    def refresh_SBL(self): 
        self.SB_L.setValue(self.HS_L.value())
        self.Schwingkreis_Timer.start()

    def refresh_SBR(self): 
        self.SB_R.setValue(self.HS_R.value())
        self.Schwingkreis_Timer.start()



    def refresh_HSF_from_SB(self): 
        self.HS_F.setValue(self.SB_F.value())

    def refresh_HSU_from_SB(self): 
        self.HS_U.setValue(self.SB_U.value())

    def refresh_HSC_from_SB(self): 
        self.HS_C.setValue(self.SB_C.value())

    def refresh_HSL_from_SB(self): 
        self.HS_L.setValue(self.SB_L.value())

    def refresh_HSR_from_SB(self): 
        self.HS_R.setValue(self.SB_R.value())

    ###!!!###

    


    def send_all_val_from_Bupdate(self):
        self.send_all_val(B_send="Button")

    def send_all_val_Schwingkreis_from_Bupdate(self):
        self.send_all_val_Schwingkreis(B_send="Button")

    def send_all_val(self, B_send=None):
        if self.RB_autoupdate.isChecked() or B_send is not None:
            print(Fore.GREEN, "F1: " + str(self.VS_F1.value()))
            print(Fore.GREEN, "F2: " + str(self.VS_F2.value()))
            print(Fore.GREEN, "P: " + str(self.VS_P.value()))
            print(Fore.GREEN, "A1: " + str(self.VS_A1.value()))
            print(Fore.GREEN, "A2: " + str(self.VS_A2.value()))

            if self.CB_Laser.isChecked():
                Laser_status = 1
            else:
                Laser_status = 0

            self.send_String = str(self.VS_F1.value()) +","+ str(self.VS_F2.value()) +","+ str(self.VS_P.value())+","+ str(self.VS_A1.value()) +","+ str(self.VS_A2.value() +","+ Laser_status)

            self.send_Serial(self.send_String, "")
        else:
            pass
            print("Autoupdate not activated")

    def map_range(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    ###Senden Schwingkreis###
    def send_all_val_Schwingkreis(self, B_send=None):
        if self.RB_autoupdate.isChecked() or B_send is not None:
            self.F1 = self.HS_F.value()
            self.L = self.HS_L.value()/1000
            self.C = self.HS_C.value()/1000000000
            self.R = self.HS_R.value()
            self.U = self.HS_U.value()

            print(Fore.GREEN, "F1: " + str(self.F1))
            print(Fore.GREEN, "V: " + str(self.U))
            print(Fore.GREEN, "C: " + str(self.C))
            print(Fore.GREEN, "L: " + str(self.L))
            print(Fore.GREEN, "R: " + str(self.R))

            phase_raw = math.atan(((2*math.pi*self.F1*self.L) - (1/(2*math.pi*self.F1*self.C))) / self.R)
            phase = (180/math.pi) * math.atan(((2*math.pi*self.F1*self.L) - (1/(2*math.pi*self.F1*self.C))) / self.R)
            # phase = (180/math.pi) * math.atan(((100) - (100)) / self.R)

            print(Fore.RED, "Phase_rad: " + str(phase_raw))
            print(Fore.RED, "Phase: " + str(phase))


            Strom = self.U*1000 / math.sqrt(self.R**2 + (((2*math.pi*self.F1*self.L) - (1/(2*math.pi*self.F1*self.C)))**2)) #mA
            print(Fore.RED, "Strom: " + str(Strom))

            #Strom_mapped = self.map_range(Strom, 0, 1000, 0, 256)
            #print(Fore.RED, "Strom mapped: " + str(Strom))
            ###!!!
        
            if self.CB_Laser.isChecked():
                Laser_status = 1
            else:
                Laser_status = 0
            
            #map Strom 0-256

            self.L_out_I.setText(str(round(Strom, 2)))
            self.L_out_P.setText(str(round(phase, 2)))

            self.send_String = str(self.F1) +","+ str(self.F1) +","+ str(phase)+","+ str(self.U) +","+ str(Strom) +","+ str(Laser_status)

            # self.send_Serial(self.send_String, "")
        else:
            pass
            print("Autoupdate not activated")
    
    def update_auto_manual_send(self, checked) -> None:
        #enable/disable update button based on RadioButton State
        if checked:
            self.B_update.setEnabled(False)
        else:
            self.B_update.setEnabled(True)

    def timer_setup(self):
        #direct values
        self.direct_Timer = QTimer()
        self.direct_Timer.timeout.connect(self.send_all_val)
        self.direct_Timer.setInterval(self.Timer_Interval)
        self.direct_Timer.setSingleShot(True)

        ###Schwingkreis###
        self.Schwingkreis_Timer = QTimer()
        self.Schwingkreis_Timer.timeout.connect(self.send_all_val_Schwingkreis)
        self.Schwingkreis_Timer.setInterval(self.Timer_Interval)
        self.Schwingkreis_Timer.setSingleShot(True)

    def setup_Slider_Signals(self):
        #direct Values
        self.VS_F1.valueChanged.connect(self.refresh_SBF1_start_Timer)
        self.VS_F2.valueChanged.connect(self.refresh_SBF2_start_Timer)
        self.VS_P.valueChanged.connect(self.refresh_SBP_start_Timer)
        self.VS_A1.valueChanged.connect(self.refresh_SBA1_start_Timer)
        self.VS_A2.valueChanged.connect(self.refresh_SBA2_start_Timer)

        self.SB_val_F1.valueChanged.connect(self.refresh_VSF1_from_SB)
        self.SB_val_F2.valueChanged.connect(self.refresh_VSF2_from_SB)
        self.SB_val_P.valueChanged.connect(self.refresh_VSP_from_SB)
        self.SB_val_A1.valueChanged.connect(self.refresh_VSA1_from_SB)
        self.SB_val_A2.valueChanged.connect(self.refresh_VSA2_from_SB)

        #Schwingkreis Tab
        self.HS_F.valueChanged.connect(self.refresh_SBF)
        self.HS_U.valueChanged.connect(self.refresh_SBU)
        self.HS_C.valueChanged.connect(self.refresh_SBC)
        self.HS_L.valueChanged.connect(self.refresh_SBL)
        self.HS_R.valueChanged.connect(self.refresh_SBR)

        self.SB_F.valueChanged.connect(self.refresh_HSF_from_SB)
        self.SB_U.valueChanged.connect(self.refresh_HSU_from_SB)
        self.SB_C.valueChanged.connect(self.refresh_HSC_from_SB)
        self.SB_L.valueChanged.connect(self.refresh_HSL_from_SB)
        self.SB_R.valueChanged.connect(self.refresh_HSR_from_SB)
        
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

    def Einstellungen_Presets_Fenster(self):
        self.Temp_Fenster = Presets_Fenster()
        # self.Temp_Fenster.Presets_gespeichert.connect(self.Temps_laden)

                    
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
            
        

    


class Presets_Fenster(QWidget, Ui_Presets_Form):
    Presets_gespeichert = Signal()
    def __init__(self, *args, obj=None, **kwargs):
        super(Presets_Fenster, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Presets festlegen")
        self.show()


        self.B_Plus.clicked.connect(self.Item_hinzufuegen)
        self.B_speichern.clicked.connect(self.Speichern)
        self.B_abbrechen.clicked.connect(self.Abbrechen)

        self.TW_Presets.setContextMenuPolicy(Qt.CustomContextMenu)
        self.TW_Presets.customContextMenuRequested.connect(self.contextMenuEvent_Item)

        self.B_Plus.setIcon(QIcon(path.join(bundle_dir, "icons", "icon_plus.png")))
        self.B_Plus.setAutoRaise(True)
        self.B_Plus.setIconSize(QSize(40, 40))

        #Hintergrundfarbe weiß
        self.pal = QPalette()
        self.pal.setColor(QPalette.Window, Qt.white)
        self.TW_Presets.setAutoFillBackground(True)
        self.TW_Presets.setPalette(self.pal)

        self.TW_Presets.setSortingEnabled(True)

        self.loaddata()
        

    def loaddata(self):
        with open(path.join(bundle_dir, "settings.json"), "r", encoding='utf-8') as f:
            self.settings_data = json.load(f)

        f.close()

        self.TW_Presets.setRowCount(0)

        self.Preset_List = self.settings_data["Presets"] #Json Dict mit Key "Temps" aufrufen -> Liste mit Preset-dicts
        # print(self.settings_data)
        row = 0
        for self.preset in self.Preset_List:
            print(self.preset)

            self.TW_Presets.insertRow(row)

            self.Item = QTableWidgetItem()
            self.Item.setText(self.preset["name"])
            self.Item.setFlags(self.Item.flags() | QtCore.Qt.ItemIsEditable)
            self.TW_Presets.setItem(row, 0, self.Item)

            self.Item = QTableWidgetItem()
            self.Item.setText(str(self.preset["F"]))
            self.Item.setFlags(self.Item.flags() | QtCore.Qt.ItemIsEditable)
            self.TW_Presets.setItem(row, 1, self.Item)

            self.Item = QTableWidgetItem()
            self.Item.setText(str(self.preset["U"]))
            self.Item.setFlags(self.Item.flags() | QtCore.Qt.ItemIsEditable)
            self.TW_Presets.setItem(row, 2, self.Item)

            self.Item = QTableWidgetItem()
            self.Item.setText(str(self.preset["C"]))
            self.Item.setFlags(self.Item.flags() | QtCore.Qt.ItemIsEditable)
            self.TW_Presets.setItem(row, 3, self.Item)

            self.Item = QTableWidgetItem()
            self.Item.setText(str(self.preset["L"]))
            self.Item.setFlags(self.Item.flags() | QtCore.Qt.ItemIsEditable)
            self.TW_Presets.setItem(row, 4, self.Item)

            self.Item = QTableWidgetItem()
            self.Item.setText(str(self.preset["R"]))
            self.Item.setFlags(self.Item.flags() | QtCore.Qt.ItemIsEditable)
            self.TW_Presets.setItem(row, 5, self.Item)

            row+=1
            
            
        
    def contextMenuEvent_Item(self, event):
        self.evennnt = event
        self.menu = QMenu(self)

        self.selected_Item = self.TW_Presets.currentItem()

        self.entfernen_Action = QAction('entfernen', self)
        self.menu.addAction(self.entfernen_Action)
        self.entfernen_Action.triggered.connect(self.Item_Entfernen)
        
        self.menu.popup(QCursor.pos())
        

    def Item_Entfernen(self):
        self.Warndialog = QMessageBox(QMessageBox.Warning, "Warnung", "Soll das Preset wirklich entfernt werden?", QMessageBox.Cancel | QMessageBox.Ok)
        self.Warndialog.setDefaultButton(QMessageBox.Cancel)
        self.ret = self.Warndialog.exec()

        if self.ret == QMessageBox.Ok:
            self.TW_Presets.removeRow(self.TW_Presets.currentRow())


    def Item_hinzufuegen(self):
        self.rowcount = self.TW_Presets.rowCount()
        self.TW_Presets.insertRow(self.TW_Presets.rowCount()) #row unten einfügen


        for col in range(self.TW_Presets.columnCount()):
            self.Item = QTableWidgetItem()
            self.Item.setFlags(self.Item.flags() | QtCore.Qt.ItemIsEditable) #editable Flag zu bestehenden hinzufügen
            self.Item.setText("")
            self.TW_Presets.setItem(self.TW_Presets.rowCount(), col, self.Item)

        self.TW_Presets.selectRow(self.TW_Presets.rowCount())

    def Speichern(self):
        self.Presets_List = []

        

        for self.row in range(self.TW_Presets.rowCount()):
            self.preset_dict = {"name": "test", "F": 0, "U": 0, "C": 0, "L": 0, "R": 0}
            
            try:

                self.preset_dict["name"] = self.TW_Presets.item(self.row, 0).text()
                self.preset_dict["F"] = int(self.TW_Presets.item(self.row, 1).text())
                self.preset_dict["U"] = int(self.TW_Presets.item(self.row, 2).text())
                self.preset_dict["C"] = int(self.TW_Presets.item(self.row, 3).text())
                self.preset_dict["L"] = int(self.TW_Presets.item(self.row, 4).text())
                self.preset_dict["R"] = int(self.TW_Presets.item(self.row, 5).text())

            except Exception as e:
                print(e)

            self.Presets_List.append(self.preset_dict)
            
        print("Presets_List: ", self.Presets_List)

        self.settings_data["Presets"] = self.Presets_List #settings_data Dict wurde aus JSON File geholt und
        #der Key "Presets" wird mit der neuen ausgelesenen Liste überschrieben
       
        with open(path.join(bundle_dir, "settings.json"), "w", encoding='utf-8') as f:
            json.dump(self.settings_data, f, ensure_ascii=False, indent=4)

        f.close()
        #self.Presets_gespeichert.emit()

        self.close()

    def Abbrechen(self):
        self.close()


        


  


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

app = QApplication(sys.argv)
try:
    app.setWindowIcon(QIcon(path.join(bundle_dir, "icons", "icon_L.png")))
except:
    print(Fore.RED + "Window Icon not found")
Hauptfenster_Called = Hauptfenster()
Hauptfenster_Called.show()

#app.setStyle("Fusion")
app.exec()