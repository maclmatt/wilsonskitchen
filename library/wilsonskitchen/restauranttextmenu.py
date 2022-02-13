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
            bookings.select_booking_bill()
        else:
            print("That is not a valid choice, the main menu will now reload:")