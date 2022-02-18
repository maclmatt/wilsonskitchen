from classes import List, Customers, Bookings, Tables, Orders, OrderProducts
from classes import Products, Uses, Ingredients, IngredientBatches, StaffMembers
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
        self._tables = Tables(DB_NAME, "Tables")
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

    def restaruant_recalculate_quantityavailable_for_product(self, productid):
        usesofproduct = self._uses.uses_select_uses_forproduct(productid)
        self._productavailabilitieslist.wipe()
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
            if self._bookings.bookings_add_booking(tableid, custid, time, date, nopeople):
                return True
            else:
                return False

    def restaurant_delete_booking(self, email, time, date):
        custid = self._customers.customers_select_custid(email)[0]
        self._bookings.bookings_delete_booking(custid, time, date)

    def restaurant_make_order(self, tableid, n):
        orderid = self._orders.orders_add_order(tableid)
        ids = self._productidlist.return_list()
        quantity = self._quantitylist.return_list()

        check = True
        for i in range(0, n):
            check = self._products.products_check_quantity_availabilty(quantity[i], ids[i])
            if check == False:
                break
            # update order price
            self._orderproducts.orderproducts_add_orderproduct(orderid, ids[i], quantity[i])
            price = self._products.products_get_product_price(ids[i])
            sumprice = price * quantity[i]
            self._orders.orders_add_orderproduct_price(orderid, sumprice)
            # update ingredient stock
            usesofproduct = self._uses.uses_select_uses_forproduct(ids[i])
            quantityofproduct = quantity[i]
            for i in range(0, len(usesofproduct)):
                usequantity = quantityofproduct * usesofproduct[i][3]
                self._ingredients.ingredients_reduce_ingredient_stock(
                    usesofproduct[i][2], usequantity)

        ordercost = self._orders.orders_get_order_totalprice(orderid)
        bookingid = self._bookings.bookings_select_bookingid(tableid)
        self._bookings.bookings_increase_booking_billtotal(bookingid, ordercost)

        checkproducts = self._products.products_return_products()
        for i in range(0, len(checkproducts)):
            self.restaruant_recalculate_quantityavailable_for_product(checkproducts[i][0])

        if check == False:
            self._orders.orders_delete_order(orderid)
            return False
        else:
            return True

    def restaurant_make_product(self, type, name, price, n):
        
        productid = self._products.products_add_product(type,  name, price)
        ingredientnames = self._ingredientnameslist.return_list()
        ingredientquantities = self._ingredientquantitylist.return_list()
        for i in range(0, n):
            ingredientid = self._ingredients.ingredients_select_ingredientid(
                ingredientnames[i])[0]
            self._uses.uses_add_use(
                productid, ingredientid, ingredientquantities[i])
            costofingredient = self._ingredients.ingredients_select_cost(
                ingredientid)
            costofproduct = costofingredient * ingredientquantities[i]
            self._products.products_increase_cost(productid, costofproduct)
        self.restaruant_recalculate_quantityavailable_for_product(productid)

    def restaurant_add_ingredientbatch(self, ingname, quantity, expirydate):
        ingredientid = self._ingredients.ingredients_select_ingredientid(ingname)[0]
        self._ingredientbatches.batches_add_ingredientbatch(ingredientid, quantity, expirydate)
        self._ingredients.ingredients_increase_ingredient_stock(ingredientid, quantity)

        checkproducts = self._products.products_return_products()
        for i in range(0, len(checkproducts)):
            self.restaruant_recalculate_quantityavailable_for_product(checkproducts[i][0])

    def restaurant_delete_ingredient_and_products(self, ingid):
        usesofingredient = self._uses.uses_select_uses_from_ingid(ingid)
        for i in range(0, len(usesofingredient)):
            self._products.products_delete_product(usesofingredient[i][1])
            self._uses.uses_delete_use(usesofingredient[i][1])
        self._ingredients.ingredients_delete_ingredient(ingid)

    def restaurant_delete_ingredientbatch(self, ingid, expirydate):
        # selecting quantity for the ingredient batch
        quantitytuple = self._ingredientbatches.batches_select_quant(ingid, expirydate)
        quantity = quantitytuple[0]
        # reducing the ingredient stock by the quantity of the ingredient batch
        self._ingredients.ingredients_reduce_ingredient_stock(ingid, quantity)
        # retrieving all products, to calculate the new quantity available
        # after this reduction of ingredient stock
        checkproducts = self._products.products_return_products()
        for i in range(0, len(checkproducts)):
            self.restaruant_recalculate_quantityavailable_for_product(checkproducts[i][0])
        self._ingredientbatches.batches_delete_ingredientbatch(ingid, expirydate)

    def restaurant_delete_outofdate_ingredients(self):
        batches = self._ingredientbatches.batches_select_all_batches()
        for i in range(0, len(batches)):
            expirydatestr = batches[i][3]
            expirydate = datetime.strptime(expirydatestr, "%Y-%m-%d").date()
            if expirydate < date.today():
                self.restaurant_delete_ingredientbatch(batches[i][1], expirydatestr)

    def restaurant_check_outofstock_products(self):
        ings = self._ingredients.ingredients_select_ingredients()
        ingtobeordered = []
        for i in range(0, len(ings)):
            usesofingredients = self._uses.uses_select_uses_from_ingid(ings[i][0])
            for j in range(0, len(usesofingredients)):
                case = "x"
                if ings[i][5] < usesofingredients[j][3]:
                    ingtobeordered.append(ings[i][1])
                    case = "break"
                if case == "break":
                    break
        allproducts = self._products.products_return_products()
        outproducts = []
        for i in range(0, len(allproducts)):
            instock = self._products.products_check_quantity_availability(1, allproducts[i][0])
            if instock == False:
                outproducts.append(allproducts[i][2])

        return [ingtobeordered, outproducts]
