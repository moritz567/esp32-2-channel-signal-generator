# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Presets.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QToolButton,
    QWidget)

class Ui_Presets_Form(object):
    def setupUi(self, Presets_Form):
        if not Presets_Form.objectName():
            Presets_Form.setObjectName(u"Presets_Form")
        Presets_Form.resize(655, 421)
        self.gridLayout_3 = QGridLayout(Presets_Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(Presets_Form)
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

        self.frame_2 = QFrame(Presets_Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.TW_Presets = QTableWidget(self.frame_2)
        if (self.TW_Presets.columnCount() < 6):
            self.TW_Presets.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.TW_Presets.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TW_Presets.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TW_Presets.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TW_Presets.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TW_Presets.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TW_Presets.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.TW_Presets.rowCount() < 1):
            self.TW_Presets.setRowCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TW_Presets.setVerticalHeaderItem(0, __qtablewidgetitem6)
        self.TW_Presets.setObjectName(u"TW_Presets")

        self.gridLayout_2.addWidget(self.TW_Presets, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_3 = QFrame(Presets_Form)
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
            icon.addFile(u"../OneDrive/PYSide Tests \u00dcberwachung 07.14", QSize(), QIcon.Normal, QIcon.Off)

        self.B_Plus.setIcon(icon)

        self.horizontalLayout.addWidget(self.B_Plus)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.B_abbrechen = QPushButton(self.frame_3)
        self.B_abbrechen.setObjectName(u"B_abbrechen")

        self.horizontalLayout.addWidget(self.B_abbrechen)

        self.B_speichern = QPushButton(self.frame_3)
        self.B_speichern.setObjectName(u"B_speichern")

        self.horizontalLayout.addWidget(self.B_speichern)


        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 1)


        self.retranslateUi(Presets_Form)

        QMetaObject.connectSlotsByName(Presets_Form)
    # setupUi

    def retranslateUi(self, Presets_Form):
        Presets_Form.setWindowTitle(QCoreApplication.translate("Presets_Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Presets_Form", u"Presets Schwingkreis", None))
        ___qtablewidgetitem = self.TW_Presets.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Presets_Form", u"Name", None));
        ___qtablewidgetitem1 = self.TW_Presets.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Presets_Form", u"Frequenz", None));
        ___qtablewidgetitem2 = self.TW_Presets.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Presets_Form", u"Spannung", None));
        ___qtablewidgetitem3 = self.TW_Presets.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Presets_Form", u"Kapazit\u00e4t", None));
        ___qtablewidgetitem4 = self.TW_Presets.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Presets_Form", u"Induktivit\u00e4t", None));
        ___qtablewidgetitem5 = self.TW_Presets.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Presets_Form", u"Widerstand", None));
        self.B_Plus.setText("")
        self.B_abbrechen.setText(QCoreApplication.translate("Presets_Form", u"Abbrechen", None))
        self.B_speichern.setText(QCoreApplication.translate("Presets_Form", u"Speichern", None))
    # retranslateUi

