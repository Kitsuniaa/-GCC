import sqlite3


class SqliteHelper:
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
        c.execute("""CREATE TABLE userss(id INTEGER PRIMARY KEY AUTOINCREMENT, inv TEXT NOT NULL,username TEXT NOT NULL,Honorific TEXT NOT NULL,First_Name TEXT NOT NULL,Middle_name TEXT NOT NULL,Last_Name TEXT NOT NULL,Organisation TEXT NOT NULL,Adress TEXT NOT NULL,Country TEXT NOT NULL,Phone_Num TEXT NOT NULL,Fax_Num TEXT NOT NULL,Email TEXT NOT NULL,Login TEXT NOT NULL,Password TEXT NOT NULL)""")

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


test = SqliteHelper('testik.db')
#test.create_table()

# test.edit("INSERT INTO users (name,year,admin) VALUES ('Leon',2002,0)")
#test.edit("DELETE FROM userss")
# print(test.select("SELECT * fROM users"))
