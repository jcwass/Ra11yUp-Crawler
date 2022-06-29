from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QProcess
import sys

class MainWindow(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.p = None
        self.args = []
        self.setFixedWidth(800)

        self.l1 = QLabel('URL')
        self.url_input = QLineEdit()
        self.url_input.setText('https://ra11yup.linearbsystems.net')

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        self.robots = QRadioButton("Check Robots?")
        

        l = QVBoxLayout()
        l.addWidget(self.url_input)
        l.addWidget(self.robots)
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start('python3', ['Ra11yUp-Crawler/crawler/crawl_start.py',self.url_input.text(), str(self.robots.isChecked())])

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None






# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from crawler.validator import Validator
# class start_window(QWidget):
#     def __init__(self, crawler, app, parent = None):
#         super(start_window, self).__init__(parent)
#         self.validator = Validator()

#         self.crawler = crawler
#         self.app = app
#         self.win = QWidget()

#         self.l1 = QLabel('URL')
#         self.url_input = QLineEdit()
#         self.url_input.setText('https://ra11yup.linearbsystems.net')

#         self.fbox = QFormLayout()
#         self.fbox.addRow(self.l1, self.url_input)

#         self.b1 = QPushButton("Submit")
#         self.b1.setCheckable(True)
#         self.b1.clicked.connect(self.btnstate)
#         self.b1.clearFocus()

#         self.b2 = QPushButton("Cancel")
#         self.b2.setCheckable(True)
#         self.b2.clicked.connect(self.btnstate)

#         self.hbox = QHBoxLayout()
#         self.robots = QRadioButton("Check Robots?")
#         self.hbox.addWidget(self.robots)
#         self.hbox.addStretch()
#         self.fbox.addRow(QLabel("Options"), self.hbox)
#         self.fbox.addRow(self.b1, self.b2)

#         self.setLayout(self.fbox)
#         self.setWindowTitle("Button demo")

#     def btnstate(self):
#         if self.b1.isChecked():
#             if self.validator.does_url_exist(self.url_input.text()):
#                 self.crawler.start_crawls(self.url_input.text(), self.robots.isChecked())
#             else:
#                 msg = QMessageBox()
#                 msg.setIcon(QMessageBox.Critical)
#                 msg.setText("Invalid")
#                 msg.setInformativeText('Invalid URL Provided, please try another.')
#                 msg.setWindowTitle("Invalid")
#                 msg.exec_()
#             self.b1.setChecked(False)
#         elif self.b2.isChecked():
#             sys.exit()

                