from Table import Table
from constants import LOGGER
from ast import Tuple

class TablesofRestaurant(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_tables_table(self) -> None:
        try:
            sql = """CREATE TABLE Tables
                    (TableID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NoSeats INTEGER,
                    Description TEXT)"""
            self.recreate_table(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Tables Table could not be reset.") from err

    def find_table_for_booking(self, Time, Date, nopeople) -> int:
        try:
            booked = False
            while not booked:
                sql = """SELECT TableID 
                        FROM Tables 
                        WHERE NoSeats=?"""
                tableids = self.select_dataspecific_fetchall(sql, (nopeople,))
                for i in range(0, len(tableids)):
                    tableid = str(tableids[i])
                    values = (tableid[1], Time, Date)
                    sql = """SELECT * 
                            FROM Bookings 
                            WHERE TableID=? AND Time=? AND Date=?"""
                    booking = self.select_dataspecific_fetchall(sql, values)
                    if booking == []:
                        break
                if booking == []:
                    booked = True
                    return tableid[1]
                else:
                    return -1
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Table could not be found.") from err

    def add_table(self, NoSeats, Description) -> None:
        try:
            values = (NoSeats, Description)
            sql = """INSERT 
                    INTO Tables (NoSeats, Description) 
                    VALUES (?, ?)"""
            self.insert_record(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Table could not be added.") from err

    def delete_table(self, tableid) -> None:
        try:
            sql = """DELETE 
                    FROM Tables 
                    WHERE TableID=?"""
            self.delete_record(sql, (tableid,))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Table could not be deleted.") from err

    def update_table(self, oldtableid, noseats, description) -> None:
        try:
            values = (noseats, description, oldtableid)
            sql = """UPDATE Tables 
                    SET NoSeats=?, Description=? 
                    WHERE TableID=?"""
            self.update(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Table could not be updated.") from err

    def print_all_tables(self) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Tables 
                    ORDER BY NoSeats ASC"""
            return self.select(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Tables could not be found.") from err
