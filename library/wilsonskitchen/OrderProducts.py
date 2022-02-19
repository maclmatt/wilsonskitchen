from Table import Table
from constants import LOGGER

class OrderProducts(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_orderproducts_table(self) -> None:
        try:
            # calls recreate_table 
            # to execute sql
            sql = """CREATE TABLE OrderProducts
                    (OrderProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ProductID INTEGER,
                    Quantity INTEGER,
                    OrderID INTEGER,
                    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
                    FOREIGN KEY (OrderID) REFERENCES OrderTable(OrderID))"""
            self.recreate_table(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Orderproducts table could not be reset.") from err

    def add_orderproduct(self, OrderID, ProductID, quantity) -> None:
        try:
            # calls insert_record 
            # to execute sql with values
            values = (ProductID, quantity, OrderID)
            sql = """INSERT 
                    INTO OrderProducts (ProductID, Quantity, OrderID) 
                    VALUES (?, ?, ?)"""
            self.insert_record(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Orderproduct could not be added.") from err
