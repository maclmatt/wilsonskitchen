from unittest import TextTestRunner
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
    _productnamelist = None
    _productidlist = None
    _quantitylist = None
    _productavailabilitieslist = None
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
        self._productnamelist = List()
        self._productidlist = List()
        self._quantitylist = List()
        self._productavailabilitieslist = List()

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
    def productnamelist(self):
        return self._productnamelist

    @property
    def productidlist(self):
        return self._productidlist

    @property
    def quantitylist(self):
        return self._quantitylist

    @property
    def productavailabilitieslist(self):
        return self._productavailabilitieslist

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
        names = self._productnamelist.return_list()
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
                usesofproduct = self._uses.uses_select_uses_forproduct(checkproducts[i][0])
                for i in range(0, len(usesofproduct)):
                    stock = self._ingredients.ingredients_select_ingredient_stock(usesofproduct[i][2])
                    usequantity = self._uses.uses_select_use_quantity(usesofproduct[i][0])
                    available = stock // usequantity
                    self._productavailabilitieslist.list_add_item(available)
                lowest = self._productavailabilitieslist.list_return_lowest()
                self._products.products_add_product_quantity(lowest, checkproducts[i][0])
            return True

        if check == False:
            self._orders.orders_delete_order(orderid)
            return False







    elif choice == "6":
        print("\nMenu Details menu:\n"
            + "   1. Add new product\n"
            + "   2. Delete product\n"
            + "   3. Update product details\n"
            + "   4. Get all products\n"
            + "   5. Print current menu")
        menuchoice = input("Please choose an option from the menu above (E to exit this menu): ")
        if menuchoice == "1":
            productid = product.insert_product_record()
            n = int(input("Please enter the number of ingredients needed for this product: "))
            for i in range(1, n):
                ingredientid = ingredient.select_ingredientid()
                use.insert_use_record(productid, ingredientid)
            uses = use.select_all_uses_forproduct(productid)
            availabilitiesofproduct = List()
            for i in range(0, len(uses)):
                stock = ingredient.select_ingredient_stock(uses[i][2])
                usequant = use.select_use_quantity(uses[i][0])
                available = stock // usequant
                availabilitiesofproduct.add_item(available)
            lowest = availabilitiesofproduct.return_lowest()
            product.insert_product_quantity(lowest, productid)
        elif menuchoice == "2":
            productid = input("Please enter the product id of the product you wish to delete: ")
            product.delete_product_record(productid)
            use.delete_use_record(productid)
            print("The product has been deleted from the database")
        elif menuchoice == "3":
            type = input("Would you like the ingredient details of the product (i) or the general details of the product: ")
            if type == "i":
                productid = input("Please enter the product id of the product you wish to update: ")
                product.delete_product_record(productid)
                use.delete_use_record(productid)
                productid = product.insert_product_record()
                n = int(input("Please enter the number of ingredients needed for this product: "))
                for i in range(1, n):
                    ingredientid = ingredient.select_ingredientid()
                    use.insert_use_record(productid, ingredientid)
                uses = use.select_all_uses_forproduct(productid)
                availabilitiesofproduct = List()
                for i in range(0, len(uses)):
                    stock = ingredient.select_ingredient_stock(uses[i][2])
                    usequant = use.select_use_quantity(uses[i][0])
                    available = stock // usequant
                    availabilitiesofproduct.add_item(available)
                lowest = availabilitiesofproduct.return_lowest()
                product.insert_product_quantity(lowest, productid)
        elif menuchoice == "4":
            product.print_all_products()
        elif menuchoice == "5":
            product.print_menu()

    elif choice == "7":
        print("\nIngredient Details menu\n"
            + "   1. Add new ingredient\n"
            + "   2. Delete ingredient\n" #do check of any products with that ingredient - ask if they want to delete that too.
            + "   3. Update ingredient\n"
            + "   4. Print list of all ingredients")
        ingredientchoice = input("Please choose an option from the menu above (E to exit ingredient menu): ")
        if ingredientchoice == "1":
            name = input("Please enter the name of the ingredient: ")
            type = input("Please enter the type of ingredient: ")
            StoragePlace = input("Please enter the storage place of the ingredient: ")
            cost = input("Please enter the cost of the ingredient per kilo: ")
            stock = 50
            ingredient.insert_ingredient_record(name, type, StoragePlace, cost, stock)

    elif choice == "8":
        print("\nStock Details menu\n"
            + "   1. Add new batch of ingredients\n"
            + "   2. Delete batch of ingredients\n"
            + "   3. Update batch of ingredients\n"
            + "   4. Get run down of all ingredient stock")
        stockchoice = input("Please choose an option from the menu above (E to exit stock menu): ")
        if stockchoice == "1":
            ingredientid = input("Please enter the ingredient id of the batch: ")
            quantity = input("Please enter the quantity of the ingredient in kilos: ")
            expirydate = input("Please enter the expriy date of the batch (YYYY-MM-DD): ")
            ingredientbatch.insert_ingredientbatch_record(ingredientid, quantity, expirydate)

    elif choice == "9":
        print("\nLogin Details menu\n"
            + "   1. Add new member of staff account"
            + "   2. Delete an account"
            + "   3. Update account details"
            + "   4. Get list of current employees")
        loginchoice = input("Please choose an option from the menu above (E to exit login menu): ")

    print("\nMain menu:\n"
        + "\n   1. Reload Main menu\n"
        + "\n   2. Customer details\n"
        + "\n   3. Booking details\n"
        + "\n   4. Table details\n"
        + "\n   5. Order details\n"
        + "\n   6. Menu details\n"
        + "\n   7. Ingredient details\n"
        + "\n   8. Stock details\n"
        + "\n   9. Login details\n")
    choice = input("Please choose an option from the menu above (E to exit):")