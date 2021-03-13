import sys

from PyQt5 import QtWidgets,QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 2")
    etiket1=QtWidgets.QLabel(pencere)
    etiket1.setText("burası bir yazıdır.")
    etiket1.move(200,30)
    etiket2=QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("a.png"))
    etiket2.move(100,50)
    pencere.setGeometry(100,140,500,500)

    pencere.show()

    sys.exit(app.exec_())


Pencere()
