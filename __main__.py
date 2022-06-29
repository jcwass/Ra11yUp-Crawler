import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from crawler.start_window import MainWindow
app = QApplication(sys.argv)

w = MainWindow(app)
w.show()

app.exec_()