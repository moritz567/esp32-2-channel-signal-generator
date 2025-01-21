# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Hauptfenster.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QTextEdit, QToolButton, QWidget)

class Ui_Hauptfenster_QMW(object):
    def setupUi(self, Hauptfenster_QMW):
        if not Hauptfenster_QMW.objectName():
            Hauptfenster_QMW.setObjectName(u"Hauptfenster_QMW")
        Hauptfenster_QMW.resize(754, 739)
        self.centralwidget = QWidget(Hauptfenster_QMW)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 90))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(85, 0))
        font = QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 12, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(85, 0))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.VS_A1 = QSlider(self.frame)
        self.VS_A1.setObjectName(u"VS_A1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VS_A1.sizePolicy().hasHeightForWidth())
        self.VS_A1.setSizePolicy(sizePolicy)
        self.VS_A1.setMaximum(255)
        self.VS_A1.setOrientation(Qt.Vertical)
        self.VS_A1.setTickPosition(QSlider.TicksAbove)
        self.VS_A1.setTickInterval(5)

        self.gridLayout.addWidget(self.VS_A1, 2, 12, 1, 2)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.VS_A2 = QSlider(self.frame)
        self.VS_A2.setObjectName(u"VS_A2")
        sizePolicy.setHeightForWidth(self.VS_A2.sizePolicy().hasHeightForWidth())
        self.VS_A2.setSizePolicy(sizePolicy)
        self.VS_A2.setMinimumSize(QSize(0, 250))
        self.VS_A2.setMaximum(255)
        self.VS_A2.setOrientation(Qt.Vertical)
        self.VS_A2.setTickPosition(QSlider.TicksAbove)
        self.VS_A2.setTickInterval(5)

        self.gridLayout.addWidget(self.VS_A2, 2, 15, 1, 2)

        self.VS_F2 = QSlider(self.frame)
        self.VS_F2.setObjectName(u"VS_F2")
        sizePolicy.setHeightForWidth(self.VS_F2.sizePolicy().hasHeightForWidth())
        self.VS_F2.setSizePolicy(sizePolicy)
        self.VS_F2.setLayoutDirection(Qt.LeftToRight)
        self.VS_F2.setMaximum(300)
        self.VS_F2.setOrientation(Qt.Vertical)
        self.VS_F2.setTickPosition(QSlider.TicksAbove)
        self.VS_F2.setTickInterval(5)

        self.gridLayout.addWidget(self.VS_F2, 2, 4, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 14, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 1, 12, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(85, 0))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 8, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 6, 1, 1)

        self.VS_P = QSlider(self.frame)
        self.VS_P.setObjectName(u"VS_P")
        sizePolicy.setHeightForWidth(self.VS_P.sizePolicy().hasHeightForWidth())
        self.VS_P.setSizePolicy(sizePolicy)
        self.VS_P.setMaximum(360)
        self.VS_P.setPageStep(10)
        self.VS_P.setOrientation(Qt.Vertical)
        self.VS_P.setTickPosition(QSlider.TicksAbove)
        self.VS_P.setTickInterval(10)

        self.gridLayout.addWidget(self.VS_P, 2, 8, 1, 2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(85, 0))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 2)

        self.VS_F1 = QSlider(self.frame)
        self.VS_F1.setObjectName(u"VS_F1")
        sizePolicy.setHeightForWidth(self.VS_F1.sizePolicy().hasHeightForWidth())
        self.VS_F1.setSizePolicy(sizePolicy)
        self.VS_F1.setMinimumSize(QSize(50, 250))
        font1 = QFont()
        font1.setPointSize(9)
        self.VS_F1.setFont(font1)
        self.VS_F1.setMaximum(300)
        self.VS_F1.setSingleStep(1)
        self.VS_F1.setPageStep(25)
        self.VS_F1.setOrientation(Qt.Vertical)
        self.VS_F1.setInvertedAppearance(False)
        self.VS_F1.setTickPosition(QSlider.TicksAbove)
        self.VS_F1.setTickInterval(5)

        self.gridLayout.addWidget(self.VS_F1, 2, 0, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 11, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 1, 15, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 1, 8, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(85, 0))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 15, 1, 2)

        self.SB_val_F1 = QSpinBox(self.frame)
        self.SB_val_F1.setObjectName(u"SB_val_F1")
        self.SB_val_F1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_val_F1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.SB_val_F1.setMaximum(300)

        self.gridLayout.addWidget(self.SB_val_F1, 1, 1, 1, 1)

        self.SB_val_P = QSpinBox(self.frame)
        self.SB_val_P.setObjectName(u"SB_val_P")
        self.SB_val_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_val_P.setReadOnly(False)
        self.SB_val_P.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_val_P.setMaximum(360)

        self.gridLayout.addWidget(self.SB_val_P, 1, 9, 1, 1)

        self.SB_val_A1 = QSpinBox(self.frame)
        self.SB_val_A1.setObjectName(u"SB_val_A1")
        self.SB_val_A1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_val_A1.setReadOnly(False)
        self.SB_val_A1.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_val_A1.setMaximum(255)

        self.gridLayout.addWidget(self.SB_val_A1, 1, 13, 1, 1)

        self.SB_val_A2 = QSpinBox(self.frame)
        self.SB_val_A2.setObjectName(u"SB_val_A2")
        self.SB_val_A2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_val_A2.setReadOnly(False)
        self.SB_val_A2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_val_A2.setMaximum(255)

        self.gridLayout.addWidget(self.SB_val_A2, 1, 16, 1, 1)

        self.SB_val_F2 = QSpinBox(self.frame)
        self.SB_val_F2.setObjectName(u"SB_val_F2")
        self.SB_val_F2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_val_F2.setReadOnly(False)
        self.SB_val_F2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_val_F2.setMaximum(300)

        self.gridLayout.addWidget(self.SB_val_F2, 1, 4, 1, 2)


        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 2)

        self.B_update = QPushButton(self.centralwidget)
        self.B_update.setObjectName(u"B_update")

        self.gridLayout_2.addWidget(self.B_update, 3, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 3, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(385, 82))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.B_connect = QPushButton(self.groupBox)
        self.B_connect.setObjectName(u"B_connect")
        self.B_connect.setMinimumSize(QSize(80, 0))
        self.B_connect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.B_connect, 1, 4, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)

        self.LE_send = QLineEdit(self.groupBox)
        self.LE_send.setObjectName(u"LE_send")

        self.gridLayout_3.addWidget(self.LE_send, 1, 6, 1, 1)

        self.B_send = QPushButton(self.groupBox)
        self.B_send.setObjectName(u"B_send")
        self.B_send.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.B_send, 1, 7, 1, 1)

        self.TB_refresh_ports = QToolButton(self.groupBox)
        self.TB_refresh_ports.setObjectName(u"TB_refresh_ports")
        self.TB_refresh_ports.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.TB_refresh_ports, 1, 3, 1, 1)

        self.CB_Port = QComboBox(self.groupBox)
        self.CB_Port.setObjectName(u"CB_Port")
        self.CB_Port.setMinimumSize(QSize(80, 0))
        self.CB_Port.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CB_Port.setEditable(False)

        self.gridLayout_3.addWidget(self.CB_Port, 1, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 1, 1, 1)

        self.textEditSerial = QTextEdit(self.groupBox)
        self.textEditSerial.setObjectName(u"textEditSerial")

        self.gridLayout_3.addWidget(self.textEditSerial, 2, 6, 1, 1)

        self.L_Connection_Status = QLabel(self.groupBox)
        self.L_Connection_Status.setObjectName(u"L_Connection_Status")

        self.gridLayout_3.addWidget(self.L_Connection_Status, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 5, 1, 1)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.RB_manualupdate = QRadioButton(self.frame_2)
        self.RB_manualupdate.setObjectName(u"RB_manualupdate")
        self.RB_manualupdate.setChecked(True)

        self.gridLayout_4.addWidget(self.RB_manualupdate, 1, 0, 1, 1)

        self.RB_autoupdate = QRadioButton(self.frame_2)
        self.RB_autoupdate.setObjectName(u"RB_autoupdate")

        self.gridLayout_4.addWidget(self.RB_autoupdate, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 2, 1, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 2, 2)

        Hauptfenster_QMW.setCentralWidget(self.centralwidget)
        self.Main_Menu = QMenuBar(Hauptfenster_QMW)
        self.Main_Menu.setObjectName(u"Main_Menu")
        self.Main_Menu.setGeometry(QRect(0, 0, 754, 22))
        Hauptfenster_QMW.setMenuBar(self.Main_Menu)
        self.statusbar = QStatusBar(Hauptfenster_QMW)
        self.statusbar.setObjectName(u"statusbar")
        Hauptfenster_QMW.setStatusBar(self.statusbar)

        self.retranslateUi(Hauptfenster_QMW)

        QMetaObject.connectSlotsByName(Hauptfenster_QMW)
    # setupUi

    def retranslateUi(self, Hauptfenster_QMW):
        Hauptfenster_QMW.setWindowTitle(QCoreApplication.translate("Hauptfenster_QMW", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Amplitude 1", None))
        self.label.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Frequenz 1", None))
        self.label_9.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Wert:", None))
        self.label_11.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Wert:", None))
        self.label_2.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Phase", None))
        self.label_3.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Frequenz 2", None))
        self.label_12.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Wert:", None))
        self.label_10.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Wert:", None))
        self.label_7.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Amplitude 2", None))
        self.B_update.setText(QCoreApplication.translate("Hauptfenster_QMW", u"updaten", None))
        self.groupBox.setTitle(QCoreApplication.translate("Hauptfenster_QMW", u"Verbindung", None))
        self.B_connect.setText(QCoreApplication.translate("Hauptfenster_QMW", u"verbinden", None))
        self.label_5.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Status:", None))
        self.B_send.setText(QCoreApplication.translate("Hauptfenster_QMW", u"senden", None))
        self.TB_refresh_ports.setText(QCoreApplication.translate("Hauptfenster_QMW", u"...", None))
        self.label_4.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Port:", None))
        self.L_Connection_Status.setText(QCoreApplication.translate("Hauptfenster_QMW", u"unbekannt", None))
        self.RB_manualupdate.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Werte manuell updaten", None))
        self.RB_autoupdate.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Werte automatisch updaten", None))
    # retranslateUi

