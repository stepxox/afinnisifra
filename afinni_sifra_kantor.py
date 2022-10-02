import sys
import string
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic
 
qtCreatorFile = "afinnisifra_kantor.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


 
class MyApp(QMainWindow, Ui_MainWindow):
    
    hodnotyA = ["1","3","5","7","9","11","15","17","19","21","23","25"]
    
    def mod_inverse(self, a, m):
        for x in range(1, m):
            if ((a % m) * (x % m)) % m == 1:
                return x
        return -1
    
    def to_normal(self):
        m = 26
        
        unwanted_characters = ['.', '-', ',', '!', '_', ')', '(', '<', '>']

        numbers = [t.upper() for t in ["+", "ě", "š", "č", "ř", "ž", "ý", "á", "í", "é"]]

        abc = string.ascii_uppercase
        a = int(self.comboBoxA.currentText())
        b = int(self.lineEditB.text())
        mod_inverse=self.mod_inverse(a, m)
        normal = ""
        cipher = self.lineEditDesifrovani.text()
        cipher = cipher.upper()

        for char in unwanted_characters:
            cipher = cipher.replace(char, "")

        cipher = cipher.replace(" ", "").replace("XMEZERAX", " ")

        for c in cipher:
            if c in abc:
                normal += abc[((abc.index(c) - b) * mod_inverse) % m]
            elif c == " ":
                normal += " "
            elif c in numbers:
                normal += str(numbers.index(c))

        self.lineEditVysledek.setText(normal)


    def to_cipher(self):
        m = 26

        unwanted_characters = ['.', '-', ',', '!', '_', ')', '(', '<', '>']

        numbers = [t.upper() for t in ["+", "ě", "š", "č", "ř", "ž", "ý", "á", "í", "é"]]

        abc = string.ascii_uppercase
        text=self.lineEditSifrovani.text()
        a = int(self.comboBoxA.currentText())
        b = int(self.lineEditB.text())
        cipher = ""
        cipher_list = []
        text = text.upper()

        for char in unwanted_characters:
            text = text.replace(char, "")

        text_list = list(text)

        for c in text_list:
            if c in abc:
                cipher_list.append(abc[(a * abc.index(c) + b) % m])
            elif c == " ":
                cipher_list.append("XMEZERAX")
            elif c.isnumeric():
                cipher_list.append(numbers[int(c)])

        for i, c in enumerate(cipher_list):
            cipher += str(c)

            if i > 0 and i % 5 == 0:
                cipher += " "

        self.lineEditVysledek.setText(cipher)
    
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButtonSifrovat.clicked.connect(self.to_cipher)
        self.pushButtonDesifrovat.clicked.connect(self.to_normal)
        self.comboBoxA.addItems(self.hodnotyA)
        
        
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
    
