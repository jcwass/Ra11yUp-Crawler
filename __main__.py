import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from crawler.crawler import Crawler
from crawler.start_window import start_window
crawler = Crawler()
app = QApplication(sys.argv)
ex = start_window(crawler, app)
ex.setGeometry(250,250,400,150)
ex.show()
sys.exit(app.exec_())
# crawler.start_crawls()