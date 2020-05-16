from PyQt5 import QtWidgets, QtCore
from Form import Ui_MainWindow
import sys


def luhnAlg(number: str):
    number = number.replace(" ", "")
    number = number[::-1]
    summ = 0


    for i in range(0, len(number)):
        if ((i + 1) % 2 == 0) & (i != 0):
            summ = summ + ((int(number[i]) * 2) % 10) + ((int(number[i]) * 2) // 10)
        else:
            summ += int(number[i])

    if summ % 10 == 0:
        return 'Valid'
    else:
        return 'Invalid'


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.checkButton.clicked.connect(self.checkBtn_clicked)

    def checkBtn_clicked(self):
        self.ui.help_TextEdit.hide()
        validity = luhnAlg(self.ui.number_LineEdit.text())
        self.ui.validation_LineEdit.setEnabled(True)
        self.ui.validation_LineEdit.setText(validity)
        if len(self.ui.number_LineEdit.text().replace(" ", "")) < 16:
            self.ui.help_TextEdit.show()
            self.ui.help_TextEdit.setText("Минимально возможное количество цифр: 16, максимум: 18")


def main():
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
