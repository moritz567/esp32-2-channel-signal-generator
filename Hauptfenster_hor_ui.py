# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Hauptfenster_hor.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolButton,
    QWidget)

class Ui_Hauptfenster_QMW(object):
    def setupUi(self, Hauptfenster_QMW):
        if not Hauptfenster_QMW.objectName():
            Hauptfenster_QMW.setObjectName(u"Hauptfenster_QMW")
        Hauptfenster_QMW.resize(1015, 824)
        self.centralwidget = QWidget(Hauptfenster_QMW)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.B_update = QPushButton(self.centralwidget)
        self.B_update.setObjectName(u"B_update")

        self.gridLayout_2.addWidget(self.B_update, 3, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 3, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 40))
        self.tab_direct = QWidget()
        self.tab_direct.setObjectName(u"tab_direct")
        self.gridLayout = QGridLayout(self.tab_direct)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.tab_direct)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(85, 0))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_3 = QLabel(self.tab_direct)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(85, 0))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label_2 = QLabel(self.tab_direct)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(85, 0))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 5, 1, 2)

        self.label_6 = QLabel(self.tab_direct)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(85, 0))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 8, 1, 2)

        self.label_7 = QLabel(self.tab_direct)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(85, 0))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 11, 1, 2)

        self.label_9 = QLabel(self.tab_direct)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.SB_val_F1 = QSpinBox(self.tab_direct)
        self.SB_val_F1.setObjectName(u"SB_val_F1")
        self.SB_val_F1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_val_F1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.SB_val_F1.setMaximum(300)

        self.gridLayout.addWidget(self.SB_val_F1, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.SB_val_F2 = QSpinBox(self.tab_direct)
        self.SB_val_F2.setObjectName(u"SB_val_F2")
        self.SB_val_F2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_val_F2.setReadOnly(False)
        self.SB_val_F2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_val_F2.setMaximum(300)

        self.gridLayout.addWidget(self.SB_val_F2, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.label_10 = QLabel(self.tab_direct)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 1, 5, 1, 1)

        self.SB_val_P = QSpinBox(self.tab_direct)
        self.SB_val_P.setObjectName(u"SB_val_P")
        self.SB_val_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_val_P.setReadOnly(False)
        self.SB_val_P.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_val_P.setMaximum(360)

        self.gridLayout.addWidget(self.SB_val_P, 1, 6, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 7, 1, 1)

        self.label_11 = QLabel(self.tab_direct)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 1, 8, 1, 1)

        self.SB_val_A1 = QSpinBox(self.tab_direct)
        self.SB_val_A1.setObjectName(u"SB_val_A1")
        self.SB_val_A1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_val_A1.setReadOnly(False)
        self.SB_val_A1.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_val_A1.setMaximum(255)

        self.gridLayout.addWidget(self.SB_val_A1, 1, 9, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 10, 1, 1)

        self.label_12 = QLabel(self.tab_direct)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 1, 11, 1, 1)

        self.SB_val_A2 = QSpinBox(self.tab_direct)
        self.SB_val_A2.setObjectName(u"SB_val_A2")
        self.SB_val_A2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_val_A2.setReadOnly(False)
        self.SB_val_A2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_val_A2.setMaximum(255)

        self.gridLayout.addWidget(self.SB_val_A2, 1, 12, 1, 1)

        self.VS_F1 = QSlider(self.tab_direct)
        self.VS_F1.setObjectName(u"VS_F1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.VS_F1.sizePolicy().hasHeightForWidth())
        self.VS_F1.setSizePolicy(sizePolicy1)
        self.VS_F1.setMinimumSize(QSize(0, 250))
        font1 = QFont()
        font1.setPointSize(9)
        self.VS_F1.setFont(font1)
        self.VS_F1.setMaximum(300)
        self.VS_F1.setSingleStep(1)
        self.VS_F1.setPageStep(10)
        self.VS_F1.setOrientation(Qt.Vertical)
        self.VS_F1.setInvertedAppearance(False)
        self.VS_F1.setTickPosition(QSlider.TicksAbove)
        self.VS_F1.setTickInterval(5)

        self.gridLayout.addWidget(self.VS_F1, 2, 0, 1, 2)

        self.VS_F2 = QSlider(self.tab_direct)
        self.VS_F2.setObjectName(u"VS_F2")
        sizePolicy1.setHeightForWidth(self.VS_F2.sizePolicy().hasHeightForWidth())
        self.VS_F2.setSizePolicy(sizePolicy1)
        self.VS_F2.setMinimumSize(QSize(0, 250))
        self.VS_F2.setLayoutDirection(Qt.LeftToRight)
        self.VS_F2.setMaximum(300)
        self.VS_F2.setOrientation(Qt.Vertical)
        self.VS_F2.setTickPosition(QSlider.TicksAbove)
        self.VS_F2.setTickInterval(5)

        self.gridLayout.addWidget(self.VS_F2, 2, 3, 1, 1)

        self.VS_P = QSlider(self.tab_direct)
        self.VS_P.setObjectName(u"VS_P")
        sizePolicy1.setHeightForWidth(self.VS_P.sizePolicy().hasHeightForWidth())
        self.VS_P.setSizePolicy(sizePolicy1)
        self.VS_P.setMinimumSize(QSize(0, 250))
        self.VS_P.setMaximum(360)
        self.VS_P.setPageStep(10)
        self.VS_P.setOrientation(Qt.Vertical)
        self.VS_P.setTickPosition(QSlider.TicksAbove)
        self.VS_P.setTickInterval(10)

        self.gridLayout.addWidget(self.VS_P, 2, 5, 1, 2)

        self.VS_A1 = QSlider(self.tab_direct)
        self.VS_A1.setObjectName(u"VS_A1")
        sizePolicy1.setHeightForWidth(self.VS_A1.sizePolicy().hasHeightForWidth())
        self.VS_A1.setSizePolicy(sizePolicy1)
        self.VS_A1.setMinimumSize(QSize(0, 250))
        self.VS_A1.setMaximum(255)
        self.VS_A1.setOrientation(Qt.Vertical)
        self.VS_A1.setTickPosition(QSlider.TicksAbove)
        self.VS_A1.setTickInterval(5)

        self.gridLayout.addWidget(self.VS_A1, 2, 8, 1, 2)

        self.VS_A2 = QSlider(self.tab_direct)
        self.VS_A2.setObjectName(u"VS_A2")
        sizePolicy1.setHeightForWidth(self.VS_A2.sizePolicy().hasHeightForWidth())
        self.VS_A2.setSizePolicy(sizePolicy1)
        self.VS_A2.setMinimumSize(QSize(0, 250))
        self.VS_A2.setMaximum(255)
        self.VS_A2.setOrientation(Qt.Vertical)
        self.VS_A2.setTickPosition(QSlider.TicksAbove)
        self.VS_A2.setTickInterval(5)

        self.gridLayout.addWidget(self.VS_A2, 2, 11, 1, 2)

        self.tabWidget.addTab(self.tab_direct, "")
        self.tab_Schwingkreis = QWidget()
        self.tab_Schwingkreis.setObjectName(u"tab_Schwingkreis")
        self.gridLayout_5 = QGridLayout(self.tab_Schwingkreis)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_19 = QLabel(self.tab_Schwingkreis)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(85, 35))
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_19, 5, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 8, 0, 1, 1)

        self.SB_R = QSpinBox(self.tab_Schwingkreis)
        self.SB_R.setObjectName(u"SB_R")
        self.SB_R.setMinimumSize(QSize(0, 26))
        self.SB_R.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_R.setReadOnly(False)
        self.SB_R.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_R.setMinimum(1)
        self.SB_R.setMaximum(600)

        self.gridLayout_5.addWidget(self.SB_R, 5, 1, 1, 1)

        self.label_20 = QLabel(self.tab_Schwingkreis)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(85, 35))
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_20, 2, 0, 1, 1)

        self.TW_presets = QTableWidget(self.tab_Schwingkreis)
        if (self.TW_presets.columnCount() < 6):
            self.TW_presets.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.TW_presets.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TW_presets.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TW_presets.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TW_presets.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TW_presets.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TW_presets.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.TW_presets.rowCount() < 1):
            self.TW_presets.setRowCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TW_presets.setVerticalHeaderItem(0, __qtablewidgetitem6)
        self.TW_presets.setObjectName(u"TW_presets")

        self.gridLayout_5.addWidget(self.TW_presets, 0, 0, 1, 3)

        self.SB_U = QSpinBox(self.tab_Schwingkreis)
        self.SB_U.setObjectName(u"SB_U")
        self.SB_U.setMinimumSize(QSize(0, 26))
        self.SB_U.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_U.setReadOnly(False)
        self.SB_U.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_U.setMaximum(255)

        self.gridLayout_5.addWidget(self.SB_U, 2, 1, 1, 1)

        self.label_17 = QLabel(self.tab_Schwingkreis)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(85, 35))
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_17, 1, 0, 1, 1)

        self.HS_C = QSlider(self.tab_Schwingkreis)
        self.HS_C.setObjectName(u"HS_C")
        self.HS_C.setMaximum(200)
        self.HS_C.setOrientation(Qt.Horizontal)
        self.HS_C.setInvertedAppearance(False)
        self.HS_C.setInvertedControls(True)

        self.gridLayout_5.addWidget(self.HS_C, 3, 2, 1, 1)

        self.SB_F = QSpinBox(self.tab_Schwingkreis)
        self.SB_F.setObjectName(u"SB_F")
        self.SB_F.setMinimumSize(QSize(0, 26))
        font2 = QFont()
        font2.setPointSize(10)
        self.SB_F.setFont(font2)
        self.SB_F.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_F.setReadOnly(False)
        self.SB_F.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_F.setMaximum(1000)

        self.gridLayout_5.addWidget(self.SB_F, 1, 1, 1, 1)

        self.label_14 = QLabel(self.tab_Schwingkreis)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_14, 7, 0, 1, 1)

        self.SB_C = QSpinBox(self.tab_Schwingkreis)
        self.SB_C.setObjectName(u"SB_C")
        self.SB_C.setMinimumSize(QSize(0, 26))
        self.SB_C.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_C.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.SB_C.setMaximum(300)

        self.gridLayout_5.addWidget(self.SB_C, 3, 1, 1, 1)

        self.label_16 = QLabel(self.tab_Schwingkreis)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(85, 35))
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_16, 4, 0, 1, 1)

        self.label_13 = QLabel(self.tab_Schwingkreis)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_13, 6, 0, 1, 1)

        self.HS_L = QSlider(self.tab_Schwingkreis)
        self.HS_L.setObjectName(u"HS_L")
        self.HS_L.setMaximum(200)
        self.HS_L.setOrientation(Qt.Horizontal)
        self.HS_L.setInvertedAppearance(False)
        self.HS_L.setInvertedControls(True)

        self.gridLayout_5.addWidget(self.HS_L, 4, 2, 1, 1)

        self.label_8 = QLabel(self.tab_Schwingkreis)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(85, 35))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_8, 3, 0, 1, 1)

        self.SB_L = QSpinBox(self.tab_Schwingkreis)
        self.SB_L.setObjectName(u"SB_L")
        self.SB_L.setMinimumSize(QSize(0, 26))
        self.SB_L.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.SB_L.setReadOnly(False)
        self.SB_L.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SB_L.setMaximum(300)

        self.gridLayout_5.addWidget(self.SB_L, 4, 1, 1, 1)

        self.HS_R = QSlider(self.tab_Schwingkreis)
        self.HS_R.setObjectName(u"HS_R")
        self.HS_R.setMinimum(1)
        self.HS_R.setMaximum(600)
        self.HS_R.setOrientation(Qt.Horizontal)
        self.HS_R.setInvertedAppearance(False)
        self.HS_R.setInvertedControls(True)

        self.gridLayout_5.addWidget(self.HS_R, 5, 2, 1, 1)

        self.HS_U = QSlider(self.tab_Schwingkreis)
        self.HS_U.setObjectName(u"HS_U")
        self.HS_U.setMaximum(265)
        self.HS_U.setOrientation(Qt.Horizontal)
        self.HS_U.setInvertedAppearance(False)
        self.HS_U.setInvertedControls(True)

        self.gridLayout_5.addWidget(self.HS_U, 2, 2, 1, 1)

        self.HS_F = QSlider(self.tab_Schwingkreis)
        self.HS_F.setObjectName(u"HS_F")
        self.HS_F.setMaximum(1000)
        self.HS_F.setOrientation(Qt.Horizontal)
        self.HS_F.setInvertedAppearance(False)
        self.HS_F.setInvertedControls(True)

        self.gridLayout_5.addWidget(self.HS_F, 1, 2, 1, 1)

        self.L_out_I = QLabel(self.tab_Schwingkreis)
        self.L_out_I.setObjectName(u"L_out_I")
        self.L_out_I.setFont(font)
        self.L_out_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.L_out_I, 6, 1, 1, 1)

        self.L_out_P = QLabel(self.tab_Schwingkreis)
        self.L_out_P.setObjectName(u"L_out_P")
        self.L_out_P.setFont(font)
        self.L_out_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.L_out_P, 7, 1, 1, 1)

        self.tabWidget.addTab(self.tab_Schwingkreis, "")

        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(385, 130))
        self.groupBox.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.B_connect = QPushButton(self.groupBox)
        self.B_connect.setObjectName(u"B_connect")
        self.B_connect.setMinimumSize(QSize(80, 0))
        self.B_connect.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.B_connect, 1, 4, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)

        self.LE_send = QLineEdit(self.groupBox)
        self.LE_send.setObjectName(u"LE_send")

        self.gridLayout_3.addWidget(self.LE_send, 1, 6, 1, 1)

        self.B_send = QPushButton(self.groupBox)
        self.B_send.setObjectName(u"B_send")
        self.B_send.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.B_send, 1, 7, 1, 1)

        self.TB_refresh_ports = QToolButton(self.groupBox)
        self.TB_refresh_ports.setObjectName(u"TB_refresh_ports")
        self.TB_refresh_ports.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.TB_refresh_ports, 1, 3, 1, 1)

        self.CB_Port = QComboBox(self.groupBox)
        self.CB_Port.setObjectName(u"CB_Port")
        self.CB_Port.setMinimumSize(QSize(80, 0))
        self.CB_Port.setCursor(QCursor(Qt.PointingHandCursor))
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 5, 1, 1)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 85))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.RB_autoupdate = QRadioButton(self.frame_2)
        self.RB_autoupdate.setObjectName(u"RB_autoupdate")

        self.gridLayout_4.addWidget(self.RB_autoupdate, 2, 0, 1, 1)

        self.RB_manualupdate = QRadioButton(self.frame_2)
        self.RB_manualupdate.setObjectName(u"RB_manualupdate")
        self.RB_manualupdate.setChecked(True)

        self.gridLayout_4.addWidget(self.RB_manualupdate, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.CB_Laser = QCheckBox(self.frame_2)
        self.CB_Laser.setObjectName(u"CB_Laser")

        self.gridLayout_4.addWidget(self.CB_Laser, 4, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 2, 1, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)

        Hauptfenster_QMW.setCentralWidget(self.centralwidget)
        self.Main_Menu = QMenuBar(Hauptfenster_QMW)
        self.Main_Menu.setObjectName(u"Main_Menu")
        self.Main_Menu.setGeometry(QRect(0, 0, 1015, 22))
        Hauptfenster_QMW.setMenuBar(self.Main_Menu)
        self.statusbar = QStatusBar(Hauptfenster_QMW)
        self.statusbar.setObjectName(u"statusbar")
        Hauptfenster_QMW.setStatusBar(self.statusbar)

        self.retranslateUi(Hauptfenster_QMW)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Hauptfenster_QMW)
    # setupUi

    def retranslateUi(self, Hauptfenster_QMW):
        Hauptfenster_QMW.setWindowTitle(QCoreApplication.translate("Hauptfenster_QMW", u"MainWindow", None))
        self.B_update.setText(QCoreApplication.translate("Hauptfenster_QMW", u"updaten", None))
        self.label.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Frequenz 1", None))
        self.label_3.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Frequenz 2", None))
        self.label_2.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Phase", None))
        self.label_6.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Amplitude 1", None))
        self.label_7.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Amplitude 2", None))
        self.label_9.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Wert:", None))
        self.label_10.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Wert:", None))
        self.label_11.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Wert:", None))
        self.label_12.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Wert:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_direct), QCoreApplication.translate("Hauptfenster_QMW", u"Werte direkt", None))
        self.label_19.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Widerstand", None))
        self.label_20.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Spannung", None))
        ___qtablewidgetitem = self.TW_presets.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Name", None));
        ___qtablewidgetitem1 = self.TW_presets.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Frequenz", None));
        ___qtablewidgetitem2 = self.TW_presets.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Spannung", None));
        ___qtablewidgetitem3 = self.TW_presets.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Kapazit\u00e4t", None));
        ___qtablewidgetitem4 = self.TW_presets.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Induktivit\u00e4t", None));
        ___qtablewidgetitem5 = self.TW_presets.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Widerstand", None));
        self.label_17.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Frequenz 1", None))
        self.label_14.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Phase", None))
        self.label_16.setText(QCoreApplication.translate("Hauptfenster_QMW", u"induktivit\u00e4t", None))
        self.label_13.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Strom", None))
        self.label_8.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Kapazit\u00e4t", None))
        self.L_out_I.setText(QCoreApplication.translate("Hauptfenster_QMW", u"0", None))
        self.L_out_P.setText(QCoreApplication.translate("Hauptfenster_QMW", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Schwingkreis), QCoreApplication.translate("Hauptfenster_QMW", u"Schwingkreis", None))
        self.groupBox.setTitle(QCoreApplication.translate("Hauptfenster_QMW", u"Verbindung", None))
        self.B_connect.setText(QCoreApplication.translate("Hauptfenster_QMW", u"verbinden", None))
        self.label_5.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Status:", None))
        self.B_send.setText(QCoreApplication.translate("Hauptfenster_QMW", u"senden", None))
        self.TB_refresh_ports.setText(QCoreApplication.translate("Hauptfenster_QMW", u"...", None))
        self.label_4.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Port:", None))
        self.textEditSerial.setHtml(QCoreApplication.translate("Hauptfenster_QMW", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4<br />4<br />4<br />4<br />$</p></body></html>", None))
        self.L_Connection_Status.setText(QCoreApplication.translate("Hauptfenster_QMW", u"unbekannt", None))
        self.RB_autoupdate.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Werte automatisch updaten", None))
        self.RB_manualupdate.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Werte manuell updaten", None))
        self.CB_Laser.setText(QCoreApplication.translate("Hauptfenster_QMW", u"Laser an", None))
    # retranslateUi

