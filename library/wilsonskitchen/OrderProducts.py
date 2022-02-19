from Table import Table
from constants import LOGGER

class OrderProducts(Table):
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
