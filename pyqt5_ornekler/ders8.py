import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QRadioButton


class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.radio_yazisi=QLabel("hangi dili seviyorsun")
        self.java=QRadioButton("java")
        self.c=QRadioButton("c")
        self.python=QRadioButton("python")
        self.yazi_alani=QLabel("")
        self.buton=QPushButton("gönder")
        v_box=QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)

        v_box.addWidget(self.java)
        v_box.addWidget(self.c)
        v_box.addWidget(self.python)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.buton.clicked.connect(lambda : self.click (self.python.isChecked(),self.c.isChecked(),self.java.isChecked(),self.yazi_alani))
        self.setWindowTitle("radio buton")
        self.show()
    def click(self,python,c,java,yazi_alani):
        if python:
            yazi_alani.setText("python işaretlendi")
        if c:
            yazi_alani.setText("c işaretlendi")
        if java:
            yazi_alani.setText("java işaretlendi")


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())