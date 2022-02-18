from distutils import command
import tkinter as tk
from turtle import st
from restaurantmain import Restaurant
import sys

wilsonskitchen = Restaurant()

class CustomersMenu():
    def __init__(self):
        self.count = 0
        self.lbl = None
    

    def show_add_new_customer(self):
        if self.count != 0:
            self.lbl.destroy()
        self.count += 1
        self.lbl = tk.Label(fr_main, text= "Please enter the details of the new customer: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.snamelbl = tk.Label(fr_main, text = "Surname:")
        self.snamelbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.customersname = tk.Entry(fr_main)
        self.customersname.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.add_new_customer_button = tk.Button(fr_main, text="Add Customer", command=self.add_new_customer)
        self.add_new_customer_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def add_new_customer(self):
        wilsonskitchen.customers.customers_add_customer(self.customersname.get(), 
                                                        self.customersname.get(), 
                                                        self.customersname.get(), 
                                                        self.customersname.get())

    def see_customers(self):
        if self.count != 0:
            self.lbl.destroy()
        self.count += 1
        customers = wilsonskitchen.customers.customers_select_customers()
        self.lbl = tk.Listbox(fr_main)
        for i in range(0, (len(customers))):
            self.lbl.insert(tk.END, f"\nCustomer {customers[i][0]}'s details:\n   Customer Email: {customers[i][1]}\n   Customer Name: {customers[i][2]} {customers[i][3]}")        
        self.lbl.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
class BookingsMenu():
    def __init__(self):
        self.count = 0
        self.lbl = None
class TablesMenu():
    def __init__(self):
        self.count = 0
        self.lbl = None
class MenuandOrdersMenu():
    def __init__(self):
        self.count = 0
        self.lbl = None
class IngredientsMenu():
    def __init__(self):
        self.count = 0
        self.lbl = None
class LoginMenu():
    def __init__(self):
        self.count = 0
        self.lbl = None

def open_customers_menu():
    custmenu = CustomersMenu()
    window.columnconfigure([0, 1, 2], minsize=100, weight=1)
    btn_add_customer = tk.Button(fr_submenu, text="Add new customer", command=custmenu.show_add_new_customer)
    btn_delete_customer = tk.Button(fr_submenu, text="Delete customer")
    btn_update_customer = tk.Button(fr_submenu, text="Update customer")
    btn_see_customer = tk.Button(fr_submenu, text="See Customer")
    btn_see_customers = tk.Button(fr_submenu, text="See Customers", command=custmenu.see_customers)
    
    btn_add_customer.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_customer.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
    btn_update_customer.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
    btn_see_customer.grid(row=3, column=1, sticky="ew", padx=10, pady=10)
    btn_see_customers.grid(row=4, column=1, sticky="ew", padx=10, pady=10)
    
    fr_submenu.grid(row=0, column=1, sticky="ns")
    fr_main.grid(row=0, column=2, sticky='nsew')

def open_bookings_menu():
    bookmenu = BookingsMenu()
    window.columnconfigure([0, 1, 2], minsize=100, weight=1)
    btn_add_booking = tk.Button(fr_submenu, text="Add new booking")
    btn_delete_booking = tk.Button(fr_submenu, text="Delete booking")
    btn_update_booking = tk.Button(fr_submenu, text="Update booking")
    btn_see_bookings = tk.Button(fr_submenu, text="See bookings")
    btn_see_bill = tk.Button(fr_submenu, text="See Bill")

    btn_add_booking.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_booking.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
    btn_update_booking.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
    btn_see_bookings.grid(row=3, column=1, sticky="ew", padx=10, pady=10)
    btn_see_bill.grid(row=4, column=1, sticky="ew", padx=10, pady=10)

    fr_submenu.grid(row=0, column=1, sticky="ns")
    fr_main.grid(row=0, column=2, sticky="nsew")




window = tk.Tk()
window.title("Wilson's Kitchen")

window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure([0, 1], minsize=100, weight=1)


fr_main = tk.Frame(window, bg = "lightsteelblue", width = 300)
fr_mainmenu = tk.Frame(window, bg = "navy")
fr_submenu = tk.Frame(window, bg = "cornflowerblue")

btn_customers = tk.Button(fr_mainmenu, text="Customers", command=open_customers_menu)
btn_bookings = tk.Button(fr_mainmenu, text="Bookings", command=open_bookings_menu)

btn_customers.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
btn_bookings.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

fr_mainmenu.grid(row=0, column=0, sticky="nsew")
fr_main.grid(row=0, column=1, sticky="nsew")

window.mainloop()