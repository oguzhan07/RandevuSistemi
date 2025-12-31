from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QApplication, QWidget, QMessageBox
import sys
from signup import SignUp
from customer import Customer
import pymongo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kuaför Randevu Sistemi")
        self.resize(600, 400)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.signup = SignUp(self.stack)
        self.customer = Customer(self.stack)
        self.stack.addWidget(self.signup)  # index 0
        self.stack.addWidget(self.customer)  # index 1
        self.stack.setCurrentIndex(0)
        self.signup.giris_button.clicked.connect(self.eposta_sifre_dogru_mu)

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["RandevuSistemi"]
        self.mycol = mydb["randevular"]

    def eposta_sifre_dogru_mu(self):
        kullanici_adi = self.signup.eposta_input.text()
        sifre = self.signup.sifre_input.text()
        true_or_false = self.mycol.find_one({"eposta": kullanici_adi, "sifre": sifre})
        if true_or_false:
            self.stack.setCurrentIndex(1)
        else:
            QMessageBox.warning(self, "Hata", "Bir şeyler eksik ya da yanlış!")






app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
