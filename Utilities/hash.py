import getpass
import bcrypt as B
import sqlite3 as sq

class demo:
    def __init__(self):
        print("Welcome to PassMan :-)")
        self.UserName = input("Username -  ")
        self.Password = getpass.getpass("Password - ")

        #creating a new connection to database for every new object
        self.conn = sq.connect("Details.db")
        self.cursor = self.conn.cursor()
        

    def hash(self):
        salt = B.gensalt()
        self.Password = self.Password.encode()
        self.hashed = B.hashpw(self.Password , salt)
    
    def db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Details 
                            (
                            UserName VARCHAR(15) , 
                            Password VARCHAR(30) NOT NULL
                            )''')
        
        self.cursor.execute(f"INSERT INTO Details(Username , Password)
                             VALUES({self.UserName , self.hashed})")
        
        self.conn.commit()
        
    
    def Check(self):
        self.cursor.execute(f"SELECT Password FROM Details 
                            WHERE UserName = {self.UserName}")
        password = self.cursor.fetchall()

        if B.checkpw(self.Password , password)




