from restaurantmain import Restaurant

wilsonskitchen = Restaurant()

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
choice = input("Please choose an option from the menu above (E to exit): ")

while choice != "E":

    if choice == "1":#reset
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
            wilsonskitchen.order.reset_order_table()
        check = input("Are you sure you want to reset the Orderproduct table (y/n): ")
        if check == "y":
            wilsonskitchen.orderproduct.reset_orderproduct_table()
        check = input("Are you sure you want to reset the Product table (y/n): ")
        if check == "y":
            wilsonskitchen.product.reset_product_table()
        check = input("Are you sure you want to reset the Use table (y/n): ")
        if check == "y":
            wilsonskitchen.use.reset_use_table()
        check = input("Are you sure you want to reset the Ingredient table (y/n): ")
        if check == "y":
            wilsonskitchen.ingredient.reset_ingredient_table()
        check = input("Are you sure you want to reset the Ingredientbatch table (y/n): ")
        if check == "y":
            wilsonskitchen.ingredientbatch.reset_ingredientbatch_table()
        
    elif choice == "2":#customers
        print("\nCustomer Details menu:\n"
                + "   1. Add new customer\n"
                + "   2. Delete customer\n"
                + "   3. Update customer's details\n"
                + "   4. Get customer's details\n"
                + "   5. Get list of all customers\n")
        custchoice = input("Please choose an option from the menu above (E to exit customer menu):")
        
        if custchoice == "1":
            print("\nPlease enter the details of the new customer:")
            email = input("Email: ")
            fname = input("Firstname: ")
            sname = input("Surname: ")
            contactno = input("Phone number: ")
            wilsonskitchen.customers.customers_add_customer(email, fname, sname, contactno)
            print("\n" + fname, sname, "has been added to the database.")
        
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
            wilsonskitchen.customers.customers_update_customer(newemail, fname, sname, contactno, oldemail)
            print("The Customer's details have been updated.")

        elif custchoice == "4":
            email = input("\nPlease enter the email of the customer: ")
            details = wilsonskitchen.customers.customers_select_customer(email)
            print("\nCustomer details:"
                + "\n   Customer ID: " + str(details[0])
                + "\n   Customer Email: " + str(details[1])
                + "\n   Customer Name: " + str(details[2]) , str(details[3])
                + "\n   Customer Phone number: " + str(details[4]))

        elif custchoice == "5":
            customers = wilsonskitchen.customers.customers_select_customers()
            for i in range(0, (len(customers))):
                print("\nCustomer " + str(customers[i][0]) + "'s details:"
                    + "\n   Customer Email: " + str(customers[i][1])                    
                    + "\n   Customer Name: " + str(customers[i][2]) , str(customers[i][3])
                    + "\n   Customer Phone number: " + str(customers[i][4]))

        else:
            print("That is not a valid choice, the main menu will now reload:")
    
    elif choice == "3":#bookings
        print("\nBooking Details menu:\n"
            + "   1. Add new booking\n"
            + "   2. Delete booking\n"
            + "   3. Update booking details\n"
            + "   4. Get all booking details\n"
            + "   5. Print bill\n")
        bookchoice = input("Please choose an option from the menu above (E to exit booking menu): ")
        
        if bookchoice == "1":
            print("Please enter the details of the new booking:")
            Time = input("Time (HH) - 24hr clock times: ")
            Date = input("Date (YYYY-MM-DD): ")
            nopeople = input("Number of people: ")
            email = input("Email of customer: ")
            custid = wilsonskitchen.customers.customers_select_custid(email)[0]
            if custid == None:
                print("The Customer does not exist on the database, please enter their details: ")
                email = input("Email: ")
                fname = input("Firstname: ")
                sname = input("Surname: ")
                contactno = input("Phone number: ")
                wilsonskitchen.customers.customers_add_customer(email, fname, sname, contactno)
                print("\n" + fname, sname, "has been added to the database.")
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
            print("\nThe Booking has been deleted from the database.")

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
                print("The Customer does not exist on the database, please enter their details: ")
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
            type = input("Please enter whether you would like all the bookings for date or date and time (d/dandt): ")
            if type == "d":
                date = input("Please enter the date you would like to see the bookings for (YYYY-MM-DD): ")
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
                date = input("Please enter the date you would like to see the bookings for (YYYY-MM-DD): ")
                time = input("Please enter the time you would like to see the bookings for (HH) 24 hr clock times: ")
                bookings = wilsonskitchen.bookings.bookings_select_booking_for_dateandtime(date, time)
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
            date = input("Please enter the date of the booking of the bill you would like (YYYY-MM-DD): ")
            bill = wilsonskitchen.bookings.bookings_select_booking_bill(tableid, time, date)
            print("The current bill for table " + str(tableid) + " is: " + bill)

        else:
            print("That is not a valid choice, the main menu will now reload:")

    elif choice == "4":#tables
        print("\nTable Details menu:\n"
            + "   1. Add new table\n"
            + "   2. Delete table\n"
            + "   3. Update table details\n"
            + "   4. Get list of all tables")
        tablechoice = input("Please choose an option from the menu above (E to exit table menu): ")
        
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

    elif choice == "5":#orders
        print("\nOrder Details menu:\n"
            + "   1. Add new order\n"
            + "   2. Get all orders\n")
        orderchoice = input("Please choose an option from the menu above (E to exit order menu): ")
        
        if orderchoice == "1":
            TableID = input("Please enter which table the order is for: ")
            n = int(input("Please enter the number of different items on the order: "))
            wilsonskitchen.productidlist.wipe()
            wilsonskitchen.quantitylist.wipe()
            for i in range(1, n):
                newproductname = input("Please enter the product name: ")
                wilsonskitchen.productidlist.list_add_item(wilsonskitchen.products.products_select_productid(newproductname))
                wilsonskitchen.quantitylist.list_add_item(int(input("Please enter the quantity of the item ordered: ")))
            check = wilsonskitchen.restaurant_make_order(TableID, n)
            if check:
                print("Order has been added to the database.")
            else:
                    print("This product is out of stock, please re-enter order excluding this item.")
            
        elif orderchoice == "2":
            type = input("Would you like to see all orders made by a particular table (t) or a particular date (d): ")
            if type == "t":
                tableid = input("Please enter the table of the orders you would like to see: ")
                orders = wilsonskitchen.orders.orders_select_orders_for_table(tableid)
                for i in range(0, (len(orders))):
                    print("\nOrder " + str(orders[i][0]) + " details:"
                        + "\n   Date and Time: " + str(orders[i][1])
                        + "\n   Total Price: " + str(orders[i][2])
                        + "\n   Table ID: " + str(orders[i][3]))
            elif type == "d":
                chosendate = input("Please enter the date of the orders you would like to see (YYYY-MM-DD): ")
                orders = wilsonskitchen.orders.orders_select_orders_for_date(date)
                for i in range(0, (len(orders))):
                    print("\nOrder " + str(orders[i][0]) + " details:"
                        + "\n   Date and Time: " + str(orders[i][1])
                        + "\n   Total Price: " + str(orders[i][2])
                        + "\n   Table ID: " + str(orders[i][3]))

    elif choice == "6":#menu/prodcuts
        print("\nMenu Details menu:\n"
            + "   1. Add new product\n"
            + "   2. Delete product\n"
            + "   3. Update product details\n"
            + "   4. Get all products\n"
            + "   5. Print current menu")
        menuchoice = input("Please choose an option from the menu above (E to exit this menu): ")

        if menuchoice == "1":
            type = input("Please enter the type of product: ")
            name = input("Please enter the name of the product: ")
            price = input("Please enter the price of the product: ")
            n = int(input("Please enter the number of ingredients needed for this product: "))
            wilsonskitchen.ingredientnameslist.wipe()
            wilsonskitchen.ingredientquantitylist.wipe()
            for i in range(1, n):
                ingredientname = input("Please enter the name of an ingredient for this product: ")
                wilsonskitchen.ingredientnameslist.list_add_item(ingredientname)
                quantity = int(input("Please enter the amount in kilos needed of this ingredient for the product: "))
                wilsonskitchen.ingredientquantitylist.list_add_item(quantity)
            wilsonskitchen.restaurant_make_product(type, name, price, n)

        elif menuchoice == "2":
            productid = input("Please enter the product id of the product you wish to delete: ")
            wilsonskitchen.products.products_delete_product(productid)
            wilsonskitchen.uses.uses_delete_use(productid)
            print("The product has been deleted from the database")

        elif menuchoice == "3":
            productid = input("Please enter the product id of the product you wish to update: ")
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
                ingredientname = input("Please enter the name of an ingredient for this product: ")
                wilsonskitchen.ingredientnameslist.list_add_item(ingredientname)
                quantity = int(input("Please enter the amount in kilos needed of this ingredient for the product: "))
                wilsonskitchen.ingredientquantitylist.list_add_item(quantity)
            wilsonskitchen.restaurant_make_product(type, name, price, n)

        elif menuchoice == "4":
            products = wilsonskitchen.products.products_return_products()
            for i in range(0, (len(products))):
                print("\nProduct " + str(products[i][0]) + " details:"
                        + "\n   Type: " + str(products[i][1])
                        + "\n   Name: " + str(products[i][2])
                        + "\n   Price: " + str(products[i][3])
                        + "\n   Quantity Available: " + str(products[i][4]))

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

            
  

#next to do: choice 6 menu details
#left to update on classes.py: 192-206 in Bookings, 363 onwards in products, ingredients and ingredientbatches

#note for deleting ingredient:
#find all products attatched to ingredient and return list. saying these products must be deleted before an ingredient is deleted.

    #def reduce_product_quantity(self, productid, quantity):
        #sql = "SELECT QuantityAvailable FROM Products WHERE ProductID=?"
        #oldquantity = self.select_dataspecific_fetchone(sql, (productid,))
        #newquantity = oldquantity - quantity
        #sql = "UPDATE Products SET QuantityAvailable=? WHERE ProductID=?"
        #self.update(sql, (newquantity, productid))