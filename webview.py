#Import all the necessary modules for using html page on python ap
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import  QVBoxLayout, QWidget

class WebPage(QWidget):

    def __init__(self):
        super().__init__() 
        
    def addWeb(self):
        #add the layout view
        self.lay = QVBoxLayout()
        self.lay.setContentsMargins(0,0,0,0)
        self.setLayout(self.lay)
        #make a browser
        self.browser = QWebEngineView()
        self.browser.setAcceptDrops(False)
        self.lay.addWidget(self.browser)  
        
    def addUrl(self, url):
        self.browser.setUrl(QUrl(url))
      
    
