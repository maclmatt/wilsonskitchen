from restaurantmain import Restaurant
from constants import LOGGER
import sys

wilsonskitchen = Restaurant()
LOGGER.info("Wilson's Kitchen started")

username = int(input("Please enter your username: "))
password = input("Please enter your password: ")
valid = False
logincount = 1
while valid == False and logincount <= 3:
    status = wilsonskitchen.staffmembers.staffmembers_check_login(
        username, password)
    if status[0] == False:
        logincount += 1
        if logincount == 4:
            sys.exit("You have entered the wrong details 3 times and"
                    + " will be blocked from the system.")
        if status[1] == "neither":
            print("You have entered the wrong username or wrong username and password,"
                + " please re-try:")
            username = int(input("Please enter your username: "))
            password = input("Please enter your password: ")
        else:
            print("You entered the correct username but incorrect password,"
                + " please re-enter:")
            password = input("Please enter your password: ")
    else:
        print("Welcome!")
        access = status[1]
        valid = True

print("\nMain menu:\n"
      + "\n   1. Reset database (all data and tables will be lost)\n"
      + "\n   2. Customer details\n"
      + "\n   3. Booking details\n"
      + "\n   4. Table details\n"
      + "\n   5. Order details\n"
      + "\n   6. Menu details\n"
      + "\n   7. Ingredient details\n"
      + "\n   8. Stock details\n"
      + "\n   9. Login details\n")
choice = input("Please choose an option from the menu above (E to logout): ")

