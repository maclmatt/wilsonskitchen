import tkinter as tk
from functools import partial
from restaurantmain import Restaurant
from constants import LOGGER
import sys

wilsonskitchen = Restaurant()

class Login():
    def __init__(self):
        self._attempts = 1
        self._access = None

    @property
    def attempts(self):
        return self._attempts

    @property
    def access(self):
        return self._access

    def new_attempt(self):
        self._attempts += 1

    def set_access(self, useraccess):
        self._access = useraccess

class CustomersMenu():
    def __init__(self, fr_main):
        self.lbl = None
        self.frame = fr_main
    
    def show_add_new_customer(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the new customer: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.emaillbl = tk.Label(self.frame, text = "Email:")
        self.emaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custemail = tk.Entry(self.frame)
        self.custemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.fnamelbl = tk.Label(self.frame, text = "Firstname:")
        self.fnamelbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.customerfname = tk.Entry(self.frame)
        self.customerfname.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.snamelbl = tk.Label(self.frame, text = "Surname:")
        self.snamelbl.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.customersname = tk.Entry(self.frame)
        self.customersname.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.numberlbl = tk.Label(self.frame, text = "Phone number:")
        self.numberlbl.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.custnumber = tk.Entry(self.frame)
        self.custnumber.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        
        self.add_new_customer_button = tk.Button(self.frame, text="Add Customer", command=self.add_new_customer)
        self.add_new_customer_button.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_new_customer(self):
        wilsonskitchen.customers.add_customer(self.custemail.get(), 
                                                self.customerfname.get(), 
                                                self.customersname.get(), 
                                                self.custnumber.get())
        self.lbl = tk.Label(self.frame, text= "This customer has been added.")
        self.lbl.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def show_delete_customer(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the customer you want to delete: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.emaillbl = tk.Label(self.frame, text = "Email:")
        self.emaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custemail = tk.Entry(self.frame)
        self.custemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.delete_customer_button = tk.Button(self.frame, text="Delete Customer", command=self.delete_a_customer)
        self.delete_customer_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def delete_a_customer(self):
        custid = wilsonskitchen.customers.select_custid(self.custemail.get())
        wilsonskitchen.customers.delete_customer(custid)
        self.lbl = tk.Label(self.frame, text= "This customer has been deleted.")
        self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def show_update_customer(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the customer: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.oldemaillbl = tk.Label(self.frame, text = "Old email:")
        self.oldemaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custoldemail = tk.Entry(self.frame)
        self.custoldemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.emaillbl = tk.Label(self.frame, text = "New email:")
        self.emaillbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.custemail = tk.Entry(self.frame)
        self.custemail.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.fnamelbl = tk.Label(self.frame, text = "New firstname:")
        self.fnamelbl.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.customerfname = tk.Entry(self.frame)
        self.customerfname.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.snamelbl = tk.Label(self.frame, text = "New surname:")
        self.snamelbl.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.customersname = tk.Entry(self.frame)
        self.customersname.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

        self.numberlbl = tk.Label(self.frame, text = "New phone number:")
        self.numberlbl.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.custnumber = tk.Entry(self.frame)
        self.custnumber.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
        
        self.update_customer_button = tk.Button(self.frame, text="Update Customer", command=self.update_a_customer)
        self.update_customer_button.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def update_a_customer(self):
        wilsonskitchen.customers.update_customer(self.custemail.get(),
                                                self.customerfname.get(),
                                                self.customersname.get(),
                                                self.custnumber.get(),
                                                self.custoldemail.get())
        self.lbl = tk.Label(self.frame, text= "This customer has been updated.")
        self.lbl.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def see_customer(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 250)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the customer: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.emaillbl = tk.Label(self.frame, text = "Email:")
        self.emaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custemail = tk.Entry(self.frame)
        self.custemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.see_customer_button = tk.Button(self.frame, text="See Customer", command=self.see_customers)
        self.see_customer_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def see_customers(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")
        customers = wilsonskitchen.customers.select_customers()
        for i in range(0, (len(customers))):
            self.lbl = tk.Label(self.frame, text= f"Customer {customers[i][0]}'s details:"
                                                + f"\nCustomer Email: {customers[i][1]}"
                                                + f"\nCustomer Name: {customers[i][2]} {customers[i][3]}"
                                                + f"\nPhone number: {customers[i][4]}")
            self.lbl.grid(row=i, column=0, columnspan=2, sticky= "ew", padx=10, pady=10)

class BookingsMenu():
    def __init__(self, fr_main):
        self.lbl = None
        self.frame = fr_main

    def show_add_booking(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the new booking: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.timelbl = tk.Label(self.frame, text = "Time:")
        self.timelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.time = tk.Entry(self.frame)
        self.time.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.datelbl = tk.Label(self.frame, text = "Date:")
        self.datelbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.date = tk.Entry(self.frame)
        self.date.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.peoplelbl = tk.Label(self.frame, text = "Number of People:")
        self.peoplelbl.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.people = tk.Entry(self.frame)
        self.people.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.emaillbl = tk.Label(self.frame, text = "Email:")
        self.emaillbl.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.email = tk.Entry(self.frame)
        self.email.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        
        self.add_new_booking_button = tk.Button(self.frame, text="Add Booking", command=self.add_new_booking)
        self.add_new_booking_button.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_new_booking(self):
        # selects cust ID
        custid = wilsonskitchen.customers.select_custid(self.email.get())
        if custid == None:
            self.lbl = tk.Label(self.frame, text="This customer needs to be added\nbefore a booking can be made.")
            self.lbl.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            return None
        custid = custid[0]
        # makes booking
        booked = wilsonskitchen.make_booking(self.time.get(),
                                            self.date.get(),
                                            self.people.get(),
                                            custid)
        if booked:
            self.lbl = tk.Label(self.frame, text= "This booking has been added.")
            self.lbl.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            LOGGER.info("The Booking has been added to the database.")
        else:
            self.lbl = tk.Label(self.frame, text= "There are no tables available for this time and date")
            self.lbl.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            LOGGER.info("Booking unable to be added")

    def show_delete_booking(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the booking you want to delete: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.emaillbl = tk.Label(self.frame, text = "Email:")
        self.emaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custemail = tk.Entry(self.frame)
        self.custemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.timelbl = tk.Label(self.frame, text = "Time:")
        self.timelbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.time = tk.Entry(self.frame)
        self.time.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.datelbl = tk.Label(self.frame, text = "Date:")
        self.datelbl.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.date = tk.Entry(self.frame)
        self.date.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.delete_customer_button = tk.Button(self.frame, text="Delete Customer", command=self.delete_a_booking)
        self.delete_customer_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def delete_a_booking(self):
        wilsonskitchen.delete_booking(self.custemail.get(),
                                    self.time.get(),
                                    self.date.get())
        self.lbl = tk.Label(self.frame, text= "This booking has been deleted.")
        self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        LOGGER.info("Booking at %s %s has been deleted.", self.time.get(), self.date.get())

    def show_update_booking(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the booking: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.oldemaillbl = tk.Label(self.frame, text = "Old email:")
        self.oldemaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custoldemail = tk.Entry(self.frame)
        self.custoldemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.oldtimelbl = tk.Label(self.frame, text = "Time:")
        self.oldtimelbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.oldtime = tk.Entry(self.frame)
        self.oldtime.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.olddatelbl = tk.Label(self.frame, text = "Date:")
        self.olddatelbl.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.olddate = tk.Entry(self.frame)
        self.olddate.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.lbl = tk.Label(self.frame, text= "Please enter the new details of the booking: ")
        self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.timelbl = tk.Label(self.frame, text = "Time:")
        self.timelbl.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.time = tk.Entry(self.frame)
        self.time.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        self.datelbl = tk.Label(self.frame, text = "Date:")
        self.datelbl.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        self.date = tk.Entry(self.frame)
        self.date.grid(row=6, column=1, sticky="ew", padx=5, pady=5)

        self.peoplelbl = tk.Label(self.frame, text = "Time:")
        self.peoplelbl.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
        self.people = tk.Entry(self.frame)
        self.people.grid(row=7, column=1, sticky="ew", padx=5, pady=5)

        self.emaillbl = tk.Label(self.frame, text = "Date:")
        self.emaillbl.grid(row=8, column=0, sticky="ew", padx=5, pady=5)
        self.email = tk.Entry(self.frame)
        self.email.grid(row=8, column=1, sticky="ew", padx=5, pady=5)

        self.update_booking_button = tk.Button(self.frame, text="Update Booking", command=self.update_a_booking)
        self.update_booking_button.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def update_a_booking(self):
        wilsonskitchen.delete_booking(self.custoldemail.get(),
                                    self.oldtime.get(),
                                    self.olddate.get())
        custidtuple = wilsonskitchen.customers.select_custid(self.email.get())
        if custidtuple == None:
            self.lbl = tk.Label(self.frame, text="This customer needs to be added\nbefore a booking can be made.")
            self.lbl.grid(row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            return None
        custid = custidtuple[0]
        booked = wilsonskitchen.make_booking(self.time.get(),
                                            self.date.get(),
                                            self.people.get(),
                                            custid)
        if booked:
            self.lbl = tk.Label(self.frame, text= "This booking has been updated.")
            self.lbl.grid(row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            LOGGER.info("The Booking has been added to the database.")
        else:
            self.lbl = tk.Label(self.frame, text= "There are no tables available for this time and date")
            self.lbl.grid(row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            LOGGER.info("Booking unable to be added")

    def show_see_bookings(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 250)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please add the date of the bookings you would like to see.")
        self.lbl.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.datelbl = tk.Label(self.frame, text = "Date:")
        self.datelbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.date = tk.Entry(self.frame)
        self.date.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.see_bookings_btn = tk.Button(self.frame,
                                        text="See Bookings",
                                        command=self.see_bookings)
        self.see_bookings_btn.grid(row=3,
                                column=0,
                                columnspan=2,
                                sticky="ew",
                                padx=10,
                                pady=10)

    def see_bookings(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 250)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame,
                            text=f"Bookings for the date {self.date.get()}:")
        self.lbl.grid(row=0,
                    column=0,
                    columnspan=2,
                    sticky="ew",
                    padx=5,
                    pady=5)
        bookings = wilsonskitchen.bookings.select_bookings_for_date(self.date.get())
        for i in range(0, (len(bookings))):
            self.lbl = tk.Label(self.frame, text= f"Booking {bookings[i][0]}'s details:"
                                                + f"\nTime: {bookings[i][1]}"
                                                + f"\nDate: {bookings[i][2]}"
                                                + f"\nNumber of People: {bookings[i][3]}"
                                                + f"\nTable booked: {bookings[i][4]}"
                                                + f"\nCurrent bill: {bookings[i][5]}"
                                                + f"\nCustomer ID: {bookings[i][6]}")
            self.lbl.grid(row=i, column=0, columnspan=2, sticky= "ew", padx=10, pady=10)

    def show_see_bill(self):
        self.frame = tk.Frame(window_main,
                            bg = "lightsteelblue",
                            width = 250)
        self.frame.grid(row=0,
                        column=2,
                        sticky="nsew")

        self.lbl = tk.Label(self.frame,
                            text="Please enter the details of the booking")
        self.lbl.grid(row=0,
                    column=0,
                    columnspan=2,
                    sticky="ew",
                    padx=5,
                    pady=5)

        self.tablelbl = tk.Label(self.frame, text = "Table ID:")
        self.tablelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.table = tk.Entry(self.frame)
        self.table.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.timelbl = tk.Label(self.frame, text = "Time:")
        self.timelbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.time = tk.Entry(self.frame)
        self.time.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.datelbl = tk.Label(self.frame, text = "Date:")
        self.datelbl.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.date = tk.Entry(self.frame)
        self.date.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.see_booking_btn = tk.Button(self.frame,
                                        text="See Bill",
                                        command=self.see_bill)
        self.see_booking_btn.grid(row=4,
                                column=0,
                                columnspan=2,
                                sticky="ew",
                                padx=10,
                                pady=10)

    def see_bill(self):
        bill = wilsonskitchen.bookings.select_booking_bill(self.table.get(),
                                                        self.time.get(),
                                                        self.date.get())
        
        self.lbl = tk.Label(self.frame,
                            text=f"Bill of the booking is {bill}")
        self.lbl.grid(row=5,
                    column=0,
                    columnspan=2,
                    sticky="ew",
                    padx=5,
                    pady=5)
        
class TablesMenu():
    def __init__(self, fr_main):
        self.lbl = None
        self.frame = fr_main

    def show_add_table(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the new table: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.peoplelbl = tk.Label(self.frame, text = "Number of seats:")
        self.peoplelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.people = tk.Entry(self.frame)
        self.people.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Add Table", command=self.add_new_table)
        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_new_table(self):
        wilsonskitchen.tables.add_table(self.people.get())
        self.lbl = tk.Label(self.frame, text= "This table has been added.")
        self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        LOGGER.info("Table has been added to the database.")

    def show_delete_table(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the table you want to delete: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.tablelbl = tk.Label(self.frame, text = "Table ID:")
        self.tablelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.table = tk.Entry(self.frame)
        self.table.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Delete Table", command=self.delete_a_table)
        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def delete_a_table(self):
        check = wilsonskitchen.bookings.select_bookings_fromtableid(self.table.get())
        if check == None:
            # deletes table
            wilsonskitchen.tables.delete_table(self.table.get())
            self.lbl = tk.Label(self.frame, text= "The Table has been deleted from the database.")
            self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            LOGGER.info("Table %s has been deleted.", self.table.get())
        else:
            self.lbl = tk.Label(self.frame, text= "You cannot delete this table as there are bookings made for it.")
            self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            LOGGER.info("Table %s coudn't be deleted as there are bookings made for it.", self.table.get())

    def show_update_table(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the table: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.tablelbl = tk.Label(self.frame, text = "Table ID:")
        self.tablelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.table = tk.Entry(self.frame)
        self.table.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.peoplelbl = tk.Label(self.frame, text = "New number of seats:")
        self.peoplelbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.people = tk.Entry(self.frame)
        self.people.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Update Table", command=self.update_a_table)
        self.btn.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def update_a_table(self):
        # checks if bookings are made to the table
        check = wilsonskitchen.bookings.select_bookings_fromtableid(self.table.get())
        if check == None:
            # updates table details
            wilsonskitchen.tables.update_table(self.table.get(), self.people.get())
            self.lbl = tk.Label(self.frame, text= "The details of the table have been updated.")
            self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            LOGGER.info("Details of table %s has been updated", self.table.get())
        else:
            self.lbl = tk.Label(self.frame, text= "You cannot update this table as there are bookings made for it.")
            self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            LOGGER.info("Table %s coudn't be updated, due to bookings made for it.", self.table.get())

    def see_tables(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")
        tables = wilsonskitchen.tables.print_all_tables()
        for i in range(0, (len(tables))):
            self.lbl = tk.Label(self.frame, text= f"Table {tables[i][0]}'s details:"
                                                + f"\nNumber of seats: {tables[i][1]}")
            self.lbl.grid(row=i, column=0, columnspan=2, sticky= "ew", padx=10, pady=10)

class MenuandOrdersMenu():
    def __init__(self, fr_main):
        self.count = 0
        self.lbl = None
        self.frame = fr_main

    def show_add_order(self):
        wilsonskitchen.productidlist.wipe()
        wilsonskitchen.quantitylist.wipe()

        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of new order:")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.tablelbl = tk.Label(self.frame, text = "Table ID:")
        self.tablelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.table = tk.Entry(self.frame)
        self.table.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.numberlbl = tk.Label(self.frame, text = "Number of different items:")
        self.numberlbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.number = tk.Entry(self.frame)
        self.number.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Enter items", command=self.enter_items_for_order)
        self.btn.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def enter_items_for_order(self):
        for i in range(0, int(self.number.get())):
            self.lbl = tk.Label(self.frame, text= "Please enter an item for the order:")
            self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

            self.productlbl = tk.Label(self.frame, text = "Product name:")
            self.productlbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
            self.product = tk.Entry(self.frame)
            self.product.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

            self.quantitylbl = tk.Label(self.frame, text = "Quantity:")
            self.quantitylbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
            self.quantity = tk.Entry(self.frame)
            self.quantity.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

            self.btn = tk.Button(self.frame, text="Add item/s to order", command=self.add_item_to_order)
            self.btn.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        self.btn = tk.Button(self.frame, text="Done", command=self.add_a_order)
        self.btn.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_item_to_order(self):
        wilsonskitchen.productidlist.add_item(
            wilsonskitchen.products.select_productid(self.product.get()))
        wilsonskitchen.quantitylist.add_item(int(self.quantity.get()))

    def add_a_order(self):
        check = wilsonskitchen.make_order(int(self.table.get()), int(self.number.get()))
        if check:
            self.btn.destroy()
            self.lbl = tk.Label(self.frame, text= "This order has been added.")
            self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            LOGGER.info("Order has been added to the database.")
        else:
            self.btn.destroy()
            self.lbl = tk.Label(self.frame, text= "One of the items is out of stock, please check out of stock items.")
            self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            LOGGER.info("Order unable to be added, possibly due to out of stock item.")

    def show_see_orders(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the orders you wish to see:")
        self.lbl.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.datelbl = tk.Label(self.frame, text = "Date:")
        self.datelbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.date = tk.Entry(self.frame)
        self.date.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.see_bookings_btn = tk.Button(self.frame,
                                        text="See Orders",
                                        command=self.see_orders)
        self.see_bookings_btn.grid(row=3,
                                column=0,
                                columnspan=2,
                                sticky="ew",
                                padx=10,
                                pady=10)

    def see_orders(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")
        orders = wilsonskitchen.orders.select_orders_for_date(self.date.get())
        for i in range(0, (len(orders))):
            self.lbl = tk.Label(self.frame, text= f"Order {orders[i][0]}'s details:"
                                                + f"\nDate and Time: {orders[i][1]} {orders[i][2]}"
                                                + f"\nTotal Price: {orders[i][3]}"
                                                + f"\nTable ID: {orders[i][4]}")
            self.lbl.grid(row=i, column=0, columnspan=2, sticky= "ew", padx=10, pady=10)

    def show_add_product(self):
        wilsonskitchen.ingredientnameslist.wipe()
        wilsonskitchen.ingredientquantitylist.wipe()

        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the new product: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.typelbl = tk.Label(self.frame, text = "Type:")
        self.typelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.type = tk.Entry(self.frame)
        self.type.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.namelbl = tk.Label(self.frame, text = "Name:")
        self.namelbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.name = tk.Entry(self.frame)
        self.name.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.pricelbl = tk.Label(self.frame, text = "Price:")
        self.pricelbl.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.price = tk.Entry(self.frame)
        self.price.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.numberlbl = tk.Label(self.frame, text = "Number of ingredients:")
        self.numberlbl.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.number = tk.Entry(self.frame)
        self.number.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Enter ingredients", command=self.enter_ingredients)
        self.btn.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def enter_ingredients(self):
        for i in range(0, int(self.number.get())):
            self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
            self.frame.grid(row=0, column=2, sticky="nsew")

            self.lbl = tk.Label(self.frame, text= "Please enter an item for the order:")
            self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

            self.ingredientlbl = tk.Label(self.frame, text = "Ingredient name:")
            self.ingredientlbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
            self.ingredient = tk.Entry(self.frame)
            self.ingredient.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

            self.quantitylbl = tk.Label(self.frame, text = "Quantity:")
            self.quantitylbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
            self.quantity = tk.Entry(self.frame)
            self.quantity.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
            
            self.btn = tk.Button(self.frame, text="Add ingredient to product", command=self.add_ing_to_product)
            self.btn.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            
        self.btn = tk.Button(self.frame, text="Done", command=self.add_a_product)
        self.btn.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_ing_to_product(self):
        check = wilsonskitchen.ingredients.select_ingredientid(self.ingredient.get())
        if check == None:
            self.lbl = tk.Label(self.frame, text= "This ingredient does not exist.")
            self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
            self.lbl.tkraise()
        else:
            wilsonskitchen.ingredientnameslist.add_item(self.ingredient.get())
            wilsonskitchen.ingredientquantitylist.add_item(float(self.quantity.get()))

    def add_a_product(self):
        wilsonskitchen.make_product(self.type.get(), self.name.get(), float(self.price.get()), int(self.number.get()))
        self.lbl = tk.Label(self.frame, text= "The Product has been added to the database.")
        self.lbl.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        LOGGER.info("Product %s has been added.", self.name.get())

    def show_delete_product(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the product you want to delete: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.idlbl = tk.Label(self.frame, text = "Product ID:")
        self.idlbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.id = tk.Entry(self.frame)
        self.id.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Delete Table", command=self.delete_a_product)
        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def delete_a_product(self):
        # deletes product
        wilsonskitchen.products.delete_product(self.id.get())
        # deletes all uses linked to product
        wilsonskitchen.uses.delete_use(self.id.get())
        self.lbl = tk.Label(self.frame, text= "This product has been deleted.")
        self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        LOGGER.info("Product %s has been deleted.", self.id.get())

    def show_update_product(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the product: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.idlbl = tk.Label(self.frame, text = "Product ID:")
        self.idlbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.id = tk.Entry(self.frame)
        self.id.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.lbl = tk.Label(self.frame, text= "Please enter the new details of the product: ")
        self.lbl.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.typelbl = tk.Label(self.frame, text = "Type:")
        self.typelbl.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.type = tk.Entry(self.frame)
        self.type.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.namelbl = tk.Label(self.frame, text = "Name:")
        self.namelbl.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.name = tk.Entry(self.frame)
        self.name.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

        self.pricelbl = tk.Label(self.frame, text = "Price:")
        self.pricelbl.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.price = tk.Entry(self.frame)
        self.price.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        self.numberlbl = tk.Label(self.frame, text = "Number of ingredients:")
        self.numberlbl.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        self.number = tk.Entry(self.frame)
        self.number.grid(row=6, column=1, sticky="ew", padx=5, pady=5)

        self.update_booking_button = tk.Button(self.frame, text="Update product", command=self.update_a_product)
        self.update_booking_button.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def update_a_product(self):
        # deletes product
        wilsonskitchen.products.delete_product(self.id.get())
        # deletes all uses linked to product
        wilsonskitchen.uses.delete_use(self.id.get())
        # empties ingredientname list and ingredientquantity
        wilsonskitchen.ingredientnameslist.wipe()
        wilsonskitchen.ingredientquantitylist.wipe()
        self.enter_ingredients()

    def see_products(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")
        products = wilsonskitchen.products.return_products()
        for i in range(0, (len(products))):
            self.lbl = tk.Label(self.frame, text= f"Product {products[i][0]} details:"
                                                + f"\nType: {products[i][1]}"
                                                + f"\nName: {products[i][2]}"
                                                + f"\nPrice: {products[i][3]}"
                                                + f"\nQuantity Available: {products[i][4]}"
                                                + f"\nCost per portion: {products[i][5]}")
            self.lbl.grid(row=i, column=0, columnspan=2, sticky= "ew", padx=10, pady=10)

    def see_menu(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")
        # selects all products on the menu, grouped by type
        menu = wilsonskitchen.products.print_menu()
        
        starters = menu[0]
        self.lbl = tk.Label(self.frame, text= "Starters:")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        textprod = ""
        for i in range(0, len(starters)):
            textprod = textprod + "\n" + starters[i][2] + " - " + str(starters[i][3])
        self.lbl = tk.Label(self.frame, text=textprod + "\n")
        self.lbl.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        mains = menu[1]
        self.lbl = tk.Label(self.frame, text= "Mains:")
        self.lbl.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        textprod = ""
        for i in range(0, len(mains)):
            textprod = textprod + "\n" + mains[i][2] + " - " + str(mains[i][3])
        self.lbl = tk.Label(self.frame, text=textprod + "\n")
        self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        sides = menu[2]
        self.lbl = tk.Label(self.frame, text= "Sides:")
        self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        textprod = ""
        for i in range(0, len(sides)):
            textprod = textprod + "\n" + sides[i][2] + " - " + str(sides[i][3])
        self.lbl = tk.Label(self.frame, text=textprod + "\n")
        self.lbl.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        desserts = menu[3]
        self.lbl = tk.Label(self.frame, text= "Desserts:")
        self.lbl.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        textprod = ""
        for i in range(0, len(desserts)):
            textprod = textprod + "\n" + desserts[i][2] + " - " + str(desserts[i][3])
        self.lbl = tk.Label(self.frame, text=textprod + "\n")
        self.lbl.grid(row=7, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        LOGGER.info("Products in form of menu have been outputted.")
        
    def check_out_of_stock(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        # gets list of ingredients to be ordered and out of stock products
        outofstock = wilsonskitchen.check_outofstock_products()

        ingredients = outofstock[0]
        if ingredients == []:
            self.lbl = tk.Label(self.frame, text= "All of the ingredients are stocked.")
            self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        else:
            self.lbl = tk.Label(self.frame, text= "These are out of stock ingredients:")
            self.lbl.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
            texting = ""
            for i in range(0, len(ingredients)):
                texting = texting + ingredients[i]
            self.lbl = tk.Label(self.frame, text=texting + "\n")
            self.lbl.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        LOGGER.info("Out of stock ingredients have been outputted.")

        products = outofstock[1]
        if products == []:
            self.lbl = tk.Label(self.frame, text= "All of the products are in stock.")
            self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        else:
            self.lbl = tk.Label(self.frame, text= "These are out of stock products:")
            self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
            textprod = ""
            for i in range(0, len(ingredients)):
                textprod = textprod + products[i]
            self.lbl = tk.Label(self.frame, text=textprod + "\n")
            self.lbl.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        LOGGER.info("Out of stock products have been outputted.")

class IngredientsMenu():
    def __init__(self, fr_main):
        self.count = 0
        self.lbl = None
        self.frame = fr_main

    def show_add_ingredient(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the new ingredient: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.namelbl = tk.Label(self.frame, text = "Name:")
        self.namelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.name = tk.Entry(self.frame)
        self.name.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.typelbl = tk.Label(self.frame, text = "Type:")
        self.typelbl.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.type = tk.Entry(self.frame)
        self.type.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.placelbl = tk.Label(self.frame, text = "Storage Place:")
        self.placelbl.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.place = tk.Entry(self.frame)
        self.place.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.costlbl = tk.Label(self.frame, text = "Cost:")
        self.costlbl.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.cost = tk.Entry(self.frame)
        self.cost.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Add Ingredient", command=self.add_a_ingredient)
        self.btn.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_a_ingredient(self):
        wilsonskitchen.ingredients.add_ingredient(self.name.get(),
                                                  self.type.get(),
                                                  self.place.get(),
                                                  self.cost.get(),
                                                  0)
        self.lbl = tk.Label(self.frame, text= "This ingredient has been added.")
        self.lbl.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        LOGGER.info("The ingredient %s has been added", self.name.get())

    def show_delete_ingredient(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the table you want to delete: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.tablelbl = tk.Label(self.frame, text = "Table ID:")
        self.tablelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.table = tk.Entry(self.frame)
        self.table.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Delete Table", command=self.delete_a_table)
        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def delete_a_ingredient(self):
        wilsonskitchen.delete_booking(self.custemail.get(),
                                    self.time.get(),
                                    self.date.get())
        self.lbl = tk.Label(self.frame, text= "This booking has been deleted.")
        self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        LOGGER.info("Booking at %s %s has been deleted.", self.time.get(), self.date.get())

    def show_update_ingredient(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the booking: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.oldemaillbl = tk.Label(self.frame, text = "Old email:")
        self.oldemaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custoldemail = tk.Entry(self.frame)
        self.custoldemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.lbl = tk.Label(self.frame, text= "Please enter the new details of the booking: ")
        self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.timelbl = tk.Label(self.frame, text = "Time:")
        self.timelbl.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.time = tk.Entry(self.frame)
        self.time.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        self.datelbl = tk.Label(self.frame, text = "Date:")
        self.datelbl.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        self.date = tk.Entry(self.frame)
        self.date.grid(row=6, column=1, sticky="ew", padx=5, pady=5)

        self.update_booking_button = tk.Button(self.frame, text="Update Booking", command=self.update_a_booking)
        self.update_booking_button.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def update_a_ingredient(self):
        wilsonskitchen.customers.update_customer(self.custemail.get(),
                                                self.customerfname.get(),
                                                self.customersname.get(),
                                                self.custnumber.get(),
                                                self.custoldemail.get())
        self.lbl = tk.Label(self.frame, text= "This customer has been updated.")
        self.lbl.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def see_ingredients(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")
        tables = wilsonskitchen.tables.print_all_tables()
        for i in range(0, (len(tables))):
            self.lbl = tk.Label(self.frame, text= f"Customer {tables[i][0]}'s details:"
                                                + f"\nNumber of seats: {tables[i][1]}")
            self.lbl.grid(row=i, column=0, columnspan=2, sticky= "ew", padx=10, pady=10)

    def show_add_batch(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the new table: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.peoplelbl = tk.Label(self.frame, text = "Number of seats:")
        self.peoplelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.people = tk.Entry(self.frame)
        self.people.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Add Table", command=self.add_new_table)
        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_a_batch(self):
        wilsonskitchen.tables.add_table(self.people.get())
        self.lbl = tk.Label(self.frame, text= "This table has been added.")
        self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        LOGGER.info("Table has been added to the database.")

    def show_delete_batch(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the table you want to delete: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.tablelbl = tk.Label(self.frame, text = "Table ID:")
        self.tablelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.table = tk.Entry(self.frame)
        self.table.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Delete Table", command=self.delete_a_table)
        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def delete_a_batch(self):
        wilsonskitchen.delete_booking(self.custemail.get(),
                                    self.time.get(),
                                    self.date.get())
        self.lbl = tk.Label(self.frame, text= "This booking has been deleted.")
        self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        LOGGER.info("Booking at %s %s has been deleted.", self.time.get(), self.date.get())

    def show_update_batch(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the booking: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.oldemaillbl = tk.Label(self.frame, text = "Old email:")
        self.oldemaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custoldemail = tk.Entry(self.frame)
        self.custoldemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.lbl = tk.Label(self.frame, text= "Please enter the new details of the booking: ")
        self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.timelbl = tk.Label(self.frame, text = "Time:")
        self.timelbl.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.time = tk.Entry(self.frame)
        self.time.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        self.datelbl = tk.Label(self.frame, text = "Date:")
        self.datelbl.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        self.date = tk.Entry(self.frame)
        self.date.grid(row=6, column=1, sticky="ew", padx=5, pady=5)

        self.update_booking_button = tk.Button(self.frame, text="Update Booking", command=self.update_a_booking)
        self.update_booking_button.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def update_a_batch(self):
        wilsonskitchen.customers.update_customer(self.custemail.get(),
                                                self.customerfname.get(),
                                                self.customersname.get(),
                                                self.custnumber.get(),
                                                self.custoldemail.get())
        self.lbl = tk.Label(self.frame, text= "This customer has been updated.")
        self.lbl.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def see_batches(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")
        tables = wilsonskitchen.tables.print_all_tables()
        for i in range(0, (len(tables))):
            self.lbl = tk.Label(self.frame, text= f"Customer {tables[i][0]}'s details:"
                                                + f"\nNumber of seats: {tables[i][1]}")
            self.lbl.grid(row=i, column=0, columnspan=2, sticky= "ew", padx=10, pady=10)

    def show_delete_expired(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

    def delete_expired(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")
class StaffMenu():
    def __init__(self, fr_main):
        self.count = 0
        self.lbl = None
        self.frame = fr_main

    def show_add_member(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the new table: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.peoplelbl = tk.Label(self.frame, text = "Number of seats:")
        self.peoplelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.people = tk.Entry(self.frame)
        self.people.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Add Table", command=self.add_new_table)
        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_a_member(self):
        wilsonskitchen.tables.add_table(self.people.get())
        self.lbl = tk.Label(self.frame, text= "This table has been added.")
        self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        LOGGER.info("Table has been added to the database.")

    def show_delete_member(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the table you want to delete: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.tablelbl = tk.Label(self.frame, text = "Table ID:")
        self.tablelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.table = tk.Entry(self.frame)
        self.table.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.btn = tk.Button(self.frame, text="Delete Table", command=self.delete_a_table)
        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def delete_a_member(self):
        wilsonskitchen.delete_booking(self.custemail.get(),
                                    self.time.get(),
                                    self.date.get())
        self.lbl = tk.Label(self.frame, text= "This booking has been deleted.")
        self.lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        LOGGER.info("Booking at %s %s has been deleted.", self.time.get(), self.date.get())

    def show_update_account(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the booking: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.oldemaillbl = tk.Label(self.frame, text = "Old email:")
        self.oldemaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custoldemail = tk.Entry(self.frame)
        self.custoldemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.lbl = tk.Label(self.frame, text= "Please enter the new details of the booking: ")
        self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.timelbl = tk.Label(self.frame, text = "Time:")
        self.timelbl.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.time = tk.Entry(self.frame)
        self.time.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        self.datelbl = tk.Label(self.frame, text = "Date:")
        self.datelbl.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        self.date = tk.Entry(self.frame)
        self.date.grid(row=6, column=1, sticky="ew", padx=5, pady=5)

        self.update_booking_button = tk.Button(self.frame, text="Update Booking", command=self.update_a_booking)
        self.update_booking_button.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def update_account(self):
        wilsonskitchen.customers.update_customer(self.custemail.get(),
                                                self.customerfname.get(),
                                                self.customersname.get(),
                                                self.custnumber.get(),
                                                self.custoldemail.get())
        self.lbl = tk.Label(self.frame, text= "This customer has been updated.")
        self.lbl.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def show_update_member(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.lbl = tk.Label(self.frame, text= "Please enter the details of the booking: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.oldemaillbl = tk.Label(self.frame, text = "Old email:")
        self.oldemaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custoldemail = tk.Entry(self.frame)
        self.custoldemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.lbl = tk.Label(self.frame, text= "Please enter the new details of the booking: ")
        self.lbl.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.timelbl = tk.Label(self.frame, text = "Time:")
        self.timelbl.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.time = tk.Entry(self.frame)
        self.time.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        self.datelbl = tk.Label(self.frame, text = "Date:")
        self.datelbl.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        self.date = tk.Entry(self.frame)
        self.date.grid(row=6, column=1, sticky="ew", padx=5, pady=5)

        self.update_booking_button = tk.Button(self.frame, text="Update Booking", command=self.update_a_booking)
        self.update_booking_button.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def update_member(self):
        wilsonskitchen.customers.update_customer(self.custemail.get(),
                                                self.customerfname.get(),
                                                self.customersname.get(),
                                                self.custnumber.get(),
                                                self.custoldemail.get())
        self.lbl = tk.Label(self.frame, text= "This customer has been updated.")
        self.lbl.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def see_employees(self):
        self.frame = tk.Frame(window_main, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")
        tables = wilsonskitchen.tables.print_all_tables()
        for i in range(0, (len(tables))):
            self.lbl = tk.Label(self.frame, text= f"Customer {tables[i][0]}'s details:"
                                                + f"\nNumber of seats: {tables[i][1]}")
            self.lbl.grid(row=i, column=0, columnspan=2, sticky= "ew", padx=10, pady=10)


def loginfunc(username_lbl, password_lbl):
    status  = wilsonskitchen.staffmembers.check_login(username_lbl.get(), password_lbl.get())
    attempts = userlogin.attempts
    if status[0] == True:
        LOGGER.info("%s has logged in.", username_lbl.get())
        userlogin.set_access(status[1])
        window_login.destroy()
    elif attempts >= 3:
        # if invalid login details are entered 3 times:
            # exits user
        frame_login = tk.Frame(window_login, bg="LightSteelBlue")
        frame_login.grid(row=0, column=0, sticky="nsew")
        lbl = tk.Label(frame_login,
                       bg="AliceBlue",
                       font=("lucida 20 bold italic", 15),
                       text="You have entered the wrong"
                            + "\ndetails 3 times so will now be"
                            + "\nlocked out")
        lbl.grid(row=0, column=0, padx=20, pady=20)
        window_login.after(3000, sys.exit)
    else:
        userlogin.new_attempt()
        
        if status[1] == "neither":
            frame_login = tk.Frame(window_login, bg="LightSteelBlue")
            frame_login.grid(row=0, column=0, sticky="nsew")

            lbl = tk.Label(frame_login, bg="AliceBlue", text="You have entered incorrect details.")
            lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        else:
            frame_login = tk.Frame(window_login, bg="LightSteelBlue")
            frame_login.grid(row=0, column=0, sticky="nsew")

            lbl = tk.Label(frame_login, bg="AliceBlue", text="You have entered the incorrect password.")
            lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        lbl = tk.Label(frame_login, bg="AliceBlue", text="Please re-enter your details:")
        lbl.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        username_lbl = tk.Label(frame_login, bg="AliceBlue", text="Username:")
        username_lbl.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        username_lbl = tk.Entry(frame_login)
        username_lbl.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

        password_lbl = tk.Label(frame_login, bg="AliceBlue", text="Password:")
        password_lbl.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
        password_lbl = tk.Entry(frame_login)
        password_lbl.grid(row=3, column=1, sticky="ew", padx=10, pady=10)

        login_btn = tk.Button(frame_login, bg="AliceBlue", text="Login", command=partial(loginfunc, username_lbl, password_lbl))
        login_btn.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)


def open_customers_menu():
    fr_submenu = tk.Frame(window_main, bg = "steelblue", width = 200)
    fr_main = tk.Frame(window_main, bg = "lightsteelblue", width=325)
    custmenu = CustomersMenu(fr_main)
    
    btn_add_customer = tk.Button(fr_submenu, text="Add new customer", command=custmenu.show_add_new_customer)
    btn_delete_customer = tk.Button(fr_submenu, text="Delete customer", command=custmenu.show_delete_customer)
    btn_update_customer = tk.Button(fr_submenu, text="Update customer", command=custmenu.show_update_customer)
    btn_see_customer = tk.Button(fr_submenu, text="See Customer", command=custmenu.see_customer)
    btn_see_customers = tk.Button(fr_submenu, text="See Customers", command=custmenu.see_customers)
    
    btn_add_customer.grid(row=0, column=1, sticky="ew", padx=20, pady=10)
    btn_delete_customer.grid(row=1, column=1, sticky="ew", padx=20, pady=10)
    btn_update_customer.grid(row=2, column=1, sticky="ew", padx=20, pady=10)
    btn_see_customer.grid(row=3, column=1, sticky="ew", padx=20, pady=10)
    btn_see_customers.grid(row=4, column=1, sticky="ew", padx=20, pady=10)
    
    fr_submenu.grid(row=0, column=1, sticky="nsew")
    fr_main.grid(row=0, column=2, sticky='nsew')

def open_bookings_menu():
    fr_submenu = tk.Frame(window_main, bg = "steelblue", width = 200)
    fr_main = tk.Frame(window_main, bg = "lightsteelblue", width=325)
    bookmenu = BookingsMenu(fr_main)

    btn_add_booking = tk.Button(fr_submenu, text="Add new booking", command=bookmenu.show_add_booking)
    btn_delete_booking = tk.Button(fr_submenu, text="Delete booking", command=bookmenu.show_delete_booking)
    btn_update_booking = tk.Button(fr_submenu, text="Update booking", command=bookmenu.show_update_booking)
    btn_see_bookings = tk.Button(fr_submenu, text="See bookings", command=bookmenu.show_see_bookings)
    btn_see_bill = tk.Button(fr_submenu, text="See Bill", command=bookmenu.show_see_bill)

    btn_add_booking.grid(row=0, column=1, sticky="ew", padx=20, pady=10)
    btn_delete_booking.grid(row=1, column=1, sticky="ew", padx=20, pady=10)
    btn_update_booking.grid(row=2, column=1, sticky="ew", padx=20, pady=10)
    btn_see_bookings.grid(row=3, column=1, sticky="ew", padx=20, pady=10)
    btn_see_bill.grid(row=4, column=1, sticky="ew", padx=20, pady=10)

    fr_submenu.grid(row=0, column=1, sticky="nsew")
    fr_main.grid(row=0, column=2, sticky="nsew")

def open_tables_menu():
    fr_submenu = tk.Frame(window_main, bg = "steelblue", width = 200)
    fr_main = tk.Frame(window_main, bg = "lightsteelblue", width=325)
    tablemenu = TablesMenu(fr_main)

    btn_add_table = tk.Button(fr_submenu, text="Add new table", command=tablemenu.show_add_table)
    btn_delete_table = tk.Button(fr_submenu, text="Delete table", command=tablemenu.show_delete_table)
    btn_update_table = tk.Button(fr_submenu, text="Update table", command=tablemenu.show_update_table)
    btn_see_tables = tk.Button(fr_submenu, text="See tables", command=tablemenu.see_tables)

    btn_add_table.grid(row=0, column=1, sticky="ew", padx=35, pady=10)
    btn_delete_table.grid(row=1, column=1, sticky="ew", padx=35, pady=10)
    btn_update_table.grid(row=2, column=1, sticky="ew", padx=35, pady=10)
    btn_see_tables.grid(row=3, column=1, sticky="ew", padx=35, pady=10)

    fr_submenu.grid(row=0, column=1, sticky="nsew")
    fr_main.grid(row=0, column=2, sticky="nsew")

def open_menu_order_menu():
    fr_submenu = tk.Frame(window_main, bg = "steelblue", width = 200)
    fr_main = tk.Frame(window_main, bg = "lightsteelblue", width=325)
    menuorder = MenuandOrdersMenu(fr_main)

    btn_add_order = tk.Button(fr_submenu, text="Add new order", command=menuorder.show_add_order)
    btn_see_orders = tk.Button(fr_submenu, text="See orders", command=menuorder.show_see_orders)
    btn_add_product = tk.Button(fr_submenu, text="Add new product", command=menuorder.show_add_product)
    btn_delete_product = tk.Button(fr_submenu, text="Delete product", command=menuorder.show_delete_product)
    btn_update_product = tk.Button(fr_submenu, text="Update product", command=menuorder.show_update_product)
    btn_see_products = tk.Button(fr_submenu, text="See products", command=menuorder.see_products)
    btn_print_menu = tk.Button(fr_submenu, text="Print menu", command=menuorder.see_menu)
    btn_check_products = tk.Button(fr_submenu, text="Check stock of products", command=menuorder.check_out_of_stock)

    btn_add_order.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
    btn_see_orders.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
    btn_add_product.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_product.grid(row=3, column=1, sticky="ew", padx=10, pady=10)
    btn_update_product.grid(row=4, column=1, sticky="ew", padx=10, pady=10)
    btn_see_products.grid(row=5, column=1, sticky="ew", padx=10, pady=10)
    btn_print_menu.grid(row=6, column=1, sticky="ew", padx=10, pady=10)
    btn_check_products.grid(row=7, column=1, sticky="ew", padx=10, pady=10)

    fr_submenu.grid(row=0, column=1, sticky="nsew")
    fr_main.grid(row=0, column=2, sticky="nsew")

def open_ingredients_menu():
    fr_submenu = tk.Frame(window_main, bg = "steelblue", width = 200)
    fr_main = tk.Frame(window_main, bg = "lightsteelblue", width=325)
    ingmenu = IngredientsMenu(fr_main)

    btn_add_ingredient = tk.Button(fr_submenu, text="Add new ingredient", command=ingmenu.show_add_ingredient)
    btn_delete_ingredient = tk.Button(fr_submenu, text="Delete ingredient", command=ingmenu.show_delete_ingredient)
    btn_update_ingredient = tk.Button(fr_submenu, text="Update ingredient", command=ingmenu.show_delete_ingredient)
    btn_see_ingredients = tk.Button(fr_submenu, text="See ingredients", command=ingmenu.see_ingredients)
    btn_add_batch = tk.Button(fr_submenu, text="Add new batch", command=ingmenu.show_add_batch)
    btn_delete_batch = tk.Button(fr_submenu, text="Delete batch", command=ingmenu.show_delete_batch)
    btn_update_batch = tk.Button(fr_submenu, text="Update batch", command=ingmenu.show_update_batch)
    btn_see_batches = tk.Button(fr_submenu, text="See batches", command=ingmenu.see_batches)
    btn_delete_batches = tk.Button(fr_submenu, text="Delete expired batches", command=ingmenu.show_delete_expired)

    btn_add_ingredient.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_ingredient.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
    btn_update_ingredient.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
    btn_see_ingredients.grid(row=3, column=1, sticky="ew", padx=10, pady=10)
    btn_add_batch.grid(row=4, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_batch.grid(row=5, column=1, sticky="ew", padx=10, pady=10)
    btn_update_batch.grid(row=6, column=1, sticky="ew", padx=10, pady=10)
    btn_see_batches.grid(row=7, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_batches.grid(row=8, column=1, sticky="ew", padx=10, pady=10)

    fr_submenu.grid(row=0, column=1, sticky="nsew")
    fr_main.grid(row=0, column=2, sticky="nsew")

def open_staff_menu():
    fr_submenu = tk.Frame(window_main, bg = "steelblue", width=200)
    fr_main = tk.Frame(window_main, bg = "lightsteelblue", width=325)
    staffmenu = StaffMenu(fr_main)

    btn_add_staff = tk.Button(fr_submenu, text="Add new employee", command=staffmenu.show_add_member)
    btn_delete_staff = tk.Button(fr_submenu, text="Delete an employee", command=staffmenu.show_delete_member)
    btn_update_self = tk.Button(fr_submenu, text="Update account details", command=staffmenu.show_update_account)
    btn_update_staff = tk.Button(fr_submenu, text="Update an employee", command=staffmenu.show_update_member)
    btn_see_staffs = tk.Button(fr_submenu, text="See employees", command=staffmenu.see_employees)

    btn_add_staff.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_staff.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
    btn_update_self.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
    btn_update_staff.grid(row=3, column=1, sticky="ew", padx=10, pady=10)
    btn_see_staffs.grid(row=4, column=1, sticky="ew", padx=10, pady=10)

    fr_submenu.grid(row=0, column=1, sticky="nsew")
    fr_main.grid(row=0, column=2, sticky="nsew")
    


window_login = tk.Tk()
window_login.title("Wilson's Kitchen")

window_login.rowconfigure(0, minsize=200, weight=1)
window_login.columnconfigure(0, minsize=150, weight=1)

frame_login = tk.Frame(window_login, bg="LightSteelBlue")
frame_login.grid(row=0, column=0, sticky="nsew")

lbl = tk.Label(frame_login, bg="AliceBlue", text="Please enter your details:")
lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

username_lbl = tk.Label(frame_login, bg="AliceBlue", text="Username:")
username_lbl.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
username_lbl = tk.Entry(frame_login)
username_lbl.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

password_lbl = tk.Label(frame_login, bg="AliceBlue", text="Password:")
password_lbl.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
password_lbl = tk.Entry(frame_login)
password_lbl.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

userlogin = Login()

login_btn = tk.Button(frame_login, bg="AliceBlue", text="Login", command=partial(loginfunc, username_lbl, password_lbl))
login_btn.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=10)


window_login.mainloop()

window_main = tk.Tk()
window_main.title("Wilson's Kitchen")

window_main.rowconfigure(0, minsize=500, weight=1)
window_main.columnconfigure([0, 1, 2], minsize=100, weight=1)

#main
fr_main = tk.Frame(window_main, bg = "lightsteelblue", width=325)
fr_mainmenu = tk.Frame(window_main, bg = "darkblue", width=100)

fr_mainmenu.grid(row=0, column=0, sticky="nsew")
fr_main.grid(row=0, column=1, columnspan=2, sticky="nsew")

lbl = tk.Label(fr_main, bg="LightSteelblue", text="Welcome!", font=("lucida 20 bold italic", 20))
lbl.grid(row=2, column=3, sticky="ew", padx=10, pady=10)

btn_customers = tk.Button(fr_mainmenu,
                          text="Customers",
                          command=open_customers_menu)
btn_bookings = tk.Button(fr_mainmenu,
                         text="Bookings",
                         command=open_bookings_menu)
btn_tables = tk.Button(fr_mainmenu,
                       text="Tables",
                       command=open_tables_menu)
btn_menu_order = tk.Button(fr_mainmenu,
                           text="Menu and Orders",
                           command=open_menu_order_menu)
btn_ingredients = tk.Button(fr_mainmenu,
                            text="Ingredients",
                            command=open_ingredients_menu)
btn_staff = tk.Button(fr_mainmenu,
                      text="Employees",
                      command=open_staff_menu)


btn_customers.grid(row=0,
                   column=0,
                   sticky="ew",
                   padx=10,
                   pady=10)
btn_bookings.grid(row=1,
                  column=0,
                  sticky="ew",
                  padx=10,
                  pady=10)
btn_tables.grid(row=2,
                column=0,
                sticky="ew",
                padx=10,
                pady=10)
btn_menu_order.grid(row=3,
                    column=0,
                    sticky="ew",
                    padx=10,
                    pady=10)
btn_ingredients.grid(row=4,
                     column=0,
                     sticky="ew",
                     padx=10,
                     pady=10)
btn_staff.grid(row=5,
               column=0,
               sticky="ew",
               padx=10,
               pady=10)


window_main.mainloop()