from PyQt5.QtWidgets import (QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QProcess

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