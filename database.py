import sqlite3
import datetime


class Database:
    conn = sqlite3.connect("mydatabase.db")  # :memory: чтобы сохранить в RAM

    def __init__(self):
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                     confId INT(11) NOT NULL,
                                                     name VARCHAR(50) NOT NULL,
                                                     birth_date DATE NOT NULL ,
                                                     sex VARCHAR(1) NOT NULL,
                                                     orgCount INT(5))
                            """)

    def __drop_table(self, name_of_table):
        sql_request = "DROP TABLE " + name_of_table
        self.cursor.execute(sql_request)

    def recreate_table(self, name_of_table):
        sql_request = "DROP TABLE " + name_of_table
        self.cursor.execute(sql_request)
        self.cursor.execute("""CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                             confId INT(11) NOT NULL,
                                                             name VARCHAR(50) NOT NULL,
                                                             birth_date DATA NOT NULL ,
                                                             sex VARCHAR(1) NOT NULL,
                                                             orgCount INT(5))
                                    """)

    def clear_table(self, name_of_table):
        with self.conn:
            sql_requst = "DELETE FROM " + name_of_table
            self.cursor.execute(sql_requst)

    def __del__(self):
        self.cursor.close()

    def print_table(self, name="clients"):
        sql = "SELECT * FROM "
        sql_request = sql + name
        self.cursor.execute(sql_request)
        row = self.cursor.fetchall()
        print(row)

    def insert_into_table(self, data=['0', 'test', '1996-12-12', 'm', '0']):
        with self.conn:
            self.cursor.execute("""INSERT INTO clients (confId, name, birth_date, sex, orgCount)
                                                VALUES (?,?,?,?,?) """, data)

    def make_request(self, sql_request=None):
        self.cursor.execute(sql_request)
        row = self.cursor.fetchall()
        print(row)

    def find_celebrant(self):
        now = datetime.date.today()
        period = datetime.timedelta(days=7)
        checking_date = now + period
        now_date = "'" + str(now) + "'"
        need_date = "'" + str(checking_date) + "'"
        sql_request = """SELECT id,name,sex,birth_date FROM clients
                         WHERE strftime('%m-%d',birth_date) BETWEEN
                         strftime('%m-%d', """ + now_date + ") AND strftime('%m-%d'," + need_date + ")"
        self.cursor.execute(sql_request)
        row = self.cursor.fetchall()
        print(row)

    def extra_find_celebrant(self):
        now = datetime.date.today()
        row = []
        for n in range(8):
            period = datetime.timedelta(days=n)
            checking_date = now + period
            checking_day = str(checking_date)[5:]
            need_date = "'%" + checking_day + "'"
            print(need_date)
            sql_request = "SELECT id,name,sex FROM clients WHERE birth_date LIKE " + need_date
            self.cursor.execute(sql_request)
            row += self.cursor.fetchall()
        print(row)


# Base = Database()
# Base.recreate_table("clients")
# Base.insert_into_table(['0', 'test', '2017-11-09', 'm', '0'])
# Base.print_table()
# Base.find_celebrant()
# Base.extra_find_celebrant_v2()
