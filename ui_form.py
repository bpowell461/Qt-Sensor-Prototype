# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHeaderView,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpinBox, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1760, 887)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMaximumSize(QSize(1760, 887))
        self.tempAlarmSlider = QSlider(Widget)
        self.tempAlarmSlider.setObjectName(u"tempAlarmSlider")
        self.tempAlarmSlider.setGeometry(QRect(20, 330, 271, 111))
        self.tempAlarmSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.tempAlarmSlider.setMinimum(-20)
        self.tempAlarmSlider.setMaximum(100)
        self.tempAlarmSlider.setValue(32)
        self.tempAlarmSlider.setOrientation(Qt.Horizontal)
        self.humAlarmSlider = QSlider(Widget)
        self.humAlarmSlider.setObjectName(u"humAlarmSlider")
        self.humAlarmSlider.setGeometry(QRect(20, 450, 271, 111))
        self.humAlarmSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.humAlarmSlider.setMinimum(0)
        self.humAlarmSlider.setMaximum(100)
        self.humAlarmSlider.setValue(10)
        self.humAlarmSlider.setOrientation(Qt.Horizontal)
        self.tempSpinBox = QSpinBox(Widget)
        self.tempSpinBox.setObjectName(u"tempSpinBox")
        self.tempSpinBox.setGeometry(QRect(301, 370, 51, 25))
        self.tempSpinBox.setMinimum(-20)
        self.tempSpinBox.setMaximum(100)
        self.tempSpinBox.setValue(32)
        self.humSpinBox = QSpinBox(Widget)
        self.humSpinBox.setObjectName(u"humSpinBox")
        self.humSpinBox.setGeometry(QRect(300, 490, 51, 25))
        self.humSpinBox.setMaximum(100)
        self.humSpinBox.setValue(10)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 320, 141, 31))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 450, 121, 31))
        self.label_2.setFont(font)
        self.tableWidget = QTableWidget(Widget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(1170, 60, 571, 811))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.readingButton = QPushButton(Widget)
        self.readingButton.setObjectName(u"readingButton")
        self.readingButton.setGeometry(QRect(630, 800, 361, 71))
        icon = QIcon()
        iconThemeName = u"call-start"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.readingButton.setIcon(icon)
        self.continuousButton = QRadioButton(Widget)
        self.continuousButton.setObjectName(u"continuousButton")
        self.continuousButton.setGeometry(QRect(1020, 820, 121, 41))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1430, 10, 101, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_3.setFont(font1)
        self.statTable = QTableWidget(Widget)
        if (self.statTable.columnCount() < 2):
            self.statTable.setColumnCount(2)
        if (self.statTable.rowCount() < 3):
            self.statTable.setRowCount(3)
        self.statTable.setObjectName(u"statTable")
        self.statTable.setGeometry(QRect(670, 360, 271, 131))
        self.statTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.statTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.statTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.statTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.statTable.setRowCount(3)
        self.statTable.setColumnCount(2)
        self.statButton = QPushButton(Widget)
        self.statButton.setObjectName(u"statButton")
        self.statButton.setGeometry(QRect(730, 510, 141, 31))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(750, 320, 101, 21))
        self.label_4.setFont(font1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Sensor Capture Tool", None))
        self.tempSpinBox.setSuffix(QCoreApplication.translate("Widget", u"\u00b0F", None))
        self.humSpinBox.setSuffix(QCoreApplication.translate("Widget", u"%", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Temperature Alarm", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Humidity Alarm", None))
        self.readingButton.setText(QCoreApplication.translate("Widget", u"Capture", None))
        self.continuousButton.setText(QCoreApplication.translate("Widget", u"Continuous", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Readings", None))
        self.statButton.setText(QCoreApplication.translate("Widget", u"Get Statistics", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Statistics", None))
    # retranslateUi

