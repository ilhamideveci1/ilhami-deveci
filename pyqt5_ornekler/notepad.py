import sys
import os
from PyQt5.QtWidgets import QWidget , QApplication ,QHBoxLayout, QTextEdit , QLabel , QPushButton , QVBoxLayout , QFileDialog,QApplication,QAction,qApp,QMainWindow


class Notepad (QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani=QTextEdit()
        self.temizle=QPushButton("temizle")
        self.ac=QPushButton("aç")
        self.kaydet=QPushButton("kaydet")
        h_box=QHBoxLayout()
        h_box.addWidget(self.ac)


        h_box.addWidget(self.kaydet)
        h_box.addWidget(self.temizle)


        v_box=QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("notepad")
        self.temizle.clicked.connect(self.yazitemizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)


    def yazitemizle(self):
        self.yazi_alani.clear()
    def dosya_ac(self):
        dosya_ismi=QFileDialog.getOpenFileName(self,"dosya aç",os.getenv("HOME"))
        with open(dosya_ismi[0],"r",encoding="utf-8") as file:
            self.yazi_alani.setText(file.read())
        print(dosya_ismi)
    def dosya_kaydet(self):
        dosya_ismi=QFileDialog.getSaveFileName(self,"dosya kaydet",os.getenv("HOME"))
        with open (dosya_ismi[0],"w",encoding="utf-8") as file:
            file.write(self.yazi_alani.toPlainText())

class Menu(QMainWindow):
    def __init__(self):

        super().__init__()
        self.pencere=Notepad()
        self.setCentralWidget(self.pencere)
        self.menuleri_olustur()
    def menuleri_olustur(self):
        menubar=self.menuBar()
        dosya=menubar.addMenu("dosya")
        dosya_ac=QAction("dosya aç",self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet=QAction("dosya kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        temizle=QAction("temizle",self)
        temizle.setShortcut("Ctrl+D")
        cikis=QAction("çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(temizle)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)
        self.setWindowTitle("metin editörü")
        self.show()
    def response(self,action):
        if action.text()== "dosya aç":
            self.pencere.dosya_ac()

        elif action.text()== "dosya kaydet":
            self.pencere.dosya_kaydet()

        elif action.text()== "temizle":
            self.pencere.yazitemizle()

        elif action.text()=="çıkış":
            qApp.quit()


app= QApplication (sys.argv)
menu=Menu()
sys.exit(app.exec_())