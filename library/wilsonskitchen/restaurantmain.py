from List import List
from Customers import Customers
from Bookings import Bookings
from TablesofRestaurant import TablesofRestaurant
from Orders import Orders
from OrderProducts import OrderProducts
from Products import Products
from Uses import Uses
from Ingredients import Ingredients
from IngredientBatches import IngredientBatches
from StaffMembers import StaffMembers
from datetime import date, datetime
from constants import LOGGER, DB_NAME


class Restaurant():
    _customers = None
    _bookings = None
    _tables = None
    _orders = None
    _orderproducts = None
    _products = None
    _uses = None
    _ingredients = None
    _ingredientbatches = None
    _staffmembers = None
    _productidlist = None
    _quantitylist = None
    _productavailabilitieslist = None
    _ingredientnameslist = None
    _ingredientquantitylist = None

    def __init__(self):
        self._customers = Customers(DB_NAME, "Customers")
        self._bookings = Bookings(DB_NAME, "Bookings")
        self._tables = TablesofRestaurant(DB_NAME, "Tables")
        self._orders = Orders(DB_NAME, "Orders")
        self._orderproducts = OrderProducts(DB_NAME, "OrderProducts")
        self._products = Products(DB_NAME, "Products")
        self._uses = Uses(DB_NAME, "Uses")
        self._ingredients = Ingredients(DB_NAME, "Ingredients")
        self._ingredientbatches = IngredientBatches(DB_NAME, "IngredientBatches")
        self._staffmembers = StaffMembers(DB_NAME, "StaffMembers")
        self._productidlist = List()
        self._quantitylist = List()
        self._productavailabilitieslist = List()
        self._ingredientnameslist = List()
        self._ingredientquantitylist = List()

    @property
    def customers(self):
        return self._customers

    @property
    def bookings(self):
        return self._bookings

    @property
    def tables(self):
        return self._tables

    @property
    def orders(self):
        return self._orders

    @property
    def orderproducts(self):
        return self._orderproducts

    @property
    def products(self):
        return self._products

    @property
    def uses(self):
        return self._uses

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def ingredientbatches(self):
        return self._ingredientbatches

    @property
    def staffmembers(self):
        return self._staffmembers

    @property
    def productidlist(self):
        return self._productidlist

    @property
    def quantitylist(self):
        return self._quantitylist

    @property
    def productavailabilitieslist(self):
        return self._productavailabilitieslist

    @property
    def ingredientnameslist(self):
        return self._ingredientnameslist

    @property
    def ingredientquantitylist(self):
        return self._ingredientquantitylist

    def recalculate_quantityavailable_for_product(self, productid) -> None:
        try:
            # selects all uses of the product
            usesofproduct = self._uses.select_uses_forproduct(productid)
            self._productavailabilitieslist.wipe()
            for i in range(0, len(usesofproduct)):
                # selects the ingredient stock required for the product for each ingredient
                stock = self._ingredients.select_ingredient_stock(usesofproduct[i][2])
                usequantity = self._uses.select_use_quantity(usesofproduct[i][0])
                available = stock // usequantity
                # adds the availability of the product based on each ingredient to list
                self._productavailabilitieslist.add_item(available)
            lowest = self._productavailabilitieslist.return_lowest()
            # inserts the lowest availability into product quantity
            self._products.add_product_quantity(lowest, productid)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise

    def make_booking(self, time, date, nopeople, custid) -> bool:
        try:
            # selects tableid of a table available
            tableid = self._tables.find_table_for_booking(time, date, nopeople)
            # returns whether an available table was found or not
            if tableid == -1:
                return False
            else:
                self._bookings.add_booking(tableid, custid, time, date, nopeople)
                return True
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise

    def delete_booking(self, email, time, date) -> None:
        try:
            # selects custid or customer with correct email
            custid = self._customers.select_custid(email)[0]
            self._bookings.delete_booking_record(custid, time, date)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise

    def make_order(self, tableid, n) -> bool:
        try:
            orderid = self._orders.add_order(tableid)
            ids = self._productidlist.return_list()
            quantity = self._quantitylist.return_list()

            check = True
            for i in range(0, n):
                # checks that product is available
                check = self._products.check_quantity_availability(quantity[i], ids[i])
                if check == False:
                    break

                # updates order price
                # adds orderproduct
                self._orderproducts.add_orderproduct(orderid, ids[i], quantity[i])
                price = self._products.get_product_price(ids[i])
                sumprice = price * quantity[i]
                # adds sumprice to order price in orders table
                self._orders.add_orderproduct_price(orderid, sumprice)

                # updates ingredient stock
                usesofproduct = self._uses.select_uses_forproduct(ids[i])
                quantityofproduct = quantity[i]
                for i in range(0, len(usesofproduct)):
                    usequantity = quantityofproduct * usesofproduct[i][3]
                    self._ingredients.reduce_ingredient_stock(
                        usesofproduct[i][2], usequantity)

            ordercost = self._orders.get_order_totalprice(orderid)
            bookingid = self._bookings.select_bookingid(tableid)
            self._bookings.increase_booking_billtotal(bookingid, ordercost)

            # recalculates quantity available of products 
            # as ingredient stock has changed
            checkproducts = self._products.return_products()
            for i in range(0, len(checkproducts)):
                self.recalculate_quantityavailable_for_product(checkproducts[i][0])

            # returns whether all the products on the order were in stock or not
            if check == False:
                self._orders.delete_order(orderid)
                return False
            else:
                return True
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise

    def make_product(self, type, name, price, n) -> None:
        try:
            productid = self._products.add_product(type,  name, price)
            ingredientnames = self._ingredientnameslist.return_list()
            ingredientquantities = self._ingredientquantitylist.return_list()
            for i in range(0, n):
                # for each ingredient add use record and update cost of product
                ingredientid = self._ingredients.select_ingredientid(ingredientnames[i])[0]
                self._uses.add_use(
                    productid, ingredientid, ingredientquantities[i])
                costofingredient = self._ingredients.select_cost(
                    ingredientid)
                costofproduct = costofingredient * ingredientquantities[i]
                self._products.increase_cost(productid, costofproduct)
            # recalculate quantity available of product
            # as new product has been added
            self.recalculate_quantityavailable_for_product(productid)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise

    def make_ingredientbatch(self, ingname, quantity, expirydate) -> None:
        try:
            # add ingredient batch record and update ingredient stock
            ingredientid = self._ingredients.select_ingredientid(ingname)[0]
            self._ingredientbatches.add_ingredientbatch(ingredientid, quantity, expirydate)
            self._ingredients.increase_ingredient_stock(ingredientid, quantity)

            # recalculate quantity available for products 
            # as ingredient stock has changed
            checkproducts = self._products.return_products()
            for i in range(0, len(checkproducts)):
                self.recalculate_quantityavailable_for_product(checkproducts[i][0])
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise

    def delete_ingredient_and_products(self, ingid) -> None:
        try:
            # select all uses for ingredient
            usesofingredient = self._uses.select_uses_from_ingid(ingid)
            for i in range(0, len(usesofingredient)):
                # for each use of the ingredient:
                    # delete the product and use
                self._products.delete_product(usesofingredient[i][1])
                self._uses.delete_use(usesofingredient[i][1])
            self._ingredients.delete_ingredient(ingid)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise

    def delete_ingredientbatch(self, ingid, expirydate) -> None:
        try:
            # selecting quantity for the ingredient batch
            quantitytuple = self._ingredientbatches.select_quantity(ingid, expirydate)
            quantity = quantitytuple[0]
            # reduces the ingredient stock by the quantity of the ingredient batch
            self._ingredients.reduce_ingredient_stock(ingid, quantity)
            # recalculates quantity available of products
            # as ingredient stock has chnaged
            checkproducts = self._products.return_products()
            for i in range(0, len(checkproducts)):
                self.recalculate_quantityavailable_for_product(checkproducts[i][0])
            self._ingredientbatches.delete_batch(ingid, expirydate)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise

    def delete_outofdate_ingredients(self) -> None:
        try:
            # selects all ingredient batches
            batches = self._ingredientbatches.select_batches()
            for i in range(0, len(batches)):
                # for each batch, check if it is out of date or not
                expirydatestr = batches[i][3]
                expirydate = datetime.strptime(expirydatestr, "%Y-%m-%d").date()
                # if it is out of date, deletes ingredient batch
                if expirydate < date.today():
                    self.delete_ingredientbatch(batches[i][1], expirydatestr)
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise

    def check_outofstock_products(self) -> List:
        try:
            # selects all ingredients
            ings = self._ingredients.select_ingredients()
            ingtobeordered = []
            for i in range(0, len(ings)):
                # for each ingredient, selects all uses
                usesofingredients = self._uses.select_uses_from_ingid(ings[i][0])
                for j in range(0, len(usesofingredients)):
                    # for each use if the ingredient stock is less than the use:
                        # case = "break"
                        # ingredient is added to ingtobeordered list
                    case = "x"
                    if ings[i][5] < usesofingredients[j][3]:
                        ingtobeordered.append(ings[i][1])
                        case = "break"
                    if case == "break":
                        break
            # select all products
            allproducts = self._products.return_products()
            outproducts = []
            for i in range(0, len(allproducts)):
                # for each product if it is out of stock:
                    # product is added to outproducts list
                instock = self._products.check_quantity_availability(1, allproducts[i][0])
                if instock == False:
                    outproducts.append(allproducts[i][2])
            # returns list [a, b] where a is ingtobeordered and b is outproducts
            return [ingtobeordered, outproducts]
        except BaseException as err:
            # logs error in log file
            # raises error to next level
            LOGGER.error(err)
            raise
