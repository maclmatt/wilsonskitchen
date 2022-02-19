from Table import Table
from constants import LOGGER


class Ingredients(Table):
    def __init__(self, dbname, tblname):
        super().__init__(dbname, tblname)

    def reset_ingredients_table(self) -> None:
        try:
            # calls recreate_table 
            # to execute sql
            sql = """CREATE TABLE Ingredients
                    (IngredientID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Type TEXT,
                    StoragePlace TEXT,
                    CostPerKilo REAL,
                    StockInKilos REAL)"""
            self.recreate_table(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredient table could not be reset.") from err

    def add_ingredient(self, Name, Type, StoragePlace, CostPerKilo, StockInKilos) -> None:
        try:
            # calls insert_record 
            # to execute sql with values
            values = (Name, Type, StoragePlace, CostPerKilo, StockInKilos)
            sql = """INSERT 
                    INTO Ingredients (Name, Type, StoragePlace, CostPerKilo, StockInKilos) 
                    VALUES (?, ?, ?, ?, ?)"""
            self.insert_record(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredient could not be added.") from err

    def delete_ingredient(self, ingid) -> None:
        try:
            # calls delete_record
            # to execute sql with ingid
            sql = """DELETE 
                    FROM Ingredients 
                    WHERE IngredientID=?"""
            self.delete_record(sql, (ingid,))
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredient could not be deleted.") from err

    def reduce_ingredient_stock(self, ingredientid, quantity) -> None:
        try:
            # reduces ingredient stock by quantity
            sql = """SELECT StockInKilos 
                    FROM Ingredients 
                    WHERE IngredientID=?"""
            # calls select_dataspecific_fetchone
            # to execute sql with ingredientid
            oldstocktuple = self.select_dataspecific_fetchone(sql, (ingredientid,))
            oldstock = oldstocktuple[0]
            newstock = oldstock - quantity
            values = (newstock, ingredientid)
            sql = """UPDATE Ingredients 
                    SET StockInKilos=? 
                    WHERE IngredientID=?"""
            # calls update
            # to execute sql with values
            self.update(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredient stock could not be reduced.") from err

    def increase_ingredient_stock(self, ingredientid, quantity) -> None:
        try:
            # increases ingredient stock by quantity
            sql = """SELECT StockInKilos 
                    FROM Ingredients 
                    WHERE IngredientID=?"""
            # calls select_dataspecific_fetchone
            # to execute sql with ingredientid
            oldstocktuple = self.select_dataspecific_fetchone(sql, (ingredientid,))
            oldstock = oldstocktuple[0]
            newstock = oldstock + quantity
            values = (newstock, ingredientid)
            sql = """UPDATE Ingredients 
                    SET StockInKilos=? 
                    WHERE IngredientID=?"""
            # calls update
            # to execute sql with values
            self.update(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredient stock could not be increased.") from err

    def select_ingredient_stock(self, ingredientid) -> float:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with ingredientid
            # returns stock
            sql = """SELECT StockInKilos 
                    FROM Ingredients 
                    WHERE IngredientID=?"""
            stocktuple = self.select_dataspecific_fetchone(sql, (ingredientid,))
            stock = stocktuple[0]
            return stock
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredient stock could not be found.") from err

    def select_ingredientid(self, name) -> tuple:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with name
            # returns id in form (id,)
            sql = """SELECT IngredientID 
                    FROM Ingredients 
                    WHERE Name=?"""
            idtuple = self.select_dataspecific_fetchone(sql, (name,))
            return idtuple
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredient ID could not be found.") from err

    def select_cost(self, ingid) -> float:
        try:
            # calls select_dataspecific_fetchone
            # to execute sql with ingid
            # returns cost
            sql = """SELECT CostPerKilo 
                    FROM Ingredients 
                    WHERE IngredientID=?"""
            costtuple = self.select_dataspecific_fetchone(sql, (ingid,))
            cost = costtuple[0]
            return cost
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredient cost could not be found.") from err

    def update_ingredient(self, name, newtype, newstorageplace, newcost) -> None:
        try:
            # calls update
            # to execute sql with values
            values = (newtype, newstorageplace, newcost, name)
            sql = """UPDATE Ingredients 
                    SET Type=?, StoragePlace=?, CostPerKilo=? 
                    WHERE Name=?"""
            self.update(sql, values)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredient could not be updated.") from err

    def select_ingredients(self) -> tuple:
        try:
            # calls select
            # to execute sql
            # returns records
            sql = """SELECT * 
                    FROM Ingredients"""
            return self.select(sql)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise RuntimeError("Ingredients could not be found.") from err
