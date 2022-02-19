from Table import Table
from constants import LOGGER
from ast import Tuple


class IngredientBatches(Table):
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
