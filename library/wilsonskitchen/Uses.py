from Table import Table
from constants import LOGGER


class Uses(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_uses_table(self) -> None:
        try:
            # calls recreate_table 
            # to execute sql
            sql = """CREATE TABLE Uses
                    (UseID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ProductID INTEGER,
                    IngredientID INTEGER,
                    QuantityInKilos REAL,
                    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
                    FOREIGN KEY (IngredientID) REFERENCES Ingredient(IngredientID))"""
            self.recreate_table(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Uses table could not be reset.") from err

    def add_use(self, ProductID, IngredientID, Quantity) -> None:
        try:
            # calls insert_record 
            # to execute sql with values
            sql = """INSERT 
                    INTO Uses (ProductID, IngredientID, QuantityInKilos) 
                    VALUES (?, ?, ?)"""
            self.insert_record(sql, (ProductID, IngredientID, Quantity))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Use of ingredient could not be added.") from err

    def delete_use(self, productid) -> None:
        try:
            # calls delete_record
            # to execute sql with productid
            sql = """DELETE 
                    FROM Uses 
                    WHERE ProductID=?"""
            self.delete_record(sql, (productid,))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Use of ingredient could not be deleted.") from err

    def select_uses_forproduct(self, productid) -> tuple:
        try:
            # calls select_dataspecific_fetchall
            # to execute sql with productid
            # returns records
            sql = """SELECT * 
                    FROM Uses 
                    WHERE ProductID=?"""
            uses = self.select_dataspecific_fetchall(sql, (productid,))
            return uses
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Use of ingredient for the product could not be found.") from err

    def select_use_quantity(self, useid) -> float:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with useid
            # returns quantity
            sql = """SELECT QuantityInKilos 
                    FROM Uses 
                    WHERE UseID=?"""
            quantitytuple = self.select_dataspecific_fetchone(sql, (useid,))
            quantity = quantitytuple[0]
            return quantity
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Use of ingredient quantity could not be found.") from err

    def select_uses_from_ingid(self, ingid) -> tuple:
        try:
            # calls select_dataspecific_fetchall
            # to execute sql with ingid
            # returns records
            sql = """SELECT * 
                    FROM Uses 
                    WHERE IngredientID=?"""
            uses = self.select_dataspecific_fetchall(sql, (ingid,))
            return uses
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Uses of ingredient could not be found.") from err
