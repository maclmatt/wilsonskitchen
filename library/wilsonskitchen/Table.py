import sqlite3

class Table():
    def __init__(self, dbname, tblname):
        self.dbname = dbname
        self.tblname = tblname

    def recreate_table(self, sql):
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            cursor.execute(
                """SELECT name 
                    FROM sqlite_master 
                    WHERE name=?""", (self.tblname,))
            result = cursor.fetchall()
            if len(result) == 1:
                cursor.execute(
                    """DROP TABLE if exists {0}""".format(self.tblname))
                db.commit()
            cursor.execute(sql)
            db.commit()

    def insert_record(self, sql, values):
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            cursor.execute(sql, values)
            db.commit()

    def delete_record(self, sql, rid):  # rid must be in (x,) form
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            cursor.execute(sql, rid)
            db.commit()

    def select(self, sql):
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            return data

    # data must be in (x,) form
    def select_dataspecific_fetchone(self, sql, data):
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            cursor.execute(sql, data)
            data = cursor.fetchone()
            return data

    # data must be in (x,) form
    def select_dataspecific_fetchall(self, sql, data):
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            cursor.execute(sql, data)
            data = cursor.fetchall()
            return data

    def update(self, sql, data):
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            cursor.execute(sql, data)
            db.commit()