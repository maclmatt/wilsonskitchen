from distutils import command
import tkinter as tk
from restaurantmain import Restaurant
import sys

wilsonskitchen = Restaurant()

def see_customers():
    customers = wilsonskitchen.customers.customers_select_customers()
    text = f"\nCustomer {customers[0][0]}'s details:\n   Customer Email: {customers[0][1]}\n   Customer Name: {customers[0][2]} {customers[0][3]}"
    txt_edit.insert(tk.END, text)

def open_customers_menu():
    btn_see_customers = tk.Button(fr_submenu, text="See Customers", command=see_customers)
    btn_see_customers.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    fr_submenu.grid(row=0, column=1, sticky="ns")
    txt_edit.grid(row=0, column=2, sticky='nsew')
         
window = tk.Tk()
window.title("Wilson's Kitchen")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure([0, 1, 2], minsize=70, weight=1)


txt_edit = tk.Text(window)
fr_mainmenu = tk.Frame(window, bg = "navy")
fr_submenu = tk.Frame(window, bg = "cornflowerblue")
btn_customers = tk.Button(fr_mainmenu, text="Customers", command=open_customers_menu)
btn_bookings = tk.Button(fr_mainmenu, text="Bookings")

btn_customers.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_bookings.grid(row=1, column=0, sticky="ew", padx=5)

fr_mainmenu.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()