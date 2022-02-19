from Table import Table
from constants import LOGGER
from ast import Tuple
from datetime import date, datetime

class Orders(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_orders_table(self) -> None:
        try:
            sql = """CREATE TABLE Orders
                    (OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Date TEXT,
                    Time TEXT,
                    TotalPrice REAL,
                    TableID INTEGER,
                    FOREIGN KEY (TableID) REFERENCES Tables(TableID))"""
            self.recreate_table(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Orders table could not be reset.") from err

    def add_order(self, TableID) -> int:
        try:
            TotalPrice = 0.00
            today = date.today()
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            values = (today, time, TotalPrice, TableID)
            sql = """INSERT 
                    INTO Orders (Date, Time, TotalPrice, TableID) 
                    VALUES (?, ?, ?, ?)"""
            self.insert_record(sql, values)
            sql = """SELECT OrderID 
                    FROM Orders 
                    WHERE Date=? AND Time=? AND TotalPrice=? AND TableID=?"""
            orderidtuple = self.select_dataspecific_fetchone(sql, values)
            orderid = orderidtuple[0]
            return orderid
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Order could not be added.") from err

    def delete_order(self, orderid) -> None:
        try:
            sql = """DELETE 
                    FROM Orders 
                    WHERE OrderID=?"""
            self.delete_record(sql, (orderid,))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Order could not be deleted.") from err

    def add_orderproduct_price(self, orderid, price) -> None:
        try:
            sql = """SELECT TotalPrice 
                    FROM Orders 
                    WHERE OrderID=?"""
            oldpricetuple = self.select_dataspecific_fetchone(sql, (orderid,))
            oldprice = oldpricetuple[0]
            newprice = oldprice + price
            sql = """UPDATE Orders 
                    SET TotalPrice=? 
                    WHERE OrderID=?"""
            self.update(sql, (newprice, orderid))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Order could not be updated.") from err

    def get_order_totalprice(self, orderid) -> float:
        try:
            sql = """SELECT TotalPrice 
                    FROM Orders 
                    WHERE OrderID=?"""
            pricetuple = self.select_dataspecific_fetchone(sql, (orderid,))
            price = pricetuple[0]
            return price
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Order total price could not be found.") from err

    def select_orders_for_table(self, tableid) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Orders 
                    WHERE TableID=?"""
            orders = self.select_dataspecific_fetchall(sql, (tableid,))
            return orders
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Orders for table could not be found.") from err

    def select_orders_for_date(self, date) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Orders 
                    WHERE Date=?"""
            orders = self.select_dataspecific_fetchall(sql, (date,))
            return orders
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Orders for date could not be found.") from err
