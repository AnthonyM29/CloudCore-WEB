import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'cloudcore_db'
        }
        self.connection = None
    
    def connect(self):
        """Establece una conexión a la base de datos MySQL."""
        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None