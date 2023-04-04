#using sqlite database
import sqlite3
#Database class
class Db(object):
    def __init__(self):
        self.conn = sqlite3.connect("app.db") #creating the db file app.db
        self.c = self.conn.cursor()

    def createAppTable(self):
        try: #create table if it doesn't exits
            self.c.execute("""CREATE TABLE Application (
            width integer,
            height integer,
            x integer,
            y integer,
            max_win bool
            )""")
        except: #if it exists don't create
            pass

    def insertGeometry(self, width = 450, height = 600, x = 200, y = 50, max_win = False):
        self.c.execute(f"SELECT * FROM Application")
        if len(self.c.fetchall()) > 1: #update the data 
            #Fixme: find a better way to update all coumns in the table
            self.c.execute(f"UPDATE Application SET width = {width}")
            self.conn.commit()
            self.c.execute(f"UPDATE Application SET height = {height} ")
            self.conn.commit()
            self.c.execute(f"UPDATE Application SET x = {x} ")
            self.conn.commit()
            self.c.execute(f"UPDATE Application SET y = {y} ")
            self.conn.commit()
            self.c.execute(f"UPDATE Application SET max_win = {max_win} ")
            self.conn.commit()
        else:
            self.c.execute("INSERT INTO Application VALUES (:width, :height, :x, :y, :max_win)", {"width": width, "height": height, "x": x, "y": y, "max_win": max_win})   
            self.conn.commit()
        
        


    def getValues(self, filter="width"):
        self.c.execute(f"SELECT {filter} FROM Application")
        
        value = self.c.fetchone()
        if value == None:
            if filter == "width":
                value = 450
            elif filter == "height":
                value = 600
            elif filter == "x":
                value = 200
            elif filter == "y":
                value = 50
            elif filter == "max_win":
                value = False
        else:
            value = value[0]

        return value
    

      


