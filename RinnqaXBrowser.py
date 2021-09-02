import sys

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        #----------------------navbar-------------------------
        #creating a navigation bar for the browser
        navbar = QToolBar()
        #adding created navbar
        self.addToolBar(navbar)
        
        #-----------------prev Button-----------------
        #creating prev button
        prevBtn = QAction('Back 🔙 ',self)
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)

        #-----------------next Button---------------
        nextBtn = QAction('Next ⏭ ',self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)

        #-----------refresh Button--------------------
        refreshBtn = QAction('Refresh 🔃 ',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        #-----------home button----------------------
        homeBtn = QAction('Home 🏠 ',self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)
        
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.updateUrl)
    def home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    def loadUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl(url))
    def updateUrl(self, url):
        self.searchBar.setText(url.toString())
MyApp = QApplication(sys.argv)

QApplication.setApplicationName('RinnqaX')

window = Window()

MyApp.exec_()