import sqlite3
from datetime import date, datetime

class List():
    def __init__(self):
        self._list = []
        self.length = 0

    def add_item(self, item):
        list = self.list
        list.append(item)
        self.length += 1

    def switch(self, numbers, low, high):
        pivot = numbers[high]
        item = low - 1
        for i in range(low, high):
            if numbers[i] <= pivot:
                item = item + 1
                (numbers[item], numbers[i]) = (numbers[i], numbers[item])
        (numbers[item + 1], numbers[high]) = (numbers[high], numbers[item + 1])
        return item + 1

    def quick_sort(self, numbers, low, high):
        if low < high:
            pivot = self.switch(numbers, low, high)
            self.quick_sort(numbers, low, pivot-1)
            self.quick_sort(numbers, pivot + 1, high)

    def sort_list(self):
        self.quick_sort(self.list, 0, (self.length)-1)

    def return_list(self):
        return self.list

    def return_lowest(self):
        self.sort_list()
        return self.list[0]


class Table():
    def __init__(self, dbname, tblname):
        self.dbname = dbname
        self.tblname = tblname

    def recreate_table(self, sql):
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE name=?", (self.tblname,))
            result = cursor.fetchall()
            if len(result) == 1:
                    cursor.execute("DROP TABLE if exists {0}".format(self.tblname))
                    db.commit()
            cursor.execute(sql)
            db.commit()

    def insert_record(self, sql, values):
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            cursor.execute(sql, values)
            db.commit()

    def delete_record(self, sql, rid): #rid must be in (x,) form
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
    
    def select_dataspecific_fetchone(self, sql, data): #data must be in (x,) form
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            cursor.execute(sql, data)
            data = cursor.fetchone()
            return data

    def select_dataspecific_fetchall(self, sql, data): #data must be in (x,) form
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


