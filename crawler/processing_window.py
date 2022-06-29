import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from crawler.validator import Validator
class start_window(QWidget):
    def __init__(self, crawler, app, parent = None):
        super(start_window, self).__init__(parent)