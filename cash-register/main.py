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
#  Each time the `purchase_item` method is called, the `RetailItem` object that is passed as an argument should be added to the list.
# - A method named `get_total` that returns the total price of all the `RetailItem` objects stored in the `CashRegister` object’s internal list.
# - A method named `show_items` that displays data about the `RetailItem` objects stored in the `CashRegister` object’s internal list.
# - A method named `clear` that should clear the `CashRegister` object’s internal list.

# Demonstrate the `CashRegister` class in a program that allows the user to select several items for purchase. 
# When the user is ready to check out, the program should display a list of all the items he or she has selected for purchase, as well as the total price. 

import retailitem as ri
import cash_register 

cr = cash_register.CashRegister()

def main():
    # Initial Variables
    item_info = ["Jacket", 12, 56.95, "Designer Jeans", 40, 34.95, "Shirt", 20, 24.95, "Pants", 16, 25.95, "Blouse", 10, 34.95, "Sweats", 5, 14.95]
    items = []
    purchase = 1
    j=0

    # The program should store this data in the objects, 
    for i in range(0, 6):
        ndx=i*3
        items.append(ri.RetailItem(item_info[ndx],item_info[ndx+1],item_info[ndx+2]))
        
    # then display the data for each items on the screen.
    print("The items for sale are:")
    print(f"Item Number\t Description \t Units in Inventory \t Price ")
    for i in range(0,6):
        print(f" Item {i+1:<2}\t{items[i].get_description():<15} \t {items[i].get_inventory_units():^8} \t {items[i].get_price()}")
    print(f"Please, Enter a number between 1 and 6 to select the item would you like to purchase.")
    while purchase != 0 :
        purchase = int(input("Enter the item number you like to purchase, Enter 0 if you are done?"))
        if (purchase == 0):
            continue
        qty = int(input("How many would you like to buy?"))
        if (qty > items[purchase-1].get_inventory_units()) :
            print("That is too many! I don't have that many in stock! Please re-enter your purchase information.")
            continue
        if (qty <= 0):
            print("That not enough! Please re-enter your purchase information.")
            continue
        for j in range(0,qty):
            cr.purchase_item(items[purchase-1])
            items[purchase-1].set_inventory_units(items[purchase-1].get_inventory_units()-1)
            item_info[((purchase-1)*3)+1]-=1
        
    cr.show_items()
    print(f"Your Total is ${cr.get_total():.2f}")    


# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__' :
   main()


