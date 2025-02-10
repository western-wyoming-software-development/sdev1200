#
# Grant Bossa
# February 6, 2025
# RetailItem Class Programming Project
# SDEV 1200
#

# Instructions : 
# 
# Write a class descriptiond `RetailItem` that holds data about an item in a retail store. 
# The class should store the following data in attributes: 
# item description, units in inventory, and price.

# Once you have written the class, write a program that creates three `RetailItem` objects 
# and stores the following data in them:
#|         | Description    | Units in Inventory | Price |
#| ------- | -------------- | ------------------ | ----- |
#| Item #1 | Jacket         | 12                 | 59.95 |
#| Item #2 | Designer Jeans | 40                 | 34.95 |
#| Item #3 | Shirt          | 20                 | 24.95 |

class RetailItem:
    # The __init__method initalizes the attributes.
    def __init__(self, description, inventory_units, price):
        self.__description = description
        self.__inventory_units = inventory_units
        self.__price = price

    # The set_description method assigns a value to the `description` field.
    def set_description(self, description):
        self.__description = description

    # The set_inventory_units method assigns a value to the `__inventory_units` field.
    def set_inventory_units(self, inventory_units):
        self.__inventory_units = inventory_units

    # The set_price method assigns a value to the `__price` field.
    def set_price(self, price):
        self.__price = price
        
    # The get_description method returns the value of the `description` field.
    def get_description(self):
        return self.__description
        
    # The get_inventory_units method returns the value of the `__inventory_units` field.
    def get_inventory_units(self):
        return self.__inventory_units
        
    # The get_price method returns the value of the `__price` field.
    def get_price(self):
        return self.__price

def main():
    # Create three RetailItem objects to hold the following data:
    #|         | Description    | Units in Inventory | Price |
    #| ------- | -------------- | ------------------ | ----- |
    #| Item #1 | Jacket         | 12                 | 59.95 |
    #| Item #2 | Designer Jeans | 40                 | 34.95 |
    #| Item #3 | Shirt          | 20                 | 24.95 |

    # Initial Variables
    item_info = ("Jacket", 12, 56.95, "Designer Jeans", 40, 34.95, "Shirt", 20, 24.95)
    items = []

    # The program should store this data in the three objects, 
    for i in range(0, 3):
        ndx=i*3
        items.append(RetailItem(item_info[ndx],item_info[ndx+1],item_info[ndx+2]))
   
    # then display the data for each items on the screen.
    print("The items information:")
    print(f"Description \t Units in Inventory \t Price ")
    for i in range(0,3):
        print(f"{items[i].get_description():<15} \t {items[i].get_inventory_units():^8} \t {items[i].get_price()}")

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__' :
   main()
