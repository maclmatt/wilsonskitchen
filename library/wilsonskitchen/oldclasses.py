from ast import Index, Tuple
from multiprocessing.dummy import Value
import sqlite3
from datetime import date, datetime
from constants import LOGGER


class List(): # transferred
    def __init__(self):
        self._list = []
        self.length = 0

    def add_item(self, item) -> None:
        try:
            list = self._list
            list.append(item)
            self.length += 1
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Item could not be added to list.") from err

    def sort_switch(self, numbers, low, high) -> Index:
        try:
            pivot = numbers[high]
            item = low - 1
            for i in range(low, high):
                if numbers[i] <= pivot:
                    item = item + 1
                    (numbers[item], numbers[i]) = (numbers[i], numbers[item])
            (numbers[item + 1], numbers[high]) = (numbers[high], numbers[item + 1])
            return item + 1
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Switch of items could not be performed.") from err

    def quick_sort(self, numbers, low, high) -> None:
        try:
            if low < high:
                pivot = self.list_sort_switch(numbers, low, high)
                self.list_quick_sort(numbers, low, pivot-1)
                self.list_quick_sort(numbers, pivot + 1, high)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("List could not be sorted using quick sort.") from err

    def sort_list(self) -> None:
        try:
            self.list_quick_sort(self._list, 0, (self.length)-1)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("List could not be sorted.") from err

    def return_list(self) -> list:
        try:
            return self._list
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("List could not be returned.") from err

    def return_lowest(self) -> Value:
        try:
            self.sort_list()
            return self._list[0]
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Lowest list item could not be returned.") from err

    def wipe(self) -> None:
        try:
            self._list = []
            self.length = 0
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("List could not be wiped.") from err


class Table(): # transferred
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


