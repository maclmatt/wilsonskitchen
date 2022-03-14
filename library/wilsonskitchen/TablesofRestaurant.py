from Table import Table
from constants import LOGGER

class TablesofRestaurant(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_tables_table(self) -> None:
        try:
            # calls recreate_table 
            # to execute sql
            sql = """CREATE TABLE Tables
                    (TableID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NoSeats INTEGER)"""
            self.recreate_table(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Tables Table could not be reset.") from err

    def find_table_for_booking(self, Time, Date, nopeople) -> int:
        try:
            # checks for tables available
            # calls insert_record
            # to execute sql with values
            # returns tableid or -1 if no tables available
            booked = False
            while not booked:
                sql = """SELECT TableID 
                        FROM Tables 
                        WHERE NoSeats=?"""
                # executes sql through select_dataspecific_fetchall
                # to get all tables that have the correct number of seats
                tableids = self.select_dataspecific_fetchall(sql, (nopeople,))
                for i in range(0, len(tableids)):
                    tableid = str(tableids[i])
                    values = (tableid[1], Time, Date)
                    sql = """SELECT * 
                            FROM Bookings 
                            WHERE TableID=? AND Time=? AND Date=?"""
                    # checks if there is a booking for that date and time
                    booking = self.select_dataspecific_fetchall(sql, values)
                    if booking == []:
                        break
                if booking == []:
                    booked = True
                    return tableid[1]
                else:
                    return -1
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Table could not be found.") from err

    def add_table(self, NoSeats) -> None:
        try:
            # calls insert_record 
            # to execute sql with values
            values = (NoSeats)
            sql = """INSERT 
                    INTO Tables (NoSeats) 
                    VALUES (?)"""
            self.insert_record(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Table could not be added.") from err

    def delete_table(self, tableid) -> None:
        try:
            # calls delete_record
            # to execute sql with tableid
            sql = """DELETE 
                    FROM Tables 
                    WHERE TableID=?"""
            self.delete_record(sql, (tableid,))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Table could not be deleted.") from err

    def update_table(self, oldtableid, noseats) -> None:
        try:
            # calls update
            # to execute sql with values
            values = (noseats, oldtableid)
            sql = """UPDATE Tables 
                    SET NoSeats=?
                    WHERE TableID=?"""
            self.update(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Table could not be updated.") from err

    def print_all_tables(self) -> tuple:
        try:
            # calls select
            # to execute sql
            # returns records
            sql = """SELECT * 
                    FROM Tables 
                    ORDER BY NoSeats ASC"""
            return self.select(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Tables could not be found.") from err
