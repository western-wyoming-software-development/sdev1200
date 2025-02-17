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
