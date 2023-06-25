
import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QFont

class AnalogClock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analog Clock")
        self.setStyleSheet("background-color: white;")
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(100, 100, 400, 400)
        self.setFixedSize(400, 400)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # Update every 1 second
  
     
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw clock outline
        painter.setPen(QPen(Qt.black, 2))
        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(50, 50, 300, 300)
        painter.drawText(10, 390, "Made by @foysal-2023")

        # Draw numbers
        font = QFont("Arial", 12)
        painter.setFont(font)
        painter.setPen(QPen(Qt.black))
        for i in range(1, 13):
            angle = math.pi * (i - 3) / 6
            x = 200 + 130 * math.cos(angle)
            y = 200 + 130 * math.sin(angle)
            painter.drawText(int(x), int(y), str(i))

        # Draw minute markers (every 5 minutes)
            for j in range(1, 61):
                angle = math.pi * (j - 15) / 30
                x = 200 + 130 * math.cos(angle)
                y = 200 + 130 * math.sin(angle)
                painter.drawText(int(x), int(y), ".")


        # Get current time
        current_time = QTime.currentTime()
        hours = current_time.hour()
        minutes = current_time.minute()
        seconds = current_time.second()

        # Draw hour hand
        hour_angle = (hours + minutes / 60) * 30
        hour_x = 200 + 80 * math.sin(math.radians(hour_angle))
        hour_y = 200 - 80 * math.cos(math.radians(hour_angle))
        painter.setPen(QPen(Qt.black, 4))
        painter.drawLine(200, 200, hour_x, hour_y)

        # Draw minute hand
        minute_angle = (minutes + seconds / 60) * 6
        minute_x = 200 + 110 * math.sin(math.radians(minute_angle))
        minute_y = 200 - 110 * math.cos(math.radians(minute_angle))
        painter.setPen(QPen(Qt.black, 3))
        painter.drawLine(200, 200, minute_x, minute_y)

        # Draw second hand
        second_angle = seconds * 6
        second_x = 200 + 120 * math.sin(math.radians(second_angle))
        second_y = 200 - 120 * math.cos(math.radians(second_angle))
        painter.setPen(QPen(Qt.red, 2))
        painter.drawLine(200, 200, second_x, second_y)

        # Highlight 12, 6, 9
        painter.setPen(QPen(Qt.red, 3))
        painter.drawLine(200, 65, 200, 75)  # 12 o'clock
        painter.drawLine(200, 325, 200, 335)  # 6 o'clock
        painter.drawLine(65, 200, 75, 200)  # 9 o'clock
        painter.drawLine(325, 200, 335, 200)  # 3 o'clock
        
        # Draw center dot
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(197, 197, 6, 6)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock= AnalogClock()
    clock.show()
    sys.exit(app.exec_())

'''
This is a simple analog clock application written in Python with PyQt5. It displays the current time and highlights the 12, 6, and 9 o'clock positions. The clock is updated every second.
The clock is drawn using QPainter. The clock outline is drawn using drawEllipse(). The numbers are drawn using drawText(). The minute markers are drawn using drawText() as well. The hour, minute, and second hands are drawn using drawLine().
The clock is updated every second using a QTimer. The QTimer is started in the constructor of the AnalogClock class. The QTimer is connected to the update() method of the AnalogClock class. The update() method is called every second and the clock is redrawn.

pip install PyQt5


'''