class Customers(Table): # transferred
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_customers_table(self) -> None:
        try:
            sql = """CREATE TABLE Customers            
                    (CustID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Email TEXT NOT NULL UNIQUE,
                    Firstname TEXT NOT NULL,
                    Surname TEXT,              
                    Contactno TEXT NOT NULL)"""
            self.recreate_table(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Customer Table could not be reset.") from err

    def add_customer(self, email, fname, sname, contactno) -> None:
        try:
            values = (email, fname, sname, contactno)
            sql = """INSERT 
                    INTO Customers (Email, Firstname, Surname, Contactno) 
                    VALUES (?, ?, ?, ?)"""
            self.insert_record(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Customer could not be added.") from err

    def delete_customer(self, custid) -> None:
        try:
            sql = """DELETE 
                    FROM Customers 
                    WHERE CustID=?"""
            self.delete_record(sql, custid)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Customer could not be deleted.") from err

    def update_customer(self, newemail, fname, sname, contactno, oldemail) -> None:
        try:
            values = (newemail, fname, sname, contactno, oldemail)
            sql = """UPDATE Customers 
                    SET Email=?, Firstname=?, Surname=?, ContactNo=? 
                    WHERE Email=?"""
            self.update(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Customer could not be updated.") from err

    def select_custid(self, email) -> int:
        try:
            sql = """SELECT CustID 
                    FROM Customers 
                    WHERE Email=?"""
            data = self.select_dataspecific_fetchone(sql, (email,))
            return data
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Customer ID could not be found.") from err

    def select_customer(self, email) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Customers 
                    WHERE Email=?"""
            return self.select_dataspecific_fetchone(sql, (email,))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Customer could not be found.") from err

    def select_customers(self) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Customers
                    ORDER BY Firstname ASC"""
            return self.select(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Customers could not be found.") from err


class Bookings(Table): # transferred
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_bookings_table(self) -> None:
        try:
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
            LOGGER.error(err)
            raise RuntimeError("Booking Table could not be reset.") from err

    def add_booking(self, TableID, CustID, Time, Date, NoPeople) -> None:
        try:
            BillTotal = 0.00
            values = (Time, Date, NoPeople, TableID, BillTotal, CustID)
            sql = """INSERT 
                    INTO Bookings (Time, Date, NoPeople, TableID, BillTotal, CustID) 
                    VALUES (?, ?, ?, ?, ?, ?)"""
            self.insert_record(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Booking could not be added.") from err

    def delete_booking_record(self, custid, time, date) -> None:
        try:
            values = (time, date, custid)
            sql = """DELETE 
                    FROM Bookings 
                    WHERE Time=? AND Date=? AND CustID=?"""
            self.delete_record(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Booking could not be deleted.") from err

    def select_bookings_for_date(self, date) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Bookings 
                    WHERE Date=?"""
            return self.select_dataspecific_fetchall(sql, (date,))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Bookings for date could not be found.") from err

    def select_bookings_for_dateandtime(self, date, time) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Bookings 
                    WHERE Date=? AND Time=?"""
            return self.select_dataspecific_fetchall(sql, (date, time))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Bookings for date and time could not be found.") from err

    def select_booking_bill(self, tableid, time, date) -> float:
        try:
            values = (tableid, time, date)
            sql = """SELECT BillTotal 
                    FROM Bookings 
                    WHERE TableID=? AND Time=? AND Date=?"""
            billtuple = self.select_dataspecific_fetchone(sql, values)
            bill = billtuple[0]
            return bill
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Bill could not be found.") from err

    def select_bookings_fromtableid(self, tableid) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Bookings 
                    WHERE TableID=?"""
            return self.select_dataspecific_fetchone(sql, (tableid,))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Bookings for the table could not be found.") from err

    def select_bookingid(self, TableID) -> int:
        try:
            sql = """SELECT BookingID 
                    FROM Bookings 
                    WHERE TableID=? AND Time=? AND Date=?"""
            now = datetime.now()
            current_hour = now.strftime("%H")
            today = date.today()
            values = (TableID, current_hour, today)
            bookingidtuple = self.select_dataspecific_fetchone(sql, values)
            bookingid = bookingidtuple[0]
            return bookingid
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Booking ID could not be found.") from err

    def increase_booking_billtotal(self, bookingid, ordercost) -> None:
        try:
            sql = """SELECT BillTotal 
                    FROM Bookings 
                    WHERE BookingID=?"""
            oldbilltuple = self.select_dataspecific_fetchone(sql, (bookingid,))
            if oldbilltuple == None:
                newbill = ordercost
            else:
                oldbill = oldbilltuple[0]
                newbill = oldbill + ordercost
            sql = """UPDATE Bookings 
                    SET BillTotal=? 
                    WHERE BookingID=?"""
            self.update(sql, (newbill, bookingid))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Bill could not be increased.") from err


class TablesofRestaurant(Table): # transferred
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


class Orders(Table): # transferred
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

class OrderProducts(Table): # transferred
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_orderproducts_table(self) -> None:
        try:
            sql = """CREATE TABLE OrderProducts
                    (OrderProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ProductID INTEGER,
                    Quantity INTEGER,
                    OrderID INTEGER,
                    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
                    FOREIGN KEY (OrderID) REFERENCES OrderTable(OrderID))"""
            self.recreate_table(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Orderproducts table could not be reset.") from err

    def add_orderproduct(self, OrderID, ProductID, quantity) -> None:
        try:
            sql = """INSERT 
                    INTO OrderProducts (ProductID, Quantity, OrderID) 
                    VALUES (?, ?, ?)"""
            self.insert_record(sql, (ProductID, quantity, OrderID))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Orderproduct could not be added.") from err


class Products(Table): # transferred
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_products_table(self) -> None:
        try:
            sql = """CREATE TABLE Products
                    (ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Type TEXT,
                    Name TEXT,
                    Price REAL,
                    QuantityAvailable INTEGER,
                    CostPerPortion FLOAT)"""
            self.recreate_table(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Product table could not be reset.") from err

    def add_product(self, type, name, price) -> int:
        try:
            quantity = 0
            cost = 0.0
            values = (type, name, price, quantity, cost)
            sql = """INSERT 
                    INTO Products (Type, Name, Price, QuantityAvailable, CostPerPortion) 
                    VALUES (?, ?, ?, ?, ?)"""
            self.insert_record(sql, values)
            sql = """SELECT ProductID 
                    FROM Products 
                    WHERE Name=? AND Price=?"""
            idtuple = self.select_dataspecific_fetchone(sql, (name, price))
            id = idtuple[0]
            return id
        except BaseException as err:
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
            LOGGER.error(err)
            raise RuntimeError("Product cost could not be increased.") from err

    def delete_product(self, productid) -> None:
        try:
            sql = """DELETE 
                    FROM Products 
                    WHERE ProductID=?"""
            self.delete_record(sql, (productid,))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Product could not be deleted.") from err

    def return_products(self) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Products 
                    ORDER BY Type ASC"""
            products = self.select(sql)
            return products
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Products could not be found.") from err

    def print_menu(self) -> list:
        try:
            sql = """SELECT * 
                    FROM Products 
                    WHERE Type=?"""
            starters = self.select_dataspecific_fetchall(sql, ("Starter",))
            mains = self.select_dataspecific_fetchall(sql, ("Main",))
            sides = self.select_dataspecific_fetchall(sql, ("Side",))
            desserts = self.select_dataspecific_fetchall(sql, ("Dessert",))
            return [starters, mains, sides, desserts]
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Products could not be found.") from err

    def select_productid(self, name) -> int:
        try:
            sql = """SELECT ProductID 
                    FROM Products 
                    WHERE Name=?"""
            prodidtuple = self.select_dataspecific_fetchone(sql, (name,))
            prodid = prodidtuple[0]
            return prodid
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Product ID could not be found.") from err

    def check_quantity_availability(self, quantity, productid) -> bool:
        try:
            sql = """SELECT QuantityAvailable 
                    FROM Products 
                    WHERE ProductID=?"""
            availabletuple = self.select_dataspecific_fetchone(sql, (productid,))
            available = availabletuple[0]
            if available < quantity:
                return False
            else:
                return True
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Quantity Available could not be checked.") from err

    def get_product_price(self, productid) -> int:
        try:
            sql = """SELECT Price 
                    FROM Products 
                    WHERE ProductID=?"""
            price = self.select_dataspecific_fetchone(sql, (productid,))[0]
            return price
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Product price could not be found.") from err

    def add_product_quantity(self, quantity, productid) -> None:
        try:
            sql = """UPDATE Products 
                    SET QuantityAvailable=? 
                    WHERE ProductID=?"""
            values = (quantity, productid)
            self.update(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Product could not be updated.") from err


class Uses(Table): # transferred
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_uses_table(self) -> None:
        try:
            sql = """CREATE TABLE Uses
                    (UseID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ProductID INTEGER,
                    IngredientID INTEGER,
                    QuantityInKilos REAL,
                    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
                    FOREIGN KEY (IngredientID) REFERENCES Ingredient(IngredientID))"""
            self.recreate_table(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Uses table could not be reset.") from err

    def add_use(self, ProductID, IngredientID, Quantity) -> None:
        try:
            sql = """INSERT 
                    INTO Uses (ProductID, IngredientID, QuantityInKilos) 
                    VALUES (?, ?, ?)"""
            self.insert_record(sql, (ProductID, IngredientID, Quantity))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Use of ingredient could not be added.") from err

    def delete_use(self, productid) -> None:
        try:
            sql = """DELETE 
                    FROM Uses 
                    WHERE ProductID=?"""
            self.delete_record(sql, (productid,))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Use of ingredient could not be deleted.") from err

    def select_uses_forproduct(self, productid) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Uses 
                    WHERE ProductID=?"""
            uses = self.select_dataspecific_fetchall(sql, (productid,))
            return uses
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Use of ingredient for the product could not be found.") from err

    def select_use_quantity(self, useid) -> float:
        try:
            sql = """SELECT QuantityInKilos 
                    FROM Uses 
                    WHERE UseID=?"""
            quantitytuple = self.select_dataspecific_fetchone(sql, (useid,))
            quantity = quantitytuple[0]
            return quantity
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Use of ingredient quantity could not be found.") from err

    def select_uses_from_ingid(self, ingid) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Uses 
                    WHERE IngredientID=?"""
            uses = self.select_dataspecific_fetchall(sql, (ingid,))
            return uses
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Uses of ingredient could not be found.") from err


class Ingredients(Table): # transferred
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_ingredients_table(self) -> None:
        try:
            sql = """CREATE TABLE Ingredients
                    (IngredientID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Type TEXT,
                    StoragePlace TEXT,
                    CostPerKilo REAL,
                    StockInKilos REAL)"""
            self.recreate_table(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredient table could not be reset.") from err

    def add_ingredient(self, Name, Type, StoragePlace, CostPerKilo, StockInKilos) -> None:
        try:
            values = (Name, Type, StoragePlace, CostPerKilo, StockInKilos)
            sql = """INSERT 
                    INTO Ingredients (Name, Type, StoragePlace, CostPerKilo, StockInKilos) 
                    VALUES (?, ?, ?, ?, ?)"""
            self.insert_record(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredient could not be added.") from err

    def delete_ingredient(self, ingid) -> None:
        try:
            sql = """DELETE 
                    FROM Ingredients 
                    WHERE IngredientID=?"""
            self.delete_record(sql, (ingid,))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredient could not be deleted.") from err

    def reduce_ingredient_stock(self, ingredientid, quantity) -> None:
        try:
            sql = """SELECT StockInKilos 
                    FROM Ingredients 
                    WHERE IngredientID=?"""
            oldstocktuple = self.select_dataspecific_fetchone(sql, (ingredientid,))
            oldstock = oldstocktuple[0]
            newstock = oldstock - quantity
            values = (newstock, ingredientid)
            sql = """UPDATE Ingredients 
                    SET StockInKilos=? 
                    WHERE IngredientID=?"""
            self.update(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredient stock could not be reduced.") from err

    def increase_ingredient_stock(self, ingredientid, quantity) -> None:
        try:
            sql = """SELECT StockInKilos 
                    FROM Ingredients 
                    WHERE IngredientID=?"""
            oldstocktuple = self.select_dataspecific_fetchone(sql, (ingredientid,))
            oldstock = oldstocktuple[0]
            newstock = oldstock + quantity
            values = (newstock, ingredientid)
            sql = """UPDATE Ingredients 
                    SET StockInKilos=? 
                    WHERE IngredientID=?"""
            self.update(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredient stock could not be increased.") from err

    def select_ingredient_stock(self, ingredientid) -> float:
        try:
            sql = """SELECT StockInKilos 
                    FROM Ingredients 
                    WHERE IngredientID=?"""
            stocktuple = self.select_dataspecific_fetchone(sql, (ingredientid,))
            stock = stocktuple[0]
            return stock
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredient stock could not be found.") from err

    def select_ingredientid(self, name) -> Tuple:
        try:
            sql = """SELECT IngredientID 
                    FROM Ingredients 
                    WHERE Name=?"""
            idtuple = self.select_dataspecific_fetchone(sql, (name,))
            return idtuple
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredient ID could not be found.") from err

    def select_cost(self, ingid) -> float:
        try:
            sql = """SELECT CostPerKilo 
                    FROM Ingredients 
                    WHERE IngredientID=?"""
            costtuple = self.select_dataspecific_fetchone(sql, (ingid,))
            cost = costtuple[0]
            return cost
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredient cost could not be found.") from err

    def update_ingredient(self, name, newtype, newstorageplace, newcost) -> None:
        try:
            values = (newtype, newstorageplace, newcost, name)
            sql = """UPDATE Ingredients 
                    SET Type=?, StoragePlace=?, CostPerKilo=? 
                    WHERE Name=?"""
            self.update(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredient could not be updated.") from err

    def select_ingredients(self) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM Ingredients"""
            return self.select(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredients could not be found.") from err


class IngredientBatches(Table): # transferred
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_ingredientbatch_table(self) -> None:
        try:
            sql = """CREATE TABLE IngredientBatches
                    (IngredientBatchID INTEGER PRIMARY KEY AUTOINCREMENT,
                    IngredientID INTEGER,
                    Quantity REAL,
                    ExpiryDate TEXT,
                    FOREIGN KEY (IngredientID) REFERENCES Ingredient(IngredientID))"""
            self.recreate_table(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredientbatches table could not be reset.") from err

    def add_ingredientbatch(self, IngredientID, Quantity, ExpiryDate) -> None:
        try:
            sql = """INSERT 
                    INTO IngredientBatches (IngredientID, Quantity, ExpiryDate) 
                    VALUES (?, ?, ?)"""
            self.insert_record(sql, (IngredientID, Quantity, ExpiryDate))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredientbatch could not be added.") from err

    def delete_batch(self, ingid, expirydate) -> None:
        try:
            sql = """DELETE 
                    FROM IngredientBatches 
                    WHERE IngredientID=? AND ExpiryDate=?"""
            self.delete_record(sql, (ingid, expirydate))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredientbatch could not be deleted.") from err

    def select_quantity(self, ingid, expirydate) -> Tuple:
        try:
            values = (ingid, expirydate)
            sql = """SELECT Quantity 
                    FROM IngredientBatches 
                    WHERE IngredientID=? AND ExpiryDate=?"""
            return self.select_dataspecific_fetchone(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredientbatch quantity could not be found.") from err

    def select_batches(self) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM IngredientBatches"""
            return self.select(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Ingredientbatches could not be found.") from err


class StaffMembers(Table): # transferred
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self._username = 1111

    def reset_staffmembers_table(self) -> None:
        try:
            sql = """CREATE TABLE StaffMembers
                    (StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Email TEXT,
                    Firstname TEXT,
                    Surname TEXT,
                    JobTitle TEXT,
                    AccessLevel INTEGER,
                    Username INTEGER,
                    Password)"""
            self.recreate_table(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("StaffMembers table could not be reset.") from err

    def add_member(self, email, fname, sname, job, accesslevel, password) -> int:
        try:
            staffmembers = self.get_staffmembers()
            if staffmembers == []:
                username = self._username
            else:
                prevusername = staffmembers[len(staffmembers)-1][6]
                username = prevusername + 1
            values = (email, fname, sname, job, accesslevel, username, password)
            sql = """INSERT 
                    INTO StaffMembers 
                    (Email, Firstname, Surname, JobTitle, AccessLevel, Username, Password) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)"""
            self.insert_record(sql, values)
            return username
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Staff member could not be added.") from err

    def get_staffmembers(self) -> Tuple:
        try:
            sql = """SELECT * 
                    FROM StaffMembers"""
            return self.select(sql)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Staff members could not be found.") from err

    def delete_member(self, email) -> None:
        try: 
            sql = """DELETE 
                    FROM StaffMembers 
                    WHERE Email=?"""
            self.delete_record(sql, (email,))
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Staff member could not be deleted.") from err

    def update_ownaccount(self, username, email, fname, sname, password) -> None:
        try:
            values = (email, fname, sname, password, username)
            sql = """UPDATE StaffMembers 
                    SET Email=?, Firstname=?, Surname=?, Password=? 
                    WHERE Username=?"""
            self.update(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Staff member could not be updated.") from err

    def update_member(self, oldemail, email, fname, sname, job, access, password) -> None:
        try:
            values = (email, fname, sname, job, access, password, oldemail)
            sql = """UPDATE StaffMembers 
                    SET Email=?, Firstname=?, Surname=?, JobTitle=?, AccessLevel=?, Password=? 
                    WHERE Email=?"""
            self.update(sql, values)
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Staff member could not be updated.") from err

    def check_login(self, username, password) -> list:
        try:
            values = (username, password)
            sql = """SELECT AccessLevel 
                    FROM StaffMembers 
                    WHERE Username=? AND Password=?"""
            accesstuple = self.select_dataspecific_fetchone(sql, values)
            if accesstuple == None:
                sql = """SELECT Password 
                        FROM StaffMembers 
                        WHERE Username=?"""
                passwordtuple = self.select_dataspecific_fetchone(sql, (username,))
                if passwordtuple == None:
                    return [False, "neither"]
                else:
                    password = passwordtuple[0]
                    return [False, password]
            else:
                access = accesstuple[0]
                return [True, access]
        except BaseException as err:
            LOGGER.error(err)
            raise RuntimeError("Staff member login could not be checked.") from err
