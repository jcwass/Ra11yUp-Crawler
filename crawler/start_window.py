import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class start_window(QWidget):
    def __init__(self, crawler, app, parent = None):
        super(start_window, self).__init__(parent)
        self.crawler = crawler
        self.app = app
        self.win = QWidget()

        self.l1 = QLabel('URL')
        self.url_input = QLineEdit()
        self.url_input.setText('https://ra11yup.linearbsystems.net')

        self.fbox = QFormLayout()
        self.fbox.addRow(self.l1, self.url_input)

        self.b1 = QPushButton("Submit")
        self.b1.setCheckable(True)
        self.b1.clicked.connect(self.btnstate)

        self.b2 = QPushButton("Cancel")
        self.b2.setCheckable(True)
        self.b2.clicked.connect(self.btnstate)

        self.hbox = QHBoxLayout()
        self.robots = QRadioButton("Check Robots?")
        self.hbox.addWidget(self.robots)
        self.hbox.addStretch()
        self.fbox.addRow(QLabel("Options"), self.hbox)
        self.fbox.addRow(self.b1, self.b2)

        self.setLayout(self.fbox)
        self.setWindowTitle("Button demo")

    def btnstate(self):
        if self.b1.isChecked():
            self.crawler.start_crawls(self.url_input.text(), self.robots.isChecked())
        elif self.b2.isChecked():
            sys.exit()

                