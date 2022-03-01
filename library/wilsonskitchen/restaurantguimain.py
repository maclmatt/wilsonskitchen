import tkinter as tk
from turtle import st
from restaurantmain import Restaurant
import sys

wilsonskitchen = Restaurant()

class CustomersMenu():
    def __init__(self, fr_main):
        self.count = 0
        self.lbl = None
        self.frame = fr_main
    
    def show_add_new_customer(self):
        if self.count != 0:
            self.lbl.destroy()
        self.frame.destroy()
        self.frame = tk.Frame(window, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.count += 1
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
        if self.count != 0:
            self.lbl.destroy()
        self.frame.destroy()
        self.frame = tk.Frame(window, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.count += 1
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
        if self.count != 0:
            self.lbl.destroy()
        self.frame.destroy()
        self.frame = tk.Frame(window, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.count += 1
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
        if self.count != 0:
            self.lbl.destroy()
        self.frame.destroy()
        self.frame = tk.Frame(window, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")

        self.count += 1
        self.lbl = tk.Label(self.frame, text= "Please enter the details of the customer: ")
        self.lbl.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.emaillbl = tk.Label(self.frame, text = "Email:")
        self.emaillbl.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.custemail = tk.Entry(self.frame)
        self.custemail.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.see_customer_button = tk.Button(self.frame, text="See Customer", command=self.see_customers)
        self.see_customer_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def see_customers(self):
        if self.count != 0:
            self.lbl.destroy()
        self.frame.destroy()
        self.frame = tk.Frame(window, bg = "lightsteelblue", width = 200)
        self.frame.grid(row=0, column=2, sticky="nsew")
        self.count += 1
        customers = wilsonskitchen.customers.select_customers()
        self.lbl = tk.Listbox(self.frame)
        for i in range(0, (len(customers))):
            self.lbl = tk.Label(self.frame, text= f"Customer {customers[i][0]}'s details:\nCustomer Email: {customers[i][1]}\nCustomer Name: {customers[i][2]} {customers[i][3]}\nPhone number: {customers[i][4]}")
            self.lbl.grid(row=i, column=0, columnspan=2, sticky= "ew", padx=10, pady=10)
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
class StaffMenu():
    def __init__(self):
        self.count = 0
        self.lbl = None

def open_customers_menu():
    custmenu = CustomersMenu(fr_main)
    window.columnconfigure([0, 1, 2], minsize=100, weight=1)
    btn_add_customer = tk.Button(fr_submenu, text="Add new customer", command=custmenu.show_add_new_customer)
    btn_delete_customer = tk.Button(fr_submenu, text="Delete customer", command=custmenu.show_delete_customer)
    btn_update_customer = tk.Button(fr_submenu, text="Update customer", command=custmenu.show_update_customer)
    btn_see_customer = tk.Button(fr_submenu, text="See Customer", command=custmenu.see_customer)
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

def open_tables_menu():
    tablemenu = TablesMenu()
    window.columnconfigure([0, 1, 2], minsize=100, weight=1)
    btn_add_table = tk.Button(fr_submenu, text="Add new table")
    btn_delete_table = tk.Button(fr_submenu, text="Delete table")
    btn_update_table = tk.Button(fr_submenu, text="Update table")
    btn_see_tables = tk.Button(fr_submenu, text="See tables")

    btn_add_table.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_table.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
    btn_update_table.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
    btn_see_tables.grid(row=3, column=1, sticky="ew", padx=10, pady=10)

    fr_submenu.grid(row=0, column=1, sticky="ns")
    fr_main.grid(row=0, column=2, sticky="nsew")

def open_menu_order_menu():
    menuorder = MenuandOrdersMenu()
    window.columnconfigure([0, 1, 2], minsize=100, weight=1)
    btn_add_order = tk.Button(fr_submenu, text="Add new order")
    btn_see_orders = tk.Button(fr_submenu, text="See orders")
    btn_add_product = tk.Button(fr_submenu, text="Add new product")
    btn_delete_product = tk.Button(fr_submenu, text="Delete product")
    btn_update_product = tk.Button(fr_submenu, text="Update product")
    btn_see_products = tk.Button(fr_submenu, text="See products")
    btn_print_menu = tk.Button(fr_submenu, text="Print menu")
    btn_check_products = tk.Button(fr_submenu, text="Check for any out of stock products.")

    btn_add_order.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
    btn_see_orders.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
    btn_add_product.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_product.grid(row=3, column=1, sticky="ew", padx=10, pady=10)
    btn_update_product.grid(row=4, column=1, sticky="ew", padx=10, pady=10)
    btn_see_products.grid(row=5, column=1, sticky="ew", padx=10, pady=10)
    btn_print_menu.grid(row=6, column=1, sticky="ew", padx=10, pady=10)
    btn_check_products.grid(row=7, column=1, sticky="ew", padx=10, pady=10)

    fr_submenu.grid(row=0, column=1, sticky="ns")
    fr_main.grid(row=0, column=2, sticky="nsew")

def open_ingredients_menu():
    ingmenu = IngredientsMenu()
    window.columnconfigure([0, 1, 2], minsize=100, weight=1)
    btn_add_ingredient = tk.Button(fr_submenu, text="Add new ingredient")
    btn_delete_ingredient = tk.Button(fr_submenu, text="Delete ingredient")
    btn_update_ingredient = tk.Button(fr_submenu, text="Update ingredient")
    btn_see_ingredients = tk.Button(fr_submenu, text="See ingredients")
    btn_add_batch = tk.Button(fr_submenu, text="Add new batch")
    btn_delete_batch = tk.Button(fr_submenu, text="Delete batch")
    btn_update_batch = tk.Button(fr_submenu, text="Update batch")
    btn_see_batches = tk.Button(fr_submenu, text="See batches")
    btn_delete_batches = tk.Button(fr_submenu, text="Delete out of stock batches")

    btn_add_ingredient.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_ingredient.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
    btn_update_ingredient.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
    btn_see_ingredients.grid(row=3, column=1, sticky="ew", padx=10, pady=10)
    btn_add_batch.grid(row=4, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_batch.grid(row=5, column=1, sticky="ew", padx=10, pady=10)
    btn_update_batch.grid(row=6, column=1, sticky="ew", padx=10, pady=10)
    btn_see_batches.grid(row=7, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_batches.grid(row=8, column=1, sticky="ew", padx=10, pady=10)

    fr_submenu.grid(row=0, column=1, sticky="ns")
    fr_main.grid(row=0, column=2, sticky="nsew")

def open_staff_menu():
    staffmenu = StaffMenu()
    #fr_submenu.destroy()
    #fr_submenu = tk.Frame(window, bg = "cornflowerblue", width = 100)
    window.columnconfigure([0, 1, 2], minsize=100, weight=1)
    btn_add_staff = tk.Button(fr_submenu, text="Add new employee")
    btn_delete_staff = tk.Button(fr_submenu, text="Delete an employee")
    btn_update_self = tk.Button(fr_submenu, text="Update account details")
    btn_update_staff = tk.Button(fr_submenu, text="Update an employee")
    btn_see_staffs = tk.Button(fr_submenu, text="See employees")

    btn_add_staff.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
    btn_delete_staff.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
    btn_update_self.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
    btn_update_staff.grid(row=3, column=1, sticky="ew", padx=10, pady=10)
    btn_see_staffs.grid(row=4, column=1, sticky="ew", padx=10, pady=10)

    fr_submenu.grid(row=0, column=1, sticky="ns")
    fr_main.grid(row=0, column=2, sticky="nsew")
    

window = tk.Tk()
window.title("Wilson's Kitchen")

window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure([0, 1], minsize=100, weight=1)


fr_main = tk.Frame(window, bg = "lightsteelblue", width = 300)
fr_mainmenu = tk.Frame(window, bg = "navy", width = 100)
fr_submenu = tk.Frame(window, bg = "cornflowerblue", width = 100)

fr_mainmenu.grid(row=0, column=0, sticky="nsew")
fr_main.grid(row=0, column=1, sticky="nsew")

btn_customers = tk.Button(fr_mainmenu, text="Customers", command=open_customers_menu)
btn_bookings = tk.Button(fr_mainmenu, text="Bookings", command=open_bookings_menu)
btn_tables = tk.Button(fr_mainmenu, text="Tables", command=open_tables_menu)
btn_menu_order = tk.Button(fr_mainmenu, text="Menu and Orders", command=open_menu_order_menu)
btn_ingredients = tk.Button(fr_mainmenu, text="Ingredients", command=open_ingredients_menu)
btn_staff = tk.Button(fr_mainmenu, text="Employees", command=open_staff_menu)


btn_customers.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
btn_bookings.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
btn_tables.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
btn_menu_order.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
btn_ingredients.grid(row=4, column=0, sticky="ew", padx=10, pady=10)
btn_staff.grid(row=5, column=0, sticky="ew", padx=10, pady=10)


window.mainloop()