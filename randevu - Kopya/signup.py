from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QPixmap, QIcon
from PyQt6.QtWidgets import QStackedWidget
import os
import sys
import pymongo



class SignUp(QMainWindow):
    def __init__(self, stack):
        super().__init__()


        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["RandevuSistemi"]
        self.mycol = mydb["randevular"]


        self.setWindowTitle("Kuaför Randevu Sistemi")
        self.showMaximized()
        self.widget = QFrame()
        self.setCentralWidget(self.widget)

        self.arka_plan = QFrame()
        ########### GPT SAĞOLSUN ###########
        self.arka_plan.setGeometry(0, 0, 1920, 1080)
        self.arka_plan.setParent(self.widget)
        self.arka_plan.setStyleSheet("""
                background-image: url(images/arka-plan.png);
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            """)

        ####################################

        #Oturum kısmının arka planı
        self.oturum_arka_plan = QFrame()
        self.oturum_arka_plan.setParent(self.widget)
        self.oturum_arka_plan.setGeometry(100, 300, 600, 450)
        self.oturum_arka_plan.setStyleSheet("""
                    background: qlineargradient(
                        x1:1, y1:0,
                        x2:0, y2:0,
                        stop:0 #2fa5b4,
                        stop:1 #0d395a);
                    border-radius: 50px;
                    """)


        #Yönetici oturum sekmesi başlığı
        self.yonetici = QFrame()
        self.yonetici.setParent(self.widget)
        self.yonetici.setGeometry(130, 330, 250, 70)
        self.yonetici.raise_()
        self.yonetici.setStyleSheet("""
                            background: qlineargradient(
                                x1:1, y1:0,
                                x2:0, y2:0,
                                stop:0 #0d395a,
                                stop:1 #2fa5b4);
                            border-radius: 35px;
                            """)


        # Oturum2 kısmının arka planı
        self.oturum_arka_plan2 = QFrame()
        self.oturum_arka_plan2.setParent(self.widget)
        self.oturum_arka_plan2.setGeometry(130, 420, 550, 300)
        self.oturum_arka_plan2.raise_()
        self.oturum_arka_plan2.setStyleSheet("""
                    background-color: #2fa5b4;
                    border-radius: 35px;
                    """)


        # E-posta input
        self.eposta = QFrame()
        self.eposta.setParent(self.widget)
        self.eposta.setGeometry(150, 450, 510, 70)
        self.eposta.raise_()
        self.eposta.setStyleSheet("""
                            background-color: #0d3758;
                            border-radius: 35px;
                            """)


        # Sifre input
        self.sifre = QFrame()
        self.sifre.setParent(self.widget)
        self.sifre.setGeometry(150, 540, 510, 70)
        self.sifre.raise_()
        self.sifre.setStyleSheet("""
                                    background-color: #0d3758;
                                    border-radius: 35px;
                                    """)

        # Giriş butonu
        self.giris = QFrame()
        self.giris.setParent(self.widget)
        self.giris.setGeometry(150, 630, 510, 70)
        self.giris.raise_()
        self.giris.setStyleSheet("""
                                            background-color: #0d3758;
                                            border-radius: 35px;
                                            """)


        # Still Room Kuaför
        self.still = QFrame()
        self.still.setParent(self.widget)
        self.still.setGeometry(750, 300, 700, 220)
        self.still.setStyleSheet("""
                            background: qlineargradient(
                                x1:1, y1:0,
                                x2:0, y2:0,
                                stop:0 #2fa5b4,
                                stop:1 #0d395a);
                            border-radius: 50px;
                            """)

        # Telefon numarası ve adres
        self.telefon = QFrame()
        self.telefon.setParent(self.widget)
        self.telefon.setGeometry(750, 530, 700, 220)
        self.telefon.setStyleSheet("""
                            background: qlineargradient(
                                x1:1, y1:0,
                                x2:0, y2:0,
                                stop:0 #2fa5b4,
                                stop:1 #0d395a);
                            border-radius: 50px;
                            """)

        #################   Fontlar ve Yazılar  ####################

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



        base_dir = os.path.dirname(__file__)
        font_path = os.path.join(base_dir, "Fonts", "Chewy-Regular.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id == -1:
            print("Font yüklenemedi, fallback font kullanılıyor")

        else:
            family = QFontDatabase.applicationFontFamilies(font_id)[0]
            chewy = QFont(family)
            chewy.setPointSize(60)

        base_dir = os.path.dirname(__file__)
        font_path = os.path.join(base_dir, "Fonts", "Rye-Regular.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id == -1:
            print("Font yüklenemedi, fallback font kullanılıyor")

        else:
            family = QFontDatabase.applicationFontFamilies(font_id)[0]
            rye = QFont(family)
            rye.setPointSize(50)



        # self.eposta_label = QLabel("E-posta")
        # self.eposta_label.setParent(self.widget)
        # self.eposta_label.setGeometry(150, 495, 150, 50)
        # self.eposta_label.setFont(oswald)

        # self.password_label = QLabel("Şifre")
        # self.password_label.setParent(self.widget)
        # self.password_label.setGeometry(150, 580, 150, 60)
        # self.password_label.setFont(oswald)

        self.still_room = QLabel("Still Room Kuaför")
        self.still_room.setParent(self.widget)
        self.still_room.setGeometry(780, 300, 400, 100)
        self.still_room.setFont(oswald)

        self.still_room_comment = QLabel("""Bizim işimiz saç kesmek değil, still oluşturmak.
Hedefimiz size en yakışanı bulmak.""")
        self.still_room_comment.setParent(self.widget)
        self.still_room_comment.setGeometry(780, 340, 600, 200)
        self.still_room_comment.setFont(oswald2)
        self.still_room_comment.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.still_room_comment.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.still_room = QLabel("Oturum Aç")
        self.still_room.setParent(self.widget)
        self.still_room.setGeometry(170, 320, 250, 80)
        self.still_room.setFont(oswald)

        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, "Images", "phone.png")
        self.phone = QLabel()
        pixmap = QPixmap(image_path)
        self.phone.setPixmap(pixmap)
        self.phone.setParent(self.widget)
        self.phone.setGeometry(780, 560, 64, 64)

        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, "Images", "location.png")
        self.location = QLabel()
        pixmap = QPixmap(image_path)
        self.location.setPixmap(pixmap)
        self.location.setParent(self.widget)
        self.location.setGeometry(780, 650, 64, 64)

        self.phone_num = QLabel("0 (542) 480 75 60")
        self.phone_num.setParent(self.widget)
        self.phone_num.setGeometry(860, 560, 500, 60)
        self.phone_num.setFont(oswald)

        self.phone_num = QLabel("Gül mah. Menekşe sk. no: 1")
        self.phone_num.setParent(self.widget)
        self.phone_num.setGeometry(860, 650, 500, 60)
        self.phone_num.setFont(oswald)

        self.phone_num = QLabel("Gül mah. Menekşe sk. no: 1")
        self.phone_num.setParent(self.widget)
        self.phone_num.setGeometry(860, 650, 500, 60)
        self.phone_num.setFont(oswald)

        self.top_head = QLabel("Still Room")
        self.top_head.setParent(self.widget)
        self.top_head.setGeometry(550, 50, 400, 100)
        self.top_head.setFont(rye)
        self.top_head.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.top_head.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.top_head = QLabel("Randevu Sistemi")
        self.top_head.setParent(self.widget)
        self.top_head.setGeometry(450, 150, 600, 100)
        self.top_head.setFont(rye)
        self.top_head.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.top_head.setAlignment(Qt.AlignmentFlag.AlignVCenter)


        ##################################################

        #################   İnputlar  ####################

        self.eposta_input = QLineEdit()
        self.eposta_input.setParent(self.eposta)
        self.eposta_input.setGeometry(20, 0, 370, 70)
        self.eposta_input.setPlaceholderText("E-posta adresinizi girin !")
        self.eposta_input.setStyleSheet("""
                font-size: 25px;
                font-family: oswald;
        """)

        self.sifre_input = QLineEdit()
        self.sifre_input.setParent(self.sifre)
        self.sifre_input.setGeometry(20, 0, 370, 70)
        self.sifre_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.sifre_input.setPlaceholderText("Şifrenizi girin !")
        self.sifre_input.setStyleSheet("""
                        font-size: 25px;
                        font-family: oswald;
                """)
        ##################################################

        #################   Buton  ####################
        self.stack = stack
        self.giris_button = QPushButton("Giriş", self)

        self.giris_button.setParent(self.giris)
        self.giris_button.setGeometry(0, 0, 510, 70)
        self.giris.raise_()
        self.giris_button.raise_()
        self.giris_button.setStyleSheet("""
        QPushButton {
            background-color: #0d395a;
            color: white;
            font-size: 25px;
            font-family: oswald;
            border-radius: 35px;
        }

        QPushButton:hover {
            background-color: #145a8d;
        }

        QPushButton:pressed {
            background-color: #0a2a40;
        }
        """)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ekran = SignUp()
    ekran.show()
    app.exec()