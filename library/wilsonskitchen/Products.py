from Table import Table
from constants import LOGGER


class Products(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_products_table(self) -> None:
        try:
            # calls recreate_table 
            # to execute sql
            sql = """CREATE TABLE Products
                    (ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Type TEXT,
                    Name TEXT,
                    Price REAL,
                    QuantityAvailable INTEGER,
                    CostPerPortion FLOAT)"""
            self.recreate_table(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Product table could not be reset.") from err

    def add_product(self, type, name, price) -> int:
        try:
            # calls insert_record 
            # to execute sql1 with values
            # calls select_dataspecific_fetchone
            # to execute sql2 with (name, price)
            # returns productid
            quantity = 0
            cost = 0.0
            values = (type, name, price, quantity, cost)
            sql1 = """INSERT 
                    INTO Products (Type, Name, Price, QuantityAvailable, CostPerPortion) 
                    VALUES (?, ?, ?, ?, ?)"""
            self.insert_record(sql1, values)
            sql2 = """SELECT ProductID 
                    FROM Products 
                    WHERE Name=? AND Price=?"""
            idtuple = self.select_dataspecific_fetchone(sql2, (name, price))
            id = idtuple[0]
            return id
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Product could not be added.") from err

    def increase_cost(self, productid, cost) -> None:
        try:
            sql = """SELECT CostPerPortion 
                    FROM Products 
                    WHERE ProductID=?"""
            oldcosttuple = self.select_dataspecific_fetchone(sql, (productid,))
            oldcost = oldcosttuple[0]
            newcost = oldcost + cost
            values = (newcost, productid)
            sql = """UPDATE Products 
                    SET CostPerPortion=? 
                    WHERE ProductID=?"""
            self.update(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Product cost could not be increased.") from err

    def delete_product(self, productid) -> None:
        try:
            # calls delete_record
            # to execute sql with productid
            sql = """DELETE 
                    FROM Products 
                    WHERE ProductID=?"""
            self.delete_record(sql, (productid,))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Product could not be deleted.") from err

    def return_products(self) -> tuple:
        try:
            # calls select
            # to execute sql
            # returns records
            sql = """SELECT * 
                    FROM Products 
                    ORDER BY Type ASC"""
            products = self.select(sql)
            return products
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Products could not be found.") from err

    def print_menu(self) -> list:
        try:
            # calls select_dataspecific_fetchall
            # to execute sql with each kind of product:
                # Starter, Main, Side, Dessert
            # returns records
            sql = """SELECT * 
                    FROM Products 
                    WHERE Type=?"""
            starters = self.select_dataspecific_fetchall(sql, ("Starter",))
            mains = self.select_dataspecific_fetchall(sql, ("Main",))
            sides = self.select_dataspecific_fetchall(sql, ("Side",))
            desserts = self.select_dataspecific_fetchall(sql, ("Dessert",))
            return [starters, mains, sides, desserts]
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Products could not be found.") from err

    def select_productid(self, name) -> int:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with name
            # returns prodid
            sql = """SELECT ProductID 
                    FROM Products 
                    WHERE Name=?"""
            prodidtuple = self.select_dataspecific_fetchone(sql, (name,))
            prodid = prodidtuple[0]
            return prodid
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Product ID could not be found.") from err

    def check_quantity_availability(self, quantity, productid) -> bool:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with productid
            sql = """SELECT QuantityAvailable 
                    FROM Products 
                    WHERE ProductID=?"""
            availabletuple = self.select_dataspecific_fetchone(sql, (productid,))
            available = availabletuple[0]
            # returns whether the:
            # quantity required is >= to the quantity available or not
            if available < quantity:
                return False
            else:
                return True
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Quantity Available could not be checked.") from err

    def get_product_price(self, productid) -> int:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with productid
            # returns price
            sql = """SELECT Price 
                    FROM Products 
                    WHERE ProductID=?"""
            price = self.select_dataspecific_fetchone(sql, (productid,))[0]
            return price
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Product price could not be found.") from err

    def add_product_quantity(self, quantity, productid) -> None:
        try:
            # calls update
            # to execute sql with (quantity, productid)
            sql = """UPDATE Products 
                    SET QuantityAvailable=? 
                    WHERE ProductID=?"""
            values = (quantity, productid)
            self.update(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Product could not be updated.") from err
