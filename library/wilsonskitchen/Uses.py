from Table import Table
from constants import LOGGER
from ast import Tuple


class Uses(Table):
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
