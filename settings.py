from os import path as os_path
from models import Db

#Get the base path of the app
CURRENT_PATH = str(os_path.dirname(os_path.realpath(__file__))).replace("\\", '/')
#init the db
INIT_DB = Db()
#create the required table
INIT_DB.createAppTable()
#THE MINIMUM SIZE OF THE APP
MIN_WIDTH, MIN_HEIGHT = 335, 500
#THE SIZE OF THE APP
WIDTH, HEIGHT = INIT_DB.getValues(filter="width"), INIT_DB.getValues(filter="height")
#The position of the ap on the screen
POS_X, POS_Y = INIT_DB.getValues(filter="x"), INIT_DB.getValues(filter="y") 
#If set true, window will be maximized
MAX_WINDOW = INIT_DB.getValues(filter="max_win")
APP_LOGO = None
#The html page that will be viewed on the Main App
HTML_PAGE = f"{CURRENT_PATH}/Calculator/templates/base.html"

