from Table import Table
from constants import LOGGER
from datetime import date, datetime


class Bookings(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_bookings_table(self) -> None:
        try:
            # calls recreate_table 
            # to execute sql
            sql = """CREATE TABLE Bookings
                    (BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Time TEXT,
                    Date TEXT,
                    NoPeople INTEGER,
                    TableID INTEGER,
                    BillTotal REAL,
                    CustID INTEGER,
                    FOREIGN KEY (TableID) REFERENCES Tables(TableID),
                    FOREIGN KEY (CustID) REFERENCES Customer(CustID))"""
            self.recreate_table(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Booking Table could not be reset.") from err

    def add_booking(self, TableID, CustID, Time, Date, NoPeople) -> None:
        try:
            # calls insert_record 
            # to execute sql with values
            BillTotal = 0.00
            values = (Time, Date, NoPeople, TableID, BillTotal, CustID)
            sql = """INSERT 
                    INTO Bookings (Time, Date, NoPeople, TableID, BillTotal, CustID) 
                    VALUES (?, ?, ?, ?, ?, ?)"""
            self.insert_record(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Booking could not be added.") from err

    def delete_booking_record(self, custid, time, date) -> None:
        try:
            # calls delete_record
            # to execute sql with values
            values = (time, date, custid)
            sql = """DELETE 
                    FROM Bookings 
                    WHERE Time=? AND Date=? AND CustID=?"""
            self.delete_record(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Booking could not be deleted.") from err

    def select_bookings_for_date(self, date) -> tuple:
        try:
            # calls select_dataspecific_fetchall
            # to execute sql with date
            # returns records
            sql = """SELECT * 
                    FROM Bookings 
                    WHERE Date=?"""
            return self.select_dataspecific_fetchall(sql, (date,))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Bookings for date could not be found.") from err

    def select_bookings_for_dateandtime(self, date, time) -> tuple:
        try:
            # calls select_dataspecific_fetchall
            # to execute sql with (date, time)
            # returns records
            sql = """SELECT * 
                    FROM Bookings 
                    WHERE Date=? AND Time=?"""
            return self.select_dataspecific_fetchall(sql, (date, time))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Bookings for date and time could not be found.") from err

    def select_booking_bill(self, tableid, time, date) -> float:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with values
            # returns bill
            values = (tableid, time, date)
            sql = """SELECT BillTotal 
                    FROM Bookings 
                    WHERE TableID=? AND Time=? AND Date=?"""
            billtuple = self.select_dataspecific_fetchone(sql, values)
            bill = billtuple[0]
            return bill
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Bill could not be found.") from err

    def select_bookings_fromtableid(self, tableid) -> tuple:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with tableid
            # returns record
            sql = """SELECT * 
                    FROM Bookings 
                    WHERE TableID=?"""
            return self.select_dataspecific_fetchone(sql, (tableid,))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Bookings for the table could not be found.") from err

    def select_bookingid(self, TableID) -> int:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with values
            # returns bookingid
            sql = """SELECT BookingID 
                    FROM Bookings 
                    WHERE TableID=? AND Time=? AND Date=?"""
            now = datetime.now()
            # gets current hou in 24 hour clock form
            current_hour = now.strftime("%H")
            today = date.today()
            values = (TableID, current_hour, today)
            bookingidtuple = self.select_dataspecific_fetchone(sql, values)
            bookingid = bookingidtuple[0]
            return bookingid
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Booking ID could not be found.") from err

    def increase_booking_billtotal(self, bookingid, ordercost) -> None:
        try:
            # increases original billtotal by ordercost
            sql = """SELECT BillTotal 
                    FROM Bookings 
                    WHERE BookingID=?"""
            # calls select_dataspecific_fetchone
            # to execute sql with bookingid
            oldbilltuple = self.select_dataspecific_fetchone(sql, (bookingid,))
            if oldbilltuple == None:
                newbill = ordercost
            else:
                oldbill = oldbilltuple[0]
                newbill = oldbill + ordercost
            sql = """UPDATE Bookings 
                    SET BillTotal=? 
                    WHERE BookingID=?"""
            # calls update
            # to execute sql with (newbill, bookingid)
            self.update(sql, (newbill, bookingid))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Bill could not be increased.") from err