while choice != "E":

    if choice == "1" and access == 1:  # reset
        check = input("Are you sure you want to reset the Customer table (y/n): ")
        if check == "y":
            wilsonskitchen.customers.reset_customers_table()
        check = input("Are you sure you want to reset the Booking table (y/n): ")
        if check == "y":
            wilsonskitchen.bookings.reset_bookings_table()
        check = input("Are you sure you want to reset the Tables table (y/n): ")
        if check == "y":
            wilsonskitchen.tables.reset_tables_table()
        check = input("Are you sure you want to reset the Order table (y/n): ")
        if check == "y":
            wilsonskitchen.orders.reset_orders_table()
        check = input("Are you sure you want to reset the Orderproduct table (y/n): ")
        if check == "y":
            wilsonskitchen.orderproducts.reset_orderproducts_table()
        check = input("Are you sure you want to reset the Product table (y/n): ")
        if check == "y":
            wilsonskitchen.products.reset_products_table()
        check = input("Are you sure you want to reset the Use table (y/n): ")
        if check == "y":
            wilsonskitchen.uses.reset_uses_table()
        check = input("Are you sure you want to reset the Ingredient table (y/n): ")
        if check == "y":
            wilsonskitchen.ingredients.reset_ingredients_table()
        check = input("Are you sure you want to reset the Ingredientbatch table (y/n): ")
        if check == "y":
            wilsonskitchen.ingredientbatches.reset_ingredientbatch_table()
        check = input("Are you sure you want to reset the StaffMembers table (y/n): ")
        if check == "y":
            wilsonskitchen.staffmembers.reset_staffmembers_table()

    elif choice == "1" and access != 1:  # reset 2.0
        print("Unfortunately your account does not have access to reset the database.")

    elif choice == "2":  # customers
        print("\nCustomer Details menu:\n"
              + "   1. Add new customer\n"
                + "   2. Delete customer\n"
                + "   3. Update customer's details\n"
                + "   4. Get customer's details\n"
                + "   5. Get list of all customers\n")
        custchoice = input("Please choose an option from the menu above"
                        + " (E to exit customer menu):")

        if custchoice == "1":
            print("\nPlease enter the details of the new customer:")
            email = input("Email: ")
            fname = input("Firstname: ")
            sname = input("Surname: ")
            contactno = input("Phone number: ")
            if wilsonskitchen.customers.customers_add_customer(email, fname, sname, contactno):
                print("\n" + fname, sname, "has been added to the database.")
                LOGGER.info("has been added to the database. %s %s", fname, sname)
            else:
                print("%s %s could not be added to the database, see log file.", 
                    fname, sname)
                LOGGER.error("%s %s could not be added to the database, see log file.", 
                    fname, sname)

        elif custchoice == "2":
            email = input("\nPlease enter the email of the customer: ")
            custid = wilsonskitchen.customers.customers_select_custid(email)
            wilsonskitchen.customers.customers_delete_customer(custid)
            print("\nThe customer has been deleted from the database.")

        elif custchoice == "3":
            oldemail = input("\nPlease enter the email of the customer: ")
            print("Please enter the new details of the customer:")
            newemail = input("Email :")
            fname = input("Firstname :")
            sname = input("Surname :")
            contactno = input("Phone number: ")
            wilsonskitchen.customers.customers_update_customer(
                newemail, fname, sname, contactno, oldemail)
            print("The Customer's details have been updated.")

        elif custchoice == "4":
            email = input("\nPlease enter the email of the customer: ")
            details = wilsonskitchen.customers.customers_select_customer(email)
            print("\nCustomer details:"
                  + "\n   Customer ID: " + str(details[0])
                  + "\n   Customer Email: " + str(details[1])
                  + "\n   Customer Name: " + str(details[2]), str(details[3])
                  + "\n   Customer Phone number: " + str(details[4]))

        elif custchoice == "5":
            customers = wilsonskitchen.customers.customers_select_customers()
            for i in range(0, (len(customers))):
                print("\nCustomer " + str(customers[i][0]) + "'s details:"
                      + "\n   Customer Email: " + str(customers[i][1])
                      + "\n   Customer Name: " +
                      str(customers[i][2]), str(customers[i][3])
                      + "\n   Customer Phone number: " + str(customers[i][4]))

        else:
            print("That is not a valid choice, the main menu will now reload:")

    elif choice == "3":  # bookings
        print("\nBooking Details menu:\n"
              + "   1. Add new booking\n"
              + "   2. Delete booking\n"
              + "   3. Update booking details\n"
              + "   4. Get all booking details\n"
              + "   5. Print bill\n")
        bookchoice = input("Please choose an option from the menu above"
                        + " (E to exit booking menu): ")

        if bookchoice == "1":
            print("Please enter the details of the new booking:")
            Time = input("Time (HH) - 24hr clock times: ")
            Date = input("Date (YYYY-MM-DD): ")
            nopeople = input("Number of people: ")
            email = input("Email of customer: ")
            custid = wilsonskitchen.customers.customers_select_custid(email)
            if custid == None:
                print("The Customer does not exist on the database,"
                    + " please enter their details: ")
                fname = input("Firstname: ")
                sname = input("Surname: ")
                contactno = input("Phone number: ")
                wilsonskitchen.customers.customers_add_customer(email, fname, sname, contactno)
                custid = wilsonskitchen.customers.customers_select_custid(email)
                print("\n" + fname, sname, "has been added to the database.")
            custid = custid[0]
            booked = wilsonskitchen.restaurant_make_booking(Time, Date, nopeople, custid)
            if booked:
                print("The Booking has been added to the database.")
            else:
                print("There are no tables available at that time for that number of people.")

        elif bookchoice == "2":
            print("Please enter the booking details: ")
            email = input("Email of customer: ")
            time = input("Time: ")
            date = input("Date: ")
            wilsonskitchen.restaurant_delete_booking(email, time, date)

        elif bookchoice == "3":
            print("Please enter the old booking details: ")
            email = input("Email of customer: ")
            time = input("Time (HH) - 24hr clock times: ")
            date = input("Date (YYYY-MM-DD): ")
            wilsonskitchen.restaurant_delete_booking(email, time, date)

            print("Please enter the new details of the booking:")
            Time = input("Time (HH) - 24hr clock times: ")
            Date = input("Date (YYYY-MM-DD): ")
            nopeople = input("Number of people: ")
            email = input("Email of customer: ")
            custid = wilsonskitchen.customers.customers_select_custid(email)[0]
            if custid == None:
                print("The Customer does not exist on the database,"
                    + " please enter their details: ")
                email = input("Email: ")
                fname = input("Firstname: ")
                sname = input("Surname: ")
                contactno = input("Phone number: ")
                wilsonskitchen.customers.customers_add_customer(email, fname, sname, contactno)
                print("\n" + fname, sname, "has been added to the database.")
            booked = wilsonskitchen.restaurant_make_booking(Time, Date, nopeople, custid)
            if booked:
                print("The Booking has been updated.")
            else:
                print("There are no tables available at that time for that number of people.")

        elif bookchoice == "4":
            type = input("Please enter whether you would like all the bookings for date"
                        + " or date and time (d/dandt): ")
            if type == "d":
                date = input("Please enter the date you would like to see the bookings for"
                            + " (YYYY-MM-DD): ")
                bookings = wilsonskitchen.bookings.bookings_select_booking_for_date(date)
                for i in range(0, (len(bookings))):
                    print("\nBooking " + str(bookings[i][0]) + " details:"
                          + "\n   Booking Time: " + str(bookings[i][1])
                          + "\n   Booking Date: " + str(bookings[i][2])
                          + "\n   Number of People: " + str(bookings[i][3])
                          + "\n   Table booked: " + str(bookings[i][4])
                          + "\n   Current bill: " + str(bookings[i][5])
                          + "\n   Customer ID: " + str(bookings[i][6]))
            elif type == "dandt":
                date = input("Please enter the date you would like to see the bookings for"
                            + " (YYYY-MM-DD): ")
                time = input("Please enter the time you would like to see the bookings"
                            + " for (HH) 24 hr clock times: ")
                bookings = wilsonskitchen.bookings.bookings_select_booking_for_dateandtime(
                    date, time)
                for i in range(0, (len(bookings))):
                    print("\nBooking " + str(bookings[i][0]) + " details:"
                          + "\n   Booking Time: " + str(bookings[i][1])
                          + "\n   Booking Date: " + str(bookings[i][2])
                          + "\n   Number of People: " + str(bookings[i][3])
                          + "\n   Table booked: " + str(bookings[i][4])
                          + "\n   Current bill: " + str(bookings[i][5])
                          + "\n   Customer ID: " + str(bookings[i][6]))

        elif bookchoice == "5":
            tableid = input("Please enter the Table of the bill you would like: ")
            time = input("Please enter the time of the booking of the bill you would like: ")
            date = input("Please enter the date of the booking of the bill you would like"
                        + " (YYYY-MM-DD): ")
            bill = wilsonskitchen.bookings.bookings_select_booking_bill(tableid, time, date)
            print("The current bill for table " +
                  str(tableid) + " is: £" + str(bill))

        else:
            print("That is not a valid choice, the main menu will now reload:")

    elif choice == "4":  # tables
        print("\nTable Details menu:\n"
              + "   1. Add new table\n"
              + "   2. Delete table\n"
              + "   3. Update table details\n"
              + "   4. Get list of all tables")
        tablechoice = input("Please choose an option from the menu above"
                        + " (E to exit table menu): ")

        if tablechoice == "1":
            print("Please enter the details of the table.")
            NoSeats = input("Please enter the number of seats for this table: ")
            Description = input("Please enter the description for this table: ")
            wilsonskitchen.tables.tables_add_table(NoSeats, Description)
            print("\nThe Table has been added to the database.")

        elif tablechoice == "2":
            tableid = input("Please enter the Table ID of the Table you wish to delete: ")
            check = wilsonskitchen.bookings.bookings_select_booking_fromtableid(tableid)
            if check == None:
                wilsonskitchen.tables.tables_delete_table(tableid)
                print("\nThe Table has been deleted from the database.")
            else:
                print("You cannot delete this table as there are bookings made for it.")

        elif tablechoice == "3":
            oldtableid = input("Please enter the Table ID of the Table you wish to update: ")
            check = wilsonskitchen.bookings.bookings_select_booking_fromtableid(oldtableid)
            if check == None:
                print("Please enter the new details of the table:")
                noseats = input("Number of Seats: ")
                description = input("Description: ")
                wilsonskitchen.tables.tables_update_table(oldtableid, noseats, description)
                print("The details of the table have been updated.")
            else:
                print("You cannot update this table as there are bookings made for it.")

        elif tablechoice == "4":
            tables = wilsonskitchen.tables.print_all_tables()
            for i in range(0, (len(tables))):
                print("\nTable " + str(tables[i][0]) + " details:"
                      + "\n   Number of Seats: " + str(tables[i][1])
                        + "\n   Description: " + str(tables[i][2]))

        else:
            print("That is not a valid choice, the menu will now reload:")

    elif choice == "5":  # orders
        print("\nOrder Details menu:\n"
              + "   1. Add new order\n"
              + "   2. Get all orders\n")
        orderchoice = input("Please choose an option from the menu above"
                        + " (E to exit order menu): ")

        if orderchoice == "1":
            TableID = input("Please enter which table the order is for: ")
            n = int(input("Please enter the number of different items on the order: "))
            wilsonskitchen.productidlist.wipe()
            wilsonskitchen.quantitylist.wipe()
            for i in range(0, n):
                newproductname = input("Please enter the product name: ")
                wilsonskitchen.productidlist.list_add_item(
                    wilsonskitchen.products.products_select_productid(newproductname))
                wilsonskitchen.quantitylist.list_add_item(
                    int(input("Please enter the quantity of the item ordered: ")))
            check = wilsonskitchen.restaurant_make_order(TableID, n)
            if check:
                print("Order has been added to the database.")
            else:
                print("This product is out of stock, please re-enter order"
                    + " excluding this item.")

        elif orderchoice == "2":
            type = input("Would you like to see all orders made by a particular table (t)"
                        + " or a particular date (d): ")
            if type == "t":
                tableid = input("Please enter the table of the orders you would like to see: ")
                orders = wilsonskitchen.orders.orders_select_orders_for_table(tableid)
                for i in range(0, (len(orders))):
                    print("\nOrder " + str(orders[i][0]) + " details:"
                          + "\n   Date and Time: " + str(orders[i][1])
                          + "\n   Total Price: " + str(orders[i][2])
                          + "\n   Table ID: " + str(orders[i][3]))
            elif type == "d":
                chosendate = input("Please enter the date of the orders you would like to see"
                                + " (YYYY-MM-DD): ")
                orders = wilsonskitchen.orders.orders_select_orders_for_date(date)
                for i in range(0, (len(orders))):
                    print("\nOrder " + str(orders[i][0]) + " details:"
                          + "\n   Date and Time: " + str(orders[i][1])
                          + "\n   Total Price: " + str(orders[i][2])
                          + "\n   Table ID: " + str(orders[i][3]))

    elif choice == "6":  # menu/prodcuts
        print("\nMenu Details menu:\n"
              + "   1. Add new product\n"
              + "   2. Delete product\n"
              + "   3. Update product details\n"
              + "   4. Get all products\n"
              + "   5. Print current menu\n"
              + "   6. Check for any out of stock products.")
        menuchoice = input("Please choose an option from the menu above"
                        + " (E to exit this menu): ")

        if menuchoice == "1":
            type = input("Please enter the type of product: ")
            name = input("Please enter the name of the product: ")
            price = input("Please enter the price of the product: ")
            n = int(input("Please enter the number of ingredients needed for this product: "))
            wilsonskitchen.ingredientnameslist.wipe()
            wilsonskitchen.ingredientquantitylist.wipe()
            for i in range(0, n):
                ingredientname = input("Please enter the name of an ingredient"
                                    + " for this product: ")
                check = wilsonskitchen.ingredients.ingredients_select_ingredientid(
                    ingredientname)
                if check == None:
                    print("The Ingredient does not exist on the database,"
                        + " please enter its details: ")
                    ingtype = input("Please enter the type of ingredient: ")
                    StoragePlace = input("Please enter the storage place of the ingredient: ")
                    cost = float(input("Please enter the cost of the ingredient per kilo: "))
                    stock = 0
                    wilsonskitchen.ingredients.ingredients_add_ingredient(
                        ingredientname, ingtype, StoragePlace, cost, stock)
                    print("The Ingredient has been added to the database")
                wilsonskitchen.ingredientnameslist.list_add_item(ingredientname)
                quantity = float(input("Please enter the amount in kilos needed of this"
                                    + " ingredient for the product: "))
                wilsonskitchen.ingredientquantitylist.list_add_item(quantity)
            wilsonskitchen.restaurant_make_product(type, name, price, n)

        elif menuchoice == "2":
            productid = input("Please enter the product id of the product you"
                            + " wish to delete: ")
            wilsonskitchen.products.products_delete_product(productid)
            wilsonskitchen.uses.uses_delete_use(productid)
            print("The product has been deleted from the database")

        elif menuchoice == "3":
            productid = input("Please enter the product id of the product you"
                            + " wish to update: ")
            wilsonskitchen.products.products_delete_product(productid)
            wilsonskitchen.uses.uses_delete_use(productid)
            print("Please enter the new product details: ")
            type = input("Please enter the type of product: ")
            name = input("Please enter the name of the product: ")
            price = input("Please enter the price of the product: ")
            n = int(input("Please enter the number of ingredients needed for this product: "))
            wilsonskitchen.ingredientnameslist.wipe()
            wilsonskitchen.ingredientquantitylist.wipe()
            for i in range(1, n):
                ingredientname = input("Please enter the name of an ingredient"
                                    + " for this product: ")
                wilsonskitchen.ingredientnameslist.list_add_item(ingredientname)
                quantity = float(input("Please enter the amount in kilos needed of this"
                                    + " ingredient for the product: "))
                wilsonskitchen.ingredientquantitylist.list_add_item(quantity)
            wilsonskitchen.restaurant_make_product(type, name, price, n)

        elif menuchoice == "4":
            products = wilsonskitchen.products.products_return_products()
            for i in range(0, (len(products))):
                print("\nProduct " + str(products[i][0]) + " details:"
                      + "\n   Type: " + str(products[i][1])
                        + "\n   Name: " + str(products[i][2])
                        + "\n   Price: " + str(products[i][3])
                        + "\n   Quantity Available: " + str(products[i][4])
                        + "\n   Cost per portion: " + str(products[i][5]))

        elif menuchoice == "5":
            menu = wilsonskitchen.products.products_print_menu()
            starters = menu[0]
            print("\nStarters:")
            for i in range(0, (len(starters))):
                print("\n   " + str(starters[i][2]) + " - " + str(starters[i][3]))
            mains = menu[1]
            print("\nMains:")
            for i in range(0, (len(mains))):
                print("\n   " + str(mains[i][2]) + " - " + str(mains[i][3]))
            sides = menu[2]
            print("\nSides:")
            for i in range(0, (len(sides))):
                print("\n   " + str(sides[i][2]) + " - " + str(sides[i][3]))
            desserts = menu[3]
            print("\nDesserts:")
            for i in range(0, (len(desserts))):
                print("\n   " + str(desserts[i][2]) + " - " + str(desserts[i][3]))

        elif menuchoice == "6":
            outofstock = wilsonskitchen.restaurant_check_outofstock_products()

            ingredients = outofstock[0]
            if ingredients == []:
                print("All of the ingredients are stocked.")
            else:
                print("These are the ingredients that are out of stock:")
                for i in range(0, len(ingredients)):
                    print(ingredients[i])

            products = outofstock[1]
            if products == []:
                print("All of the products are in stock.")
            else:
                print("These are the products that are out of stock:")
                for i in range(0, len(products)):
                    print(products[i])

    elif choice == "7":  # ingredients
        print("\nIngredient Details menu\n"
              + "   1. Add new ingredient\n"
              + "   2. Delete ingredient\n"
              + "   3. Update ingredient\n"
              + "   4. Print list of all ingredients")
        ingredientchoice = input("Please choose an option from the menu above"
                                + " (E to exit ingredient menu): ")

        if ingredientchoice == "1":
            name = input("Please enter the name of the ingredient: ")
            type = input("Please enter the type of ingredient: ")
            StoragePlace = input("Please enter the storage place of the ingredient: ")
            cost = float(input("Please enter the cost of the ingredient per kilo: "))
            stock = 0
            wilsonskitchen.ingredients.ingredients_add_ingredient(
                name, type, StoragePlace, cost, stock)
            print("The Ingredient has been added to the database")

        elif ingredientchoice == "2":
            ingname = input("Please enter the name of the ingredient you wish to delete: ")
            ingid = wilsonskitchen.ingredients.ingredients_select_ingredientid(ingname)[0]
            uses = wilsonskitchen.uses.uses_select_uses_from_ingid(ingid)
            if uses == []:
                wilsonskitchen._ingredients.ingredients_delete_ingredient(ingid)
                print("\nThe Ingredient has been deleted from the database.")
            else:
                check = input("This ingredient is being used for products on the menu,"
                            + " would you like to cancel (c) or delete those products"
                            + " as well (d): ")
                if check == "c":
                    print("The deletion of the ingredient has been cancelled.")
                elif check == "d":
                    wilsonskitchen.restaurant_delete_ingredient_and_products(ingid)
                    print("\nThe Ingredient has been deleted from the database.")

        elif ingredientchoice == "3":
            name = input("Please enter the name of the ingredient you wish to update: ")
            type = input("Please enter the new type: ")
            storageplace = input("Please enter the new storage place: ")
            cost = float(input("Please enter the new cost per kilo: "))
            wilsonskitchen.ingredients.ingredients_update_ingredient(
                name, type, storageplace, cost)
            print("The ingredient has been updated.")

        elif ingredientchoice == "4":
            ingredients = wilsonskitchen.ingredients.ingredients_select_ingredients()
            for i in range(0, len(ingredients)):
                print("\nIngredient " + str(ingredients[i][0]) + " details:"
                      + "\n   Name: " + str(ingredients[i][1])
                        + "\n   Type: " + str(ingredients[i][2])
                        + "\n   Storage Place: " + str(ingredients[i][3])
                        + "\n   Cost per Kilo: " + str(ingredients[i][4]))

    elif choice == "8":  # stock
        print("\nStock Details menu\n"
              + "   1. Add new batch of ingredients\n"
              + "   2. Delete batch of ingredients\n"
              + "   3. Update batch of ingredients\n"
              + "   4. Get run down of all ingredient stock\n"
              + "   5. Delete out of stock batches.")
        stockchoice = input("Please choose an option from the menu above"
                        + " (E to exit stock menu): ")

        if stockchoice == "1":
            ingname = input("Please enter the name of the ingredient: ")
            quantity = int(input("Please enter the quantity of the ingredient in kilos: "))
            expirydate = input("Please enter the expriy date of the batch (YYYY-MM-DD): ")
            wilsonskitchen.restaurant_add_ingredientbatch(ingname, quantity, expirydate)
            print("The Batch has been added to the database.")

        elif stockchoice == "2":
            ingname = input("Please enter the name of the ingredient: ")
            ingid = wilsonskitchen.ingredients.ingredients_select_ingredientid(ingname)[0]
            expirydate = input("Please enter the expriy date of the batch (YYYY-MM-DD): ")
            wilsonskitchen.restaurant_delete_ingredientbatch(ingid, expirydate)
            print("The Batch has been deleted from the database.")

        elif stockchoice == "3":
            ingname = input("Please enter the name of the ingredient: ")
            ingid = wilsonskitchen.ingredients.ingredients_select_ingredientid(ingname)[0]
            expirydate = input("Please enter the expriy date of the batch (YYYY-MM-DD): ")
            wilsonskitchen.restaurant_delete_ingredientbatch(ingid, expirydate)
            print("\nPlease enter below the new details of the ingredient batch: ")
            ingname = input("Please enter the name of the ingredient: ")
            quantity = int(input("Please enter the quantity of the ingredient in kilos: "))
            expirydate = input("Please enter the expriy date of the batch (YYYY-MM-DD): ")
            wilsonskitchen.restaurant_add_ingredientbatch(ingname, quantity, expirydate)
            print("The Batch has been updated.")

        elif stockchoice == "4":
            batches = wilsonskitchen.ingredientbatches.batches_select_all_batches()
            for i in range(0, len(batches)):
                print("\nIngredient Batch " + str(batches[i][0]) + " details:"
                      + "\n   Ingredient ID: " + str(batches[i][1])
                        + "\n   Quantity: " + str(batches[i][2])
                        + "\n   Expiry Date: " + str(batches[i][3]))

        elif stockchoice == "5":
            wilsonskitchen.restaurant_delete_outofdate_ingredients()

    elif choice == "9":  # login
        print("\nLogin Details menu\n"
              + "   1. Add new member of staff account\n"
              + "   2. Delete an account\n"
              + "   3. Update account details\n"
              + "   4. Update staff members account details\n"
              + "   5. Get list of current employees")
        loginchoice = input("Please choose an option from the menu above"
                        + " (E to exit login menu): ")

        if loginchoice == "1":
            if access != 1:
                print("Unfortunately your account does not have access to add a new member.")
            else:
                print("Please enter the details of the new staff member: ")
                email = input("Please enter the staff email: ")
                fname = input("Please enter the Firstname: ")
                sname = input("Please enter the surname: ")
                job = input("Please enter the Job title: ")
                access = int(input("Please enter the access level: "))
                passwordcheck = False
                while passwordcheck == False:
                    password = input("Please enter a secure password: ")
                    password1 = input("Please re-enter your password: ")
                    if password == password1:
                        passwordcheck = True
                    else:
                        print(
                            "Your first and second password entries do not match,"
                            + " please re-enter:")
                newusername = wilsonskitchen.staffmembers.staffmembers_add_member(
                    email, fname, sname, job, access, password)
                print("Your username is " + str(newusername))
                print("The Staff Member has been added to the database.")

        elif loginchoice == "2":
            if access != 1:
                print("Unfortunately your account does not have access to delete a member.")
            else:
                email = input("Please enter the email of the staff member you"
                            + " wish to delete: ")
                wilsonskitchen.staffmembers.staffmembers_delete_member(email)
                print("The staff member has been deleted.")

        elif loginchoice == "3":
            print("Please enter your new details, you cannot change your job title,"
                + " access level or username: ")
            email = input("Please enter your new email: ")
            fname = input("Please enter your new Firstname: ")
            sname = input("Please enter your new surname: ")
            passwordcheck = False
            while passwordcheck == False:
                password = input("Please enter a new secure password: ")
                password1 = input("Please re-enter your new password: ")
                if password == password1:
                    passwordcheck = True
                else:
                    print("Your first and second password entries do not match,"
                        + " please re-enter:")
            wilsonskitchen.staffmembers.staffmembers_update_self(
                username, email, fname, sname, password)
            print("Your details have been updated.")

        elif loginchoice == "4":
            if access != 1:
                print("Unfortunately your account does not have access to update a"
                    + " member's details.")
            else:
                oldemail = input("Please enter the original email of the staff member: ")
                email = input("Please enter the new email: ")
                fname = input("Please enter the new firstname: ")
                sname = input("Please enter the new surname: ")
                job = input("Please enter the new job title: ")
                access = input("Please enter the new access level: ")
                passwordcheck = False
                while passwordcheck == False:
                    password = input("Please enter a new secure password: ")
                    password1 = input("Please re-enter your new password: ")
                    if password == password1:
                        passwordcheck = True
                    else:
                        print("Your first and second password entries do not match,"
                            + " please re-enter:")
                wilsonskitchen.staffmembers.staffmembers_update_member(
                    oldemail, email, fname, sname, job, access, password)
                print("The staff member's details have been updated.")

        elif loginchoice == "5":
            staffmembers = wilsonskitchen.staffmembers.staffmembers_get_all()
            for i in range(0, len(staffmembers)):
                print("\nStaff Member " + str(staffmembers[i][0]) + " details:"
                      + "\n   Email: " + str(staffmembers[i][1])
                        + "\n   Name: " +
                      str(staffmembers[i][2]) + str(staffmembers[i][3])
                        + "\n   Job Title: " + str(staffmembers[i][4])
                        + "\n   Access Level: " + str(staffmembers[i][5])
                        + "\n   Username: " + str(staffmembers[i][6]))

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
    choice = input("Please choose an option from the menu above (E to logout):")

print("You will now be logged out.")
