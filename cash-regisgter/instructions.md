# Instructions  

This exercise assumes you have created the `RetailItem` class for the RetailItem Class Programming Project. Create a `CashRegister` class that can be used with the `RetailItem` class. The `CashRegister` class should be able to internally keep a list of `RetailItem` objects. The class should have the following methods:
- A method named `purchase_item` that accepts a `RetailItem` object as an argument. Each time the `purchase_item` method is called, the `RetailItem` object that is passed as an argument should be added to the list.
- A method named `get_total` that returns the total price of all the `RetailItem` objects stored in the `CashRegister` object’s internal list.
- A method named `show_items` that displays data about the `RetailItem` objects stored in the `CashRegister` object’s internal list.
- A method named `clear` that should clear the `CashRegister` object’s internal list.

Demonstrate the `CashRegister` class in a program that allows the user to select several items for purchase. When the user is ready to check out, the program should display a list of all the items he or she has selected for purchase, as well as the total price.