class Customers(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self.reset_customers_table()

    def reset_customers_table(self):
        sql = """CREATE TABLE Customers            
                (CustID INTEGER PRIMARY KEY AUTOINCREMENT,
                Email TEXT NOT NULL UNIQUE,
                Firstname TEXT NOT NULL,
                Surname TEXT,              
                Contactno TEXT NOT NULL)"""
        self.recreate_table(sql)

    def customers_add_customer(self, email, fname, sname, contactno):
        values = (email, fname, sname, contactno)
        sql = "INSERT INTO Customers (Email, Firstname, Surname, Contactno) VALUES (?, ?, ?, ?)"
        self.insert_record(sql, values)
        
    def customers_delete_customer(self, custid):
        sql = "DELETE FROM Customers WHERE CustID=?"
        self.delete_record(sql, custid)
        
    def customers_update_customer(self, newemail, fname, sname, contactno, oldemail):
        values = (newemail, fname, sname, contactno, oldemail)
        sql = "UPDATE Customers SET Email=?, Firstname=?, Surname=?, ContactNo=? WHERE Email=?"
        self.update(sql, values)
        
    def customers_select_custid(self, email):
        with sqlite3.connect(self.dbname) as db:
            cursor = db.cursor()
            sql = "SELECT CustID FROM Customers WHERE Email=?"
            cursor.execute(sql, (email,))
            data = cursor.fetchone()
            return data

    def customers_select_customer(self, email):
        sql = "SELECT * FROM Customers WHERE Email=?"
        return self.select_dataspecific_fetchone(sql, (email,))

    def customers_select_customers(self):
        sql = "SELECT * FROM Customers"
        return self.select(sql)


class Bookings(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self.reset_bookings_table()

    def reset_bookings_table(self):
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

    def bookings_add_booking(self, TableID, CustID, Time, Date, NoPeople):
        BillTotal = "0.00"
        values = (Time, Date, NoPeople, TableID, BillTotal, CustID)
        sql = "INSERT INTO Bookings (Time, Date, NoPeople, TableID, BillTotal, CustID) VALUES (?, ?, ?, ?, ?, ?)"
        self.insert_record(sql, values)

    def bookings_delete_booking(self, custid, time, date):
        values = (time, date, custid)
        sql = "DELETE FROM Bookings WHERE Time=? AND Date=? AND CustID=?"
        self.delete_record(sql, values)
        
    def bookings_select_booking_for_date(self, date):
        sql = "SELECT * FROM Bookings WHERE Date=?"
        return self.select_dataspecific_fetchall(sql, (date,))
        
    def bookings_select_booking_for_dateandtime(self, date, time):
        sql = "SELECT * FROM Bookings WHERE Date=? AND Time=?"
        return self.select_dataspecific_fetchall(sql, (date, time))




    def bookings_select_booking_bill(self):
        tableid = input("Please enter the Table of the bill you would like: ")
        time = input("Please enter the time of the booking of the bill you would like: ")
        date = input("Please enter the date of the booking of the bill you would like (YYYY-MM-DD): ")
        sql = "SELECT BillTotal FROM Bookings WHERE TableID=? AND Time=? AND Date=?"
        values = (tableid, time, date)
        bill = str(self.select_dataspecific_fetchone(sql, values))
        bill = bill[1: len(bill)-2]
        print("The current bill for table " + str(tableid) + " is: " + bill)

    def bookings_select_booking_fromtableid(self, tableid):
        sql = "SELECT * FROM Bookings WHERE TableID=?"
        return self.select_dataspecific_fetchone(sql, (tableid,))

    def bookings_select_bookingid(self, TableID):
        sql = "SELECT BookingID FROM Bookings WHERE TableID=? AND Time=? AND Date=?"
        now = datetime.now()
        current_hour = now.strftime("%H")
        today = date.today()
        values = (TableID, current_hour, today)
        self.select_dataspecific_fetchone(sql, values)

    def bookings_increase_booking_billtotal(self, bookingid, ordercost):
        sql = "SELECT BillTotal FROM Bookings WHERE BookingID=?"
        oldbilltuple = self.select_dataspecific_fetchone(sql, (bookingid,))
        oldbill = oldbilltuple[0]
        newbill = oldbill + ordercost
        sql = "UPDATE Booking SET BillTotal=? WHERE BookingID=?"
        self.update(sql, newbill, bookingid)
  

class Tables(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self.reset_tables_table()

    def reset_tables_table(self):
        sql = """CREATE TABLE Tables
                (TableID INTEGER PRIMARY KEY AUTOINCREMENT,
                NoSeats INTEGER,
                Description TEXT)"""
        self.recreate_table(sql)

    def tables_find_table_for_booking(self, Time, Date, nopeople):
        booked = False
        while not booked:
            sql = "SELECT TableID FROM Tables WHERE NoSeats=?"
            tableids = self.select_dataspecific_fetchall(sql, (nopeople,))
            for i in range(0, len(tableids)):
                tableid = str(tableids[i])
                values = (tableid[1], Time, Date)
                sql = "SELECT * FROM Booking WHERE TableID=? AND Time=? AND Date=?"
                booking = self.select_dataspecific_fetchall(sql,values)
                if booking == []:
                    break
            if booking == []:
                booked = True
                return tableid[1]
            else:
                return -1

    def insert_table_record(self):
        NoSeats = input("Please enter the number of seats for this table: ")
        Description = input("Please enter the description for this table: ")
        values = (NoSeats, Description)
        sql = "INSERT INTO Tables (NoSeats, Description) VALUES (?, ?)"
        self.insert_record(sql, values)
        print("\nThe Table has been added to the database.")

    def delete_table_record(self, tableid):
        sql = "DELETE FROM Tables WHERE TableID=?"
        self.delete_record(sql, (tableid,))
        print("\nThe Table has been deleted from the database.")
    
    def update_table_record(self, oldtableid):
        print("Please enter the new details of the table:")
        noseats = input("Number of Seats: ")
        description = input("Description: ")
        sql = "UPDATE Tables SET NoSeats=?, Description=? WHERE TableID=?"
        values = (noseats, description, oldtableid)
        self.update(sql, values)
        print("The details of the table have been updated.")

    def print_all_tables(self):
        sql = "SELECT * FROM Tables ORDER BY NoSeats ASC"
        tables = self.select(sql)
        for i in range(0, (len(tables))):
            print("\nTable " + str(tables[i][0]) + " details:"
                    + "\n   Number of Seats: " + str(tables[i][1])
                    + "\n   Description: " + str(tables[i][2]))


class Order(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self.reset_order_table()

    def reset_order_table(self):
        sql = """CREATE TABLE OrderTable
                (OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
                Date TEXT,
                Time TEXT,
                TotalPrice REAL,
                TableID INTEGER,
                FOREIGN KEY (TableID) REFERENCES Tables(TableID))"""
        self.recreate_table(sql)

    def insert_order_record(self, TableID):
        TotalPrice = 0.00
        today = date.today()
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        values = (today, time, TotalPrice, TableID)
        sql = "INSERT INTO OrderTable (Date, Time, TotalPrice, TableID) VALUES (?, ?, ?, ?)"
        self.insert_record(sql, values)
        sql = "SELECT OrderID FROM OrderTable WHERE Date=? AND Time=? AND TotalPrice=? AND TableID=?"
        orderidtuple = self.select_dataspecific_fetchone(sql, values)
        orderid = orderidtuple[0]
        return orderid

    def delete_order_record(self, orderid):
        sql = "DELETE FROM OrderTable WHERE OrderID=?"
        self.delete_record(sql, (orderid,))

    def increase_order_totalprice(self, orderid, price):
        sql = "SELECT TotalPrice FROM OrderTable WHERE OrderID=?"
        oldpricetuple = self.select_dataspecific_fetchone(sql, (orderid,))
        oldprice = oldpricetuple[0]
        newprice = oldprice + price
        sql = "UPDATE OrderTable SET TotalPrice=? WHERE OrderID=?"
        self.update(sql, (newprice, orderid))

    def get_order_totalprice(self, orderid):
        sql = "SELECT TotalPrice FROM OrderTable WHERE OrderID=?"
        pricetuple = self.select_dataspecific_fetchone(sql, (orderid,))
        price = pricetuple[0]
        return price

    def select_orders_for_table(self):
        tableid = input("Please enter the table of the orders you would like to see: ")
        sql = "SELECT * FROM OrderTable WHERE TableID=?"
        orders = self.select_dataspecific_fetchall(sql, (tableid,))
        for i in range(0, (len(orders))):
            print("\nOrder " + str(orders[i][0]) + " details:"
                    + "\n   Date and Time: " + str(orders[i][1])
                    + "\n   Total Price: " + str(orders[i][2])
                    + "\n   Table ID: " + str(orders[i][3]))

    def select_orders_for_date(self):
        chosendate = input("Please enter the date of the orders you would like to see (YYYY-MM-DD): ")
        sql = "SELECT * FROM OrderTable WHERE Date=?"
        orders = self.select_dataspecific_fetchall(sql, (chosendate,))
        for i in range(0, (len(orders))):
            print("\nOrder " + str(orders[i][0]) + " details:"
                    + "\n   Date and Time: " + str(orders[i][1])
                    + "\n   Total Price: " + str(orders[i][2])
                    + "\n   Table ID: " + str(orders[i][3]))


class OrderProduct(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self.reset_orderproduct_table()

    def reset_orderproduct_table(self):
        sql = """CREATE TABLE OrderProduct
                (OrderProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                ProductID INTEGER,
                Quantity INTEGER,
                OrderID INTEGER,
                FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
                FOREIGN KEY (OrderID) REFERENCES OrderTable(OrderID))"""
        self.recreate_table(sql)

    def insert_orderproduct_record(self, OrderID, ProductID, quantity):
        sql = "INSERT INTO OrderProduct (ProductID, Quantity, OrderID) VALUES (?, ?, ?)"
        self.insert_record(sql, (ProductID, quantity, OrderID))


class Product(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self.reset_product_table()

    def reset_product_table(self):
        sql = """CREATE TABLE Product
                (ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                Type TEXT,
                Name TEXT,
                Price REAL,
                QuantityAvailable INTEGER)"""
        self.recreate_table(sql)

    def insert_product_record(self):
        type = input("Please enter the type of product: ")
        name = input("Please enter the name of the product: ")
        price = input("Please enter the price of the product: ")
        quantity = 0
        values = (type, name, price, quantity)
        sql = "INSERT INTO Product (Type, Name, Price, QuantityAvailable) VALUES (?, ?, ?, ?)"
        self.insert_record(sql, values)
        sql = "SELECT ProductID FROM Product WHERE Name=? AND Price=?"
        idtuple = self.select_dataspecific_fetchone(sql, (name, price))
        id = idtuple[0]
        return id

    def delete_product_record(self, productid):
        sql = "DELETE FROM Product WHERE ProductID=?"
        self.delete_record(sql, (productid,))
        print("\nThe Product has been deleted from the the database.")

    def print_all_products(self):
        sql = "SELECT * FROM Product ORDER BY Type ASC"
        products = self.select(sql)
        for i in range(0, (len(products))):
            print("\nProduct " + str(products[i][0]) + " details:"
                    + "\n   Type: " + str(products[i][1])
                    + "\n   Name: " + str(products[i][2])
                    + "\n   Price: " + str(products[i][3])
                    + "\n   Quantity Available: " + str(products[i][4]))

    def print_menu(self):
        sql = "SELECT * FROM Product WHERE Type=?"
        starters = self.select_dataspecific_fetchall(sql, "Starter")
        print("\nStarters:")
        for i in range(0, (len(starters))):
            print("\n   " + str(starters[i][2]) + " - " + str(starters[i][3]))
        mains = self.select_dataspecific_fetchall(sql, "Main")
        print("\nMains:")
        for i in range(0, (len(mains))):
            print("\n   " + str(mains[i][2]) + " - " + str(mains[i][3]))
        sides = self.select_dataspecific_fetchall(sql, "Side")
        print("\nSides:")
        for i in range(0, (len(sides))):
            print("\n   " + str(sides[i][2]) + " - " + str(sides[i][3]))
        desserts = self.select_dataspecific_fetchall(sql, "Dessert")
        print("\nDesserts:")
        for i in range(0, (len(desserts))):
            print("\n   " + str(desserts[i][2]) + " - " + str(desserts[i][3]))

    def select_product_id(self, name):
        sql = "SELECT ProductID FROM Product WHERE Name=?"
        prodidtuple = self.select_dataspecific_fetchone(sql, (name,))
        prodid = prodidtuple[0]
        return prodid

    def check_quantity_availabilty(self, quantity, productid):
        sql = "SELECT QuantityAvailable FROM Product WHERE ProductID=?"
        availabletuple = self.select_dataspecific_fetchone(sql, (productid,))
        available = availabletuple[0]
        if available < quantity:
            print("There is sold out, please re-enter order.")
            return False
        else:
            return True

    def get_product_price(self, productid):
        sql = "SELECT Price FROM Product WHERE ProductID=?"
        price = self.select_dataspecific_fetchone(sql, (productid,))[0]
        return price

    def reduce_product_quantity(self, productid, quantity):
        sql = "SELECT QuantityAvailable FROM Product WHERE ProductID=?"
        oldquantity = self.select_dataspecific_fetchone(sql, (productid,))
        newquantity = oldquantity - quantity
        sql = "UPDATE Product SET QuantityAvailable=? WHERE ProductID=?"
        self.update(sql, (newquantity, productid))

    def get_all_products(self):
        sql = "SELECT * FROM Product"
        return self.select(sql)

    def insert_product_quantity(self, quantity, productid):
        sql = "UPDATE Product SET QuantityAvailable=? WHERE ProductID=?"
        values = (quantity, productid)
        self.update(sql, values)


class Use(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self.reset_use_table()

    def reset_use_table(self):
        sql = """CREATE TABLE Use
                (UseID INTEGER PRIMARY KEY AUTOINCREMENT,
                ProductID INTEGER,
                IngredientID INTEGER,
                QuantityInKilos REAL,
                FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
                FOREIGN KEY (IngredientID) REFERENCES Ingredient(IngredientID))"""
        self.recreate_table(sql)
        
    def insert_use_record(self, ProductID, IngredientID):
        Quantity = int(input("Please enter the amount in kilos needed of this ingredient for the product: "))
        sql = "INSERT INTO Use (ProductID, IngredientID, QuantityInKilos) VALUES (?, ?, ?)"
        self.insert_record(sql, (ProductID, IngredientID, Quantity))

    def delete_use_record(self, productid):
        sql = "DELETE FROM Use WHERE ProductID=?"
        self.delete_record(sql, (productid,))

    def select_all_uses_forproduct(self, productid):
        sql = "SELECT * FROM Use WHERE ProductID=?"
        uses = self.select_dataspecific_fetchall(sql, (productid,))
        return uses

    def select_use_quantity(self, useid):
        sql = "SELECT QuantityInKilos FROM Use WHERE UseID=?"
        quantitytuple = self.select_dataspecific_fetchone(sql, (useid,))
        quantity = quantitytuple[0]
        return quantity


class Ingredient(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self.reset_ingredient_table()

    def reset_ingredient_table(self):
        sql = """CREATE TABLE Ingredient
                (IngredientID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Type TEXT,
                StoragePlace TEXT,
                CostPerKilo REAL,
                StockInKilos REAL)"""
        self.recreate_table(sql)

    def insert_ingredient_record(self, Name, Type, StoragePlace, CostPerKilo, StockInKilos):
        values = (Name, Type, StoragePlace, CostPerKilo, StockInKilos)
        sql = "INSERT INTO Ingredient (Name, Type, StoragePlace, CostPerKilo, StockInKilos) VALUES (?, ?, ?, ?, ?)"
        self.insert_record(sql, values)

    def delete_ingredient_record(self):
        ingid = input("Please enter the Ingredient ID of the Ingredient you wish to delete: ")
        sql = "DELETE FROM Ingredient WHERE IngredientID=?"
        self.delete_record(sql, (ingid,))
        print("\nThe Ingredient has been deleted from the database.")

    def reduce_ingredient_stock(self, ingredientid, quantity):
        sql = "SELECT StockInKilos FROM Ingredient WHERE IngredientID=?"
        oldstocktuple = self.select_dataspecific_fetchone(sql, (ingredientid,))
        oldstock = oldstocktuple[0]
        newstock = oldstock - quantity
        sql = "UPDATE Ingredient SET StockInKilos=? WHERE IngredientID=?"
        values = (newstock, ingredientid)
        self.update(sql, values)

    def select_ingredient_stock(self, ingredientid):
        sql = "SELECT StockInKilos FROM Ingredient WHERE IngredientID=?"
        stocktuple = self.select_dataspecific_fetchone(sql, (ingredientid,))
        stock = stocktuple[0]
        return stock

    def select_ingredientid(self):
        name = input("Please enter the name of an ingredient for this product: ")
        sql = "SELECT IngredientID FROM Ingredient WHERE Name=?"
        idtuple = self.select_dataspecific_fetchone(sql, (name,))
        id = idtuple[0]
        return id

    
class IngredientBatch(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)
        self.reset_ingredientbatch_table()

    def reset_ingredientbatch_table(self):
        sql = """CREATE TABLE IngredientBatch
                (IngredientBatchID INTEGER PRIMARY KEY AUTOINCREMENT,
                IngredientID INTEGER,
                Quantity REAL,
                ExpiryDate TEXT,
                FOREIGN KEY (IngredientID) REFERENCES Ingredient(IngredientID))"""
        self.recreate_table(sql)

    def insert_ingredientbatch_record(self, IngredientID, Quantity,
                                      ExpiryDate):
        sql = "INSERT INTO IngredientBatch (IngredientID, Quantity, ExpiryDate) VALUES (?, ?, ?)"
        self.insert_record(sql, (IngredientID, Quantity, ExpiryDate))

    def delete_ingredientbatch_record(self):
        ingbatchid = input("Please enter the Ingredient Batch ID of the Batch you wish to delete: ")
        sql = "DELETE FROM IngredientBatch WHERE IngredientBatchID=?"
        self.delete_record(sql, (ingbatchid,))
        print("\nThe Batch has been deleted from the database.")