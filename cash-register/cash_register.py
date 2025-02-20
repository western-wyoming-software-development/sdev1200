#
# Grant Bossa
# February 16, 2025
# Cash Register Programming Project
# SDEV 1200
#

# Instructions  

# This exercise assumes you have created the `RetailItem` class for the RetailItem Class Programming Project. 
# Create a `CashRegister` class that can be used with the `RetailItem` class. 
# The `CashRegister` class should be able to internally keep a list of `RetailItem` objects. 
# The class should have the following methods:
# - A method named `purchase_item` that accepts a `RetailItem` object as an argument. 
#   Each time the `purchase_item` method is called, the `RetailItem` object that is passed as an argument should be added to the list.
# - A method named `get_total` that returns the total price of all the `RetailItem` objects stored in the `CashRegister` object’s internal list.
# - A method named `show_items` that displays data about the `RetailItem` objects stored in the `CashRegister` object’s internal list.
# - A method named `clear` that should clear the `CashRegister` object’s internal list.

# Demonstrate the `CashRegister` class in a program that allows the user to select several items for purchase. 
# When the user is ready to check out, the program should display a list of all the items he or she has selected for purchase, as well as the total price. 

import retailitem as ri

class CashRegister:
# The __init__method initalizes the attributes.
    def __init__(self):
        self.__item_list = []
        self.__total_price = 0

    # - A method named `purchase_item` that accepts a `RetailItem` object as an argument.
    def  purchase_item(self, retail_item) :
        #  Each time the `purchase_item` method is called, 
        #  the `RetailItem` object that is passed as an argument should be added to the list.
        item = ri.RetailItem(retail_item.get_description(), retail_item.get_inventory_units(), retail_item.get_price())
        self.__item_list.append(item)

    # - A method named `get_total` that returns the total price of all the `RetailItem` objects stored in the `CashRegister` object’s internal list.
    def get_total(self):
        self.__total_price = 0
        for item in self.__item_list:
            self.__total_price += item.get_price()
        return self.__total_price
    
    # - A method named `show_items` that displays data about the `RetailItem` objects stored in the `CashRegister` object’s internal list.
    def show_items(self):
        # Display the data for each items on the screen.
        print("The items information:")
        print(f"Description \t Units in Inventory \t Price ")
        for item in self.__item_list:
            print(f"{item.get_description():<15} \t {item.get_inventory_units():^8} \t {item.get_price()}")

    # - A method named `clear` that should clear the `CashRegister` object’s internal list.
    def clear(self):
        self.__item_list=[]