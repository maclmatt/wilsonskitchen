from Table import Table
from constants import LOGGER


class Customers(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_customers_table(self) -> None:
        try:
            # calls recreate_table 
            # to execute sql
            sql = """CREATE TABLE Customers            
                    (CustID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Email TEXT NOT NULL UNIQUE,
                    Firstname TEXT NOT NULL,
                    Surname TEXT,              
                    Contactno TEXT NOT NULL)"""
            self.recreate_table(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Customer Table could not be reset.") from err

    def add_customer(self, email, fname, sname, contactno) -> None:
        try:
            # calls insert_record 
            # to execute sql with values
            values = (email, fname, sname, contactno)
            sql = """INSERT 
                    INTO Customers (Email, Firstname, Surname, Contactno) 
                    VALUES (?, ?, ?, ?)"""
            self.insert_record(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Customer could not be added.") from err

    def delete_customer(self, custid) -> None:
        try:
            # calls delete_record
            # to execute sql with custid
            sql = """DELETE 
                    FROM Customers 
                    WHERE CustID=?"""
            self.delete_record(sql, custid)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Customer could not be deleted.") from err

    def update_customer(self, newemail, fname, sname, contactno, oldemail) -> None:
        try:
            # calls update
            # to execute sql with values
            values = (newemail, fname, sname, contactno, oldemail)
            sql = """UPDATE Customers 
                    SET Email=?, Firstname=?, Surname=?, ContactNo=? 
                    WHERE Email=?"""
            self.update(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Customer could not be updated.") from err

    def select_custid(self, email) -> int:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with email
            # returns custid
            sql = """SELECT CustID 
                    FROM Customers 
                    WHERE Email=?"""
            data = self.select_dataspecific_fetchone(sql, (email,))
            return data
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Customer ID could not be found.") from err

    def select_customer(self, email) -> tuple:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with email
            # returns record
            sql = """SELECT * 
                    FROM Customers 
                    WHERE Email=?"""
            return self.select_dataspecific_fetchone(sql, (email,))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Customer could not be found.") from err

    def select_customers(self) -> tuple:
        try:
            # calls select
            # to execute sql
            # returns records
            sql = """SELECT * 
                    FROM Customers
                    ORDER BY CustID ASC"""
            return self.select(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Customers could not be found.") from err
