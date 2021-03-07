import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from main_ui import Ui_mainWindow
import questions


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.pushButton_answer.clicked.connect(self.show_answer)
        self.pushButton_next.clicked.connect(self.show_next)
        self.pushButton_reset.clicked.connect(self.show_reset)
        self.pushButton_about.clicked.connect(self.show_about)
        self.radioButton_N3.setChecked(True)
        self.radioButton_N3.toggled.connect(self.difficulty)
        self.radioButton_N4.toggled.connect(self.difficulty)
        self.radioButton_N5.toggled.connect(self.difficulty)
        self.label_putsubject.setText(questions.question_n3())

    def difficulty(self):
        if self.radioButton_N3.isChecked() == True:
            self.label_putsubject.setText(questions.question_n3())
        elif self.radioButton_N4.isChecked() == True:
            self.label_putsubject.setText(questions.question_n4())
        elif self.radioButton_N5.isChecked() == True:
            self.label_putsubject.setText(questions.question_n5())
        else:
            reply = QMessageBox.information(self, '開發中!', '空資料庫', QMessageBox.Ok)
            return reply

    def show_answer(self):
        self.label_putkanji.setText(questions.kanji)
        self.label_putanswer.setText(questions.chinese)

    def show_next(self):
        if self.radioButton_N3.isChecked():
            self.label_putsubject.setText(questions.question_n3())
        elif self.radioButton_N4.isChecked():
            self.label_putsubject.setText(questions.question_n4())
        elif self.radioButton_N5.isChecked():
            self.label_putsubject.setText(questions.question_n5())
        else:
            pass

    def show_reset(self):
        self.label_putsubject.setText('題目')
        self.label_putkanji.setText('日文漢字')
        self.label_putanswer.setText('中文解答')

    def show_about(self):
        reply = QMessageBox.information(self, '關於', 'Created by Genreal Brothers', QMessageBox.Ok)
        return reply


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())