# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Temp_Stammdaten.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QWidget)

class Ui_Temp_Stammdaten_Form(object):
    def setupUi(self, Temp_Stammdaten_Form):
        if not Temp_Stammdaten_Form.objectName():
            Temp_Stammdaten_Form.setObjectName(u"Temp_Stammdaten_Form")
        Temp_Stammdaten_Form.resize(522, 400)
        self.gridLayout_3 = QGridLayout(Temp_Stammdaten_Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(Temp_Stammdaten_Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(Temp_Stammdaten_Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Temp_LW = QListWidget(self.frame_2)
        self.Temp_LW.setObjectName(u"Temp_LW")

        self.gridLayout_2.addWidget(self.Temp_LW, 0, 0, 1, 1)

        self.Temp_LV = QListView(self.frame_2)
        self.Temp_LV.setObjectName(u"Temp_LV")

        self.gridLayout_2.addWidget(self.Temp_LV, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_3 = QFrame(Temp_Stammdaten_Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 45))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.B_Plus = QToolButton(self.frame_3)
        self.B_Plus.setObjectName(u"B_Plus")
        self.B_Plus.setMinimumSize(QSize(32, 32))
        self.B_Plus.setMaximumSize(QSize(32, 32))
        icon = QIcon()
        iconThemeName = u"battery"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../PYSide Tests \u00dcberwachung 07.14", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.B_Plus.setIcon(icon)

        self.horizontalLayout.addWidget(self.B_Plus)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.B_abbrechen = QPushButton(self.frame_3)
        self.B_abbrechen.setObjectName(u"B_abbrechen")

        self.horizontalLayout.addWidget(self.B_abbrechen)

        self.B_speichern = QPushButton(self.frame_3)
        self.B_speichern.setObjectName(u"B_speichern")

        self.horizontalLayout.addWidget(self.B_speichern)


        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 1)


        self.retranslateUi(Temp_Stammdaten_Form)

        QMetaObject.connectSlotsByName(Temp_Stammdaten_Form)
    # setupUi

    def retranslateUi(self, Temp_Stammdaten_Form):
        Temp_Stammdaten_Form.setWindowTitle(QCoreApplication.translate("Temp_Stammdaten_Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Temp_Stammdaten_Form", u"Temperaturen:", None))
        self.B_Plus.setText("")
        self.B_abbrechen.setText(QCoreApplication.translate("Temp_Stammdaten_Form", u"Abbrechen", None))
        self.B_speichern.setText(QCoreApplication.translate("Temp_Stammdaten_Form", u"Speichern", None))
    # retranslateUi

