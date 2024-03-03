# This Python file uses the following encoding: utf-8
import sys
import datetime

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import QTimer, QEventLoop, QDateTime
from PySide6.QtGui import QPixmap, QPainter
import psuedoSensor

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

sensor = psuedoSensor.PseudoSensor()

alarmImg = "alarm.png"

class ImageWidget(QWidget):
    def __init__(self, imagePath, parent):
        super(ImageWidget, self).__init__(parent)
        self.picture = QPixmap(imagePath)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.picture)

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.tempAlarmSlider.valueChanged.connect(lambda x: self.ui.tempSpinBox.setValue(self.ui.tempAlarmSlider.value()))
        self.ui.tempSpinBox.valueChanged.connect(lambda x: self.ui.tempAlarmSlider.setValue(self.ui.tempSpinBox.value()))
        self.ui.humAlarmSlider.valueChanged.connect(lambda x: self.ui.humSpinBox.setValue(self.ui.humAlarmSlider.value()))
        self.ui.humSpinBox.valueChanged.connect(lambda x: self.ui.humAlarmSlider.setValue(self.ui.humSpinBox.value()))

        self.ui.statTable.setHorizontalHeaderLabels(['Temperature', 'Humidity'])
        self.ui.statTable.setVerticalHeaderLabels(['Minimum', 'Maximum', 'Average'])
        self.ui.statTable.horizontalHeader().setStretchLastSection(True)
        self.ui.statTable.verticalHeader().setStretchLastSection(True)

        self.ui.tableWidget.setHorizontalHeaderLabels(['Humidity', '', 'Temperature', '', 'Time'])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.readingButton.clicked.connect(self.captureReading)

        self.ui.statButton.clicked.connect(self.getStats)


    def getStats(self):
        minHum = float(self.ui.humSpinBox.maximum())
        minTemp = float(self.ui.tempSpinBox.maximum())

        maxHum = float(self.ui.humSpinBox.minimum())
        maxTemp = float(self.ui.tempSpinBox.minimum())

        avgHum = 0.0
        avgTemp = 0.0
        avgItems = 0

        for i in range(self.ui.tableWidget.rowCount()-1, -1, -1):
            if(avgItems == 10):
                break;
            hum = float(self.ui.tableWidget.item(i, 0).text())
            temp = float(self.ui.tableWidget.item(i, 2).text())

            if (hum < minHum):
                minHum = hum

            if (temp < minTemp):
                minTemp = temp

            if (hum > maxHum):
                maxHum = hum

            if (temp > maxTemp):
                maxTemp = temp

            avgHum += hum
            avgTemp += temp
            avgItems += 1


        avgHum /= (avgItems)
        avgTemp /= (avgItems)

        self.insertToStatTable(0, 0, minTemp)
        self.insertToStatTable(0, 1, maxTemp)
        self.insertToStatTable(0, 2, avgTemp)

        self.insertToStatTable(1, 0, minHum)
        self.insertToStatTable(1, 1, maxHum)
        self.insertToStatTable(1, 2, avgHum)

    def insertToStatTable(self, col, row, val):
        item = QTableWidgetItem()
        item.setData(0, val)
        self.ui.statTable.setItem(row, col, item)

    def insertTableItem(self):
        hum, temp = sensor.generate_values()
        self.insertItem(hum, temp)

    def captureReading(self):
        if self.ui.continuousButton.isChecked():
            self.ui.readingButton.setEnabled(False)
            self.ui.readingButton.setText("Reading...")
            for i in range(10):
                self.insertTableItem()

                # GUI Friendly Sleep
                loop = QEventLoop()
                QTimer.singleShot(1000, loop.quit)
                loop.exec()
            self.ui.readingButton.setEnabled(True)
            self.ui.readingButton.setText("Capture")
        else:
            self.insertTableItem()


    def insertItem(self, hum, temp):

        rowPos = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPos)

        rowPos = self.ui.tableWidget.rowCount()

        item = QTableWidgetItem()
        item.setData(0, "{:.3f}".format(hum))
        self.ui.tableWidget.setItem(rowPos-1, 0, item)


        if (hum > self.ui.humSpinBox.value()):
            imageItem1 = ImageWidget(alarmImg, self)
            self.ui.tableWidget.setCellWidget(rowPos-1, 1, imageItem1)


        item1 = QTableWidgetItem()
        item1.setData(0, "{:.3f}".format(temp))
        self.ui.tableWidget.setItem(rowPos-1, 2, item1)

        if (temp > self.ui.tempSpinBox.value()):
            imageItem1 = ImageWidget(alarmImg, self)
            self.ui.tableWidget.setCellWidget(rowPos-1, 3, imageItem1)

        item3 = QTableWidgetItem()
        item3.setData(0, QDateTime(datetime.datetime.now()))
        self.ui.tableWidget.setItem(rowPos-1, 4, item3)

        # Force scroll to bottom
        item = self.ui.tableWidget.item(rowPos-1, 0)
        self.ui.tableWidget.scrollToItem(item, QAbstractItemView.PositionAtTop)
        self.ui.tableWidget.selectRow(rowPos-1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
