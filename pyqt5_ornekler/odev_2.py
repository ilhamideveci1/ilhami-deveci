import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QLabel, QPushButton, QVBoxLayout, QApplication, QLineEdit


class mailsender(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.sifre=QLineEdit()

        self.username=QLineEdit()
        self.gonderici=QLineEdit()
        self.alici=QLineEdit()
        self.konu = QLineEdit()
        self.icerik=QLineEdit()
        self.gonder=QPushButton("Gönder")
        self.temizle=QPushButton("Temizle")
        self.etiket1 = QLabel("Kullanıcı Adı:")
        self.etiket2 = QLabel("Şifre:")
        self.etiket3 = QLabel("Gönderen:")
        self.etiket4 = QLabel("Alıcı:")
        self.etiket5 = QLabel("Konu:")
        self.etiket6 = QLabel("Metin Giriniz:")
        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()
        h_box4 = QHBoxLayout()
        h_box5 = QHBoxLayout()
        h_box6 = QHBoxLayout()
        h_box7 = QHBoxLayout()
        h_box1.addWidget(self.etiket1)
        h_box1.addWidget(self.username)
        h_box2.addWidget(self.etiket2)
        h_box2.addWidget(self.sifre)
        h_box3.addWidget(self.etiket3)
        h_box3.addWidget(self.gonderici)
        h_box4.addWidget(self.etiket4)
        h_box4.addWidget(self.alici)
        h_box5.addWidget(self.etiket5)
        h_box5.addWidget(self.konu)
        h_box6.addWidget(self.etiket6)
        h_box6.addWidget(self.icerik)
        h_box7.addWidget(self.gonder)
        h_box7.addWidget(self.temizle)
        v_box=QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)
        v_box.addLayout(h_box6)
        v_box.addLayout(h_box7)
        self.setLayout(v_box)
        self.temizle.clicked.connect(self.Temizle)
        self.gonder.clicked.connect(self.Gonder)
        self.show()
    def Temizle(self):
        self.icerik.clear()
        self.konu.clear()
    def Gonder(self):


        self.mesaj = MIMEMultipart()

        self.mesaj["From"] = self.gonderici.text()
        self.mesaj["To"] = self.alici.text()

        self.mesaj["Subject"] = self.konu.text()

        self.yazi = self.icerik.text()

        self.mesaj_govdesi = MIMEText(self.yazi, "plain")

        self.mesaj.attach(self.mesaj_govdesi)

        try:
            self.mail = smtplib.SMTP("smtp.gmail.com", 587)

            self.mail.ehlo()

            self.mail.starttls()

            self.mail.login(self.username.text(), self.sifre.text())

            self.mail.sendmail(self.mesaj["From"], self.mesaj["To"], self.mesaj.as_string())

            print("Mail Başarıyla Gönderildi....")

            self.mail.close()

        except:
            sys.stderr.write("Bir sorun oluştu!")
            sys.stderr.flush()




app = QApplication(sys.argv)
mailsender = mailsender()
sys.exit(app.exec_())
