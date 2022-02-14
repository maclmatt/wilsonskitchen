
from math import prod
from classes import List, Customers, Bookings, Tables, Orders, OrderProducts, Products, Uses, Ingredients, IngredientBatches

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
    _productidlist = None
    _quantitylist = None
    _productavailabilitieslist = None
    _ingredientnameslist = None
    _ingredientquantitylist = None
    _db_name = "wilsons_kitchen.db"

    def __init__(self):
        self._customers = Customers(self._db_name, "Customers")
        self._bookings = Bookings(self._db_name, "Booking")
        self._tables = Tables(self._db_name, "Tables")
        self._orders = Orders(self._db_name, "Orders")
        self._orderproducts = OrderProducts(self._db_name, "OrderProducts")
        self._products = Products(self._db_name, "Products")
        self._uses = Uses(self._db_name, "Uses")
        self._ingredients = Ingredients(self._db_name, "Ingredients")
        self._ingredientbatches = IngredientBatches(self._db_name, "IngredientBatches")
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

    def restaruant_recalculate_quantityavailable_for_product(self, productid):
        usesofproduct = self._uses.uses_select_uses_forproduct(productid)
        for i in range(0, len(usesofproduct)):
            stock = self._ingredients.ingredients_select_ingredient_stock(usesofproduct[i][2])
            usequantity = self._uses.uses_select_use_quantity(usesofproduct[i][0])
            available = stock // usequantity
            self._productavailabilitieslist.list_add_item(available)
        lowest = self._productavailabilitieslist.list_return_lowest()
        self._products.products_add_product_quantity(lowest, productid)

    def restaurant_make_booking(self, time, date, nopeople, custid):
        tableid = self._tables.tables_find_table_for_booking(time, date, nopeople)
        if tableid == -1:
            return False
        else:
            self._bookings.bookings_add_booking(tableid, custid, time, date, nopeople)
            return True

    def restaurant_delete_booking(self, email, time, date):
        custid = self._customers.customers_select_custid(email)[0]
        self._bookings.bookings_delete_booking(custid, time, date)

    def restaurant_make_order(self, tableid, n):
        orderid = self._orders.orders_add_order(tableid)
        ids = self._productidlist.return_list()
        quantity = self._quantitylist.return_list()

        check = True
        for i in range(0, n-1):
            check = self._products.products_check_quantity_availabilty(quantity[i], ids[i])
            if check == False:
                break

            self._orderproducts.orderproducts_add_orderproduct(orderid, ids[i], quantity[i])
            price = self._products.products_get_product_price(ids[i])
            sumprice = price * quantity[i]
            self._orders.orders_add_orderproduct_price(orderid, sumprice)

            usesofproduct = self._uses.uses_select_uses_forproduct(ids[i])
            for i in range(0, len(usesofproduct)):
                usequantity = quantity[i] * usesofproduct[i][3]
                self._ingredients.ingredients_reduce_ingredient_stock(usesofproduct[i][2], usequantity)
            
            ordercost = self._orders.orders_get_order_totalprice(orderid)
            bookingid = self._bookings.bookings_select_bookingid(tableid)
            self._bookings.bookings_increase_booking_billtotal(bookingid, ordercost)

            checkproducts = self._products.products_get_all_products()
            for i in range(0, len(checkproducts)):
                self.restaruant_recalculate_quantityavailable_for_product(checkproducts[i][0])
            return True

        if check == False:
            self._orders.orders_delete_order(orderid)
            return False

    def restaurant_make_product(self, type, name, price, n):
        productid = self._products.products_add_product(type,  name, price)
        ingredientnames = self._ingredientnameslist.return_list()
        ingredientquantities = self._ingredientquantitylist.return_list()
        for i in range(0, n-1):
            ingredientid = self._ingredients.ingredients_select_ingredientid(ingredientnames[i])
            self._uses.uses_add_use(productid, ingredientid, ingredientquantities[i])
        self.restaruant_recalculate_quantityavailable_for_product(productid)


