from classes import List, Customers, Bookings, Tables, Order, OrderProduct, Product, Use, Ingredient, IngredientBatch

class Restaurant():
    _customers = None
    _bookings = None
    _tables = None
    _order = None
    _orderproduct = None
    _product = None
    _use = None
    _ingredient = None
    _ingredientbatch = None
    _db_name = "wilsons_kitchen.db"

    def __init__(self):
        self._customers = Customers(self._db_name, "Customers")
        self._bookings = Bookings(self._db_name, "Booking")
        self._tables = Tables(self._db_name, "Tables")
        self._order = Order(self._db_name, "OrderTable")
        self._orderproduct = OrderProduct(self._db_name, "OrderProduct")
        self._product = Product(self._db_name, "Product")
        self._use = Use(self._db_name, "Use")
        self._ingredient = Ingredient(self._db_name, "Ingredient")
        self._ingredientbatch = IngredientBatch(self._db_name, "IngredientBatch")

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
    def order(self):
        return self._order
    
    @property
    def orderproduct(self):
        return self._orderproduct

    @property
    def product(self):
        return self._product

    @property
    def use(self):
        return self._use

    @property
    def ingredient(self):
        return self._ingredient

    @property
    def ingredientbatch(self):
        return self._ingredientbatch

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

    














    elif choice == "4":
        print("\nTable Details menu:\n"
            + "   1. Add new table\n"
            + "   2. Delete table\n"
            + "   3. Update table details\n"
            + "   4. Get list of all tables")
        tablechoice = input("Please choose an option from the menu above (E to exit table menu): ")
        if tablechoice == "1":
            tables.insert_table_record()
        elif tablechoice == "2":
            tableid = input("Please enter the Table ID of the Table you wish to delete: ")
            check = booking.select_booking_fromtableid(tableid)
            if check == None:
                tables.delete_table_record(tableid)
            else:
                print("You cannot delete this table as there are bookings made for it.")
        elif tablechoice == "3":
            oldtableid = input("Please enter the Table ID of the Table you wish to update: ")
            check = booking.select_booking_fromtableid(oldtableid)
            if check == None:
                tables.update_table_record(oldtableid)
            else:
                print("You cannot update this table as there are bookings made for it.")
        elif tablechoice == "4":
            tables.print_all_tables()
        else:
            print("That is not a valid choice, the menu will now reload:")
            
    elif choice == "5":
        print("\nOrder Details menu:\n"
            + "   1. Add new order\n"
            + "   2. Get all orders\n")
        orderchoice = input("Please choose an option from the menu above (E to exit order menu): ")
        if orderchoice == "1":
            TableID = input("Please enter which table the order is for: ")
            orderid = order.insert_order_record(TableID)
            n = int(input("Please enter the number of different items on the order: "))
            productnamelist = List()
            productidlist = List()
            Quantitylist = List()
            check = True
            for i in range(1, n):
                newproductname = input("Please enter the product name: ")
                productnamelist.add_item(newproductname)
                newproductid = product.select_product_id(newproductname)
                productidlist.add_item(newproductid)
                newquantity = int(input("Please enter the quantity of the item ordered: "))
                Quantitylist.add_item(newquantity)
                check = product.check_quantity_availabilty(newquantity, newproductid)
                if check == False:
                    break
            if check:
                names = productnamelist.return_list()
                ids = productidlist.return_list()
                quantity = Quantitylist.return_list()
                for i in range(0, n-1):
                    orderproduct.insert_orderproduct_record(orderid, ids[i], quantity[i])
                    price = product.get_product_price(ids[i])
                    sumprice = price * quantity[i]
                    order.increase_order_totalprice(orderid, sumprice)
                    uses = use.select_all_uses_forproduct(ids[i])
                    for i in range(0, len(uses)):
                        usequantity = quantity[i] * uses[i][3]
                        ingredient.reduce_ingredient_stock(uses[i][2], usequantity)
                    ordercost = order.get_order_totalprice(orderid)
                    bookingid = booking.select_bookingid(TableID)
                    booking.increase_booking_billtotal(bookingid, ordercost)
                    
                    products = product.get_all_products()
                    for i in range(0, len(products)):
                        uses = use.select_all_uses_forproduct(int(products[i][0]))
                        availabilitiesofproduct = List()
                        for i in range(0, len(uses)):
                            stock = ingredient.select_ingredient_stock(uses[i][2])
                            usequant = use.select_use_quantity(uses[i][0])
                            available = stock // usequant
                            availabilitiesofproduct.add_item(available)
                        lowest = availabilitiesofproduct.return_lowest()
                        product.insert_product_quantity(lowest, products[i][0])

                else:
                    order.delete_order_record(orderid)
                    print("This product is out of stock, please re-enter order excluding this item.")
            
        elif orderchoice == "2":
            type = input("Would you like to see all orders made by a particular table (t) or a particular date (d): ")
            if type == "t":
                order.select_orders_for_table()
            elif type == "d":
                order.select_orders_for_date()

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