#import external libs
#import python default

from sys import argv, exit
from os import path as os_path
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtWidgets import (QMainWindow, QApplication)
from webview import WebPage
#import settings
from settings import MIN_HEIGHT, MIN_WIDTH, APP_LOGO, HTML_PAGE, POS_X, POS_Y, INIT_DB, WIDTH, HEIGHT, MAX_WINDOW


#the main class
class Main(WebPage):
    current_win_pos = QPoint(MIN_WIDTH, MIN_HEIGHT) #This will be used to update the current windows position on the screen
    current_win_size = QSize(MIN_WIDTH, MIN_HEIGHT) #This will be used to update the current windows size on the screen
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #set title
        self.setWindowTitle("Calculator")
        #set the size
        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)
        self.setGeometry(POS_X, POS_Y, WIDTH, HEIGHT)
        #if max_win is true maximize window
        if MAX_WINDOW:
            self.showMaximized()
        #set the icon
        self.setWindowIcon(QIcon(APP_LOGO))
        
        #initialize the Main App
        self.initUI()

    def initUI(self):
        self.addWeb()
        self.addUrl(HTML_PAGE)


    def resizeEvent(self, e):
        x, y = self.current_win_pos.x(), self.current_win_pos.y()
        #if max_win is true, dont add current size to the db
        if MAX_WINDOW:
            width, height = self.current_win_size.width(), self.current_win_size.height()
            #add the size of the app to the db
            INIT_DB.insertGeometry(width = width , height = height, x = x, y = y, max_win = self.isMaximized())
        else:
            self.current_win_size = e.size()
            width, height = self.current_win_size.width(), self.current_win_size.height()
            #add the size of the app to the db
            INIT_DB.insertGeometry(width = width , height = height, x = x, y = y, max_win = self.isMaximized())

    def moveEvent(self, e):
        self.current_win_pos = e.pos()
        x, y = self.current_win_pos.x(), self.current_win_pos.y()

        width, height = self.current_win_size.width(), self.current_win_size.height()
        #add the position of the app to the db
        INIT_DB.insertGeometry(x = x, y = y, width = width, height = height, max_win = self.isMaximized())

    def closeEvent(self, a):
        x, y = self.current_win_pos.x(), self.current_win_pos.y()

        width, height = self.current_win_size.width(), self.current_win_size.height()
        #add the position of the app to the db
        INIT_DB.insertGeometry(x = x, y = y, width = width, height = height, max_win = self.isMaximized())

  

   



def run_code():
    app = QApplication(argv)
    window = Main()
    window.setWindowIcon(QIcon("app_icon.png"))
    window.show()
    
    exit(app.exec_())

#launch the app
run_code()

