import sqlite3

# name_of_base = "mydatabase.db"
# conn = sqlite3.connect(name_of_base)  # name_of_base = ":memory:" чтобы сохранить в RAM
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                                        confId INT(11) NOT NULL,
#                                        name VARCHAR(50) NOT NULL,
#                                        birthdate DATE NOT NULL ,
#                                        sex VARCHAR(1) NOT NULL,
#                                        organizeCount INT(5))
#                """)
# with conn:
#     cursor.execute("""INSERT INTO clients (confId,name,birthdate,sex, organizeCount)
#                                 VALUES (1, "sDen", 19961212, "m", 0)
#                              """)
#     cursor.execute("""INSERT INTO clients (confId,name,birthdate,sex, organizeCount)
#                                     VALUES (1, "Den", 22111996, "m", 0)
#                                  """)
#
# cursor.execute("SELECT * FROM clients")
# row = cursor.fetchall()
# print(row)

class Database:
    def __init__(self, name_of_base="mydatabase.db"):
        conn = sqlite3.connect(name_of_base)  # name_of_base = ":memory:" чтобы сохранить в RAM
        self.cursor = conn.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE clients (   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                        confId INT(11) NOT NULL,
                                                        name VARCHAR(50) NOT NULL,
                                                        birthdate DATE NOT NULL ,
                                                        sex VARCHAR(1) NOT NULL,
                                                        organizeCount INT(5))
                                    """)

    def drop_table(self, name_of_table="clients"):
        self.cursor.execute("DROP TABLE clients")

    def __del__(self):
        self.cursor.close()

    def print_table(self, name_of_table="clients"):
        self.cursor.execute("SELECT * FROM clients")
        row = self.cursor.fetchall()
        print(row)

    def insert_into_table(self):
        with self.conn:
            self.cursor.execute("""INSERT INTO clients (confId,name,birthdate,sex, organizeCount)
                               VALUES (1, "sDen", 19961212, "m", 0)
                            """)
            self.cursor.execute("""INSERT INTO clients (confId,name,birthdate,sex, organizeCount)
                                   VALUES (1, "Den", 22111996, "m", 0)
                                """)


Base = Database()
# Base.create_table()
# Base.drop_table()
Base.insert_into_table()
Base.print_table()
