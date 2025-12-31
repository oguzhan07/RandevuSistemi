from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QPixmap, QIcon
import os
import sys
from datetime import datetime, timedelta

class Customer(QMainWindow):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.setWindowTitle("Kuaför Randevu Sistemi")
        self.showMaximized()
        self.user = QFrame()
        self.setCentralWidget(self.user)

        self.arka_plan = QFrame()
        self.arka_plan.setGeometry(0, 0, 1920, 1080)
        self.arka_plan.setParent(self.user)
        self.arka_plan.setStyleSheet("""
                        background-image: url(images/arka-plan.png);
                        background-repeat: no-repeat;
                        background-position: center;
                        background-size: cover;
                    """)

        self.date_background = QFrame()
        self.date_background.setParent(self.user)
        self.date_background.setGeometry(300, 50, 1000, 500)
        self.date_background.setStyleSheet("""
                            background: qlineargradient(
                                x1:1, y1:0,
                                x2:0, y2:0,
                                stop:0 #2fa5b4,
                                stop:1 #0d395a);
                            border-radius: 50px;
                            """)

        self.meet_background = QFrame()
        self.meet_background.setParent(self.user)
        self.meet_background.setGeometry(300, 570, 1000, 160)
        self.meet_background.setStyleSheet("""
                    background-color: #0d395a;
                    border-radius: 35px;
                    """)

        ##################################################################

        base_dir = os.path.dirname(__file__)
        font_path = os.path.join(base_dir, "Fonts", "Oswald-Medium.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id == -1:
            print("Font yüklenemedi, fallback font kullanılıyor")

        else:
            family = QFontDatabase.applicationFontFamilies(font_id)[0]
            oswald = QFont(family)
            oswald.setPointSize(30),

            oswald2 = QFont(family)
            oswald2.setPointSize(20)
        ####################################################################





        letter_of_days = ["P", "S", "Ç", "P", "C", "C", "P"]
        week = ["pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"]

        k = 30
        for i in range(7):
            day_background = QFrame(self.date_background)
            day_background.setGeometry(k, 30, 110, 80)
            day_background.setStyleSheet("""
                background-color: #0d395a;
                border-radius: 35px;
            """)
            day_background.raise_()
            day_label = QLabel(letter_of_days[i], day_background)
            day_label.setGeometry(45, 10, 50, 60)
            day_label.setFont(oswald)
            day_label.raise_()
            k += 140



        y = 140
        days = 0
        liste = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30
]
        for j in range(4):
            x = 30
            for i in range(7):

                now = datetime.now()  # gün.ay.yıl
                print("Now: ", now)
                future = now + timedelta(days)  # gün.ay.yıl
                index_of_future = future.weekday()  # 0 - 6 arasında
                letter_of_future_day = letter_of_days[index_of_future]  # p, s, ç, p, c

                print("Future: ", future)
                print("İndex of future: ", index_of_future)
                print("Letter of future day: ", letter_of_future_day)


                self.num_background = QFrame()
                self.num_background.setParent(self.date_background)
                self.num_background.setGeometry(x, y, 110, 70)
                self.num_background.setStyleSheet("""
                                            background-color: #ffffff;
                                            border-radius: 35px;
                                            """)
                self.num_background.raise_()

                self.num_label = QLabel()
                self.num_label.setParent(self.num_background)
                self.num_label.setGeometry(20, 5, 50, 60)
                self.num_label.setFont(oswald)
                self.num_label.raise_()
                k += 140
                x += 140
                days += 1
            y += 80




#####################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ekran = Customer()
    ekran.show()
    app.exec()

