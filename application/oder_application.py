import tkinter as tk
from tkinter import ttk

# Function to handle the order
def order_coffee():
    selected_coffee = coffee_combo.get()
    price = 0

    if selected_coffee == "Espresso":
        price = 3
    elif selected_coffee == "Latte":
        price = 4
    elif selected_coffee == "Cappuccino":
        price = 5
    elif selected_coffee == "Macchiato":
        price = 4

    result_label.config(text="Your order of " + selected_coffee + " is $" + str(price))

# Create the main window
win = tk.Tk()
win.geometry("500x500+0+0")
win.title("Order Coffee")

# Create the title label
title_label = tk.Label(win, text="Order Coffee", font=("Arial", 25, "bold"))
title_label.pack(side=tk.TOP, fill=tk.X)

# Create the frame to hold the order details
order_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
order_frame.place(x=20, y=90, width=450, height=300)

# Create the label for the coffee
coffee_label = tk.Label(order_frame, text="Coffee", font=("Arial", 15))
coffee_label.grid(row=0, column=0, padx=2, pady=2)

# Create the combo box to select the coffee
coffee_combo = ttk.Combobox(order_frame, font=("Alrial", 15))
coffee_combo['values'] = ("Espresso", "Latte", "Cappuccino", "Macchiato")
coffee_combo.grid(row=0, column=1, padx=2, pady=2)

# Create the button to place the order
order_button = tk.Button(order_frame, text="Order", font=("Arial", 15), command=order_coffee)
order_button.grid(row=1, column=0, columnspan=2, padx=2, pady=2)

# Create the label to display the result
result_label = tk.Label(win, text="", font=("Arial", 15))
result_label.pack(side=tk.BOTTOM, fill=tk.X)

# Start the main event loop
win.mainloop()
