from Table import Table
from constants import LOGGER


class IngredientBatches(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_ingredientbatch_table(self) -> None:
        try:
            # calls recreate_table 
            # to execute sql
            sql = """CREATE TABLE IngredientBatches
                    (IngredientBatchID INTEGER PRIMARY KEY AUTOINCREMENT,
                    IngredientID INTEGER,
                    Quantity REAL,
                    ExpiryDate TEXT,
                    FOREIGN KEY (IngredientID) REFERENCES Ingredient(IngredientID))"""
            self.recreate_table(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredientbatches table could not be reset.") from err

    def add_ingredientbatch(self, IngredientID, Quantity, ExpiryDate) -> None:
        try:
            # calls insert_record 
            # to execute sql with values
            values = (IngredientID, Quantity, ExpiryDate)
            sql = """INSERT 
                    INTO IngredientBatches (IngredientID, Quantity, ExpiryDate) 
                    VALUES (?, ?, ?)"""
            self.insert_record(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredientbatch could not be added.") from err

    def delete_batch(self, ingid, expirydate) -> None:
        try:
            # calls delete_record
            # to execute sql with (ingid, expirydate)
            sql = """DELETE 
                    FROM IngredientBatches 
                    WHERE IngredientID=? AND ExpiryDate=?"""
            self.delete_record(sql, (ingid, expirydate))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredientbatch could not be deleted.") from err

    def select_quantity(self, ingid, expirydate) -> tuple:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with values
            # returns record
            values = (ingid, expirydate)
            sql = """SELECT Quantity 
                    FROM IngredientBatches 
                    WHERE IngredientID=? AND ExpiryDate=?"""
            return self.select_dataspecific_fetchone(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredientbatch quantity could not be found.") from err

    def select_batches(self) -> tuple:
        try:
            # calls select
            # to execute sql
            # returns records
            sql = """SELECT * 
                    FROM IngredientBatches"""
            return self.select(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredientbatches could not be found.") from err
