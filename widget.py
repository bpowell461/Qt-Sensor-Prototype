import sys
import datetime

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import QTimer, QEventLoop, QDateTime
from PySide6.QtGui import QPixmap, QPainter
import psuedoSensor  # Assuming this is your custom module
from ui_form import Ui_Widget  # Assuming ui_form.py is generated from a .ui file

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
        self.setupUI()

    def setupUI(self):
        self.setupSliders()
        self.setupTables()
        self.ui.readingButton.clicked.connect(self.captureReading)
        self.ui.statButton.clicked.connect(self.calculateStatistics)

    def setupSliders(self):
        self.ui.tempAlarmSlider.valueChanged.connect(lambda x: self.ui.tempSpinBox.setValue(x))
        self.ui.tempSpinBox.valueChanged.connect(lambda x: self.ui.tempAlarmSlider.setValue(x))
        self.ui.humAlarmSlider.valueChanged.connect(lambda x: self.ui.humSpinBox.setValue(x))
        self.ui.humSpinBox.valueChanged.connect(lambda x: self.ui.humAlarmSlider.setValue(x))

    def setupTables(self):
        self.ui.statTable.setHorizontalHeaderLabels(['Humidity', 'Temperature'])
        self.ui.statTable.setVerticalHeaderLabels(['Minimum', 'Maximum', 'Average'])
        self.ui.statTable.horizontalHeader().setStretchLastSection(True)
        self.ui.statTable.verticalHeader().setStretchLastSection(True)

        self.ui.tableWidget.setHorizontalHeaderLabels(['Humidity', '', 'Temperature', '', 'Time'])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

    def calculateStatistics(self):
        readings = []
        for i in range(self.ui.tableWidget.rowCount()):
            hum = float(self.ui.tableWidget.item(i, 0).text())
            temp = float(self.ui.tableWidget.item(i, 2).text())
            readings.append((hum, temp))

        if readings:
            min_hum = min(readings, key=lambda x: x[0])[0]
            max_hum = max(readings, key=lambda x: x[0])[0]
            avg_hum = sum(hum for hum, _ in readings) / len(readings)

            min_temp = min(readings, key=lambda x: x[1])[1]
            max_temp = max(readings, key=lambda x: x[1])[1]
            avg_temp = sum(temp for _, temp in readings) / len(readings)

            self.insertToStatTable(0, [min_hum, min_temp])
            self.insertToStatTable(1, [max_hum, max_temp])
            self.insertToStatTable(2, [avg_hum, avg_temp])

    def insertToStatTable(self, row, values):
        for col, val in enumerate(values):
            item = QTableWidgetItem("{:.3f}".format(val))
            self.ui.statTable.setItem(row, col, item)

    def insertTableItem(self, hum, temp):
        rowPos = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPos)
        self.insertItem(rowPos, hum, temp)

    def captureReading(self):
        if self.ui.continuousButton.isChecked():
            self.captureContinuousReadings()
        else:
            hum, temp = sensor.generate_values()
            self.insertTableItem(hum, temp)

    def captureContinuousReadings(self):
        self.ui.readingButton.setEnabled(False)
        self.ui.readingButton.setText("Reading...")
        for _ in range(10):
            hum, temp = sensor.generate_values()
            self.insertTableItem(hum, temp)
            self.sleep(1000)  # Sleep for 1 second
        self.ui.readingButton.setEnabled(True)
        self.ui.readingButton.setText("Capture")

    def insertItem(self, row, hum, temp):
        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem("{:.3f}".format(hum)))
        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem("{:.3f}".format(temp)))

        if hum > self.ui.humSpinBox.value():
            self.ui.tableWidget.setCellWidget(row, 1, ImageWidget(alarmImg, self))
        if temp > self.ui.tempSpinBox.value():
            self.ui.tableWidget.setCellWidget(row, 3, ImageWidget(alarmImg, self))

        self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(QDateTime.currentDateTime().toString()))

        # Force scroll to bottom
        item = self.ui.tableWidget.item(row, 0)
        self.ui.tableWidget.scrollToItem(item, QAbstractItemView.PositionAtTop)
        self.ui.tableWidget.selectRow(row)

    def sleep(self, milliseconds):
        loop = QEventLoop()
        QTimer.singleShot(milliseconds, loop.quit)
        loop.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
