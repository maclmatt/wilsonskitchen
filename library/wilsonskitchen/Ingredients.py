from Table import Table
from constants import LOGGER
from ast import Tuple


class Ingredients(Table):
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
