import sqlite3


class SqliteHelper_req:
    def __init__(self, name=None):
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect((name))
            self.cursor = self.conn.cursor()
            print(sqlite3.version)

        except sqlite3.Error as e:
            print('Error!')

    def create_table(self):
        c = self.cursor
        c.execute("""CREATE TABLE request(id INTEGER PRIMARY KEY AUTOINCREMENT, Type TEXT NOT NULL,SubType TEXT NOT NULL,Early_Start TEXT NOT NULL,Late_Start TEXT NOT NULL,Duration TEXT NOT NULL,Target_Name TEXT NOT NULL,Right_Ascression TEXT NOT NULL,V_Magnitude TEXT NOT NULL,Target_Type TEXT NOT NULL,Decination TEXT NOT NULL,Other_Fluxes TEXT NOT NULL)""")

    def edit(self, query, updates):
        c = self.cursor
        c.execute(query, updates)
        self.conn.commit()

    def delete(self, query):
        c = self.cursor
        c.execute(query)
        self.conn.commit()

    def insert(self, query, inserts):
        c = self.cursor
        c.execute(query, inserts)
        self.conn.commit()

    def select(self, query):
        c = self.cursor
        c.execute(query)
        return c.fetchall()


test = SqliteHelper_req('test.db')
#test.create_table()
#test.edit("INSERT INTO users (name,year,admin) VALUES ('Leon',2002,0)")