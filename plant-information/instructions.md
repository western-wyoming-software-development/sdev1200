# Instructions  

Given a base Plant class and a derived Flower class, write a program to create a list called `my_garden`. Store objects that belong to the `Plant` class or the `Flower` class in the list. Create a function called `print_list()`, that uses the `print_info()` instance methods defined in the respective classes and prints each element in `my_garden`. The program should read plants or flowers from input (ending with -1), add each `Plant` or `Flower` to the `my_garden` list, and output each element in `my_garden` using the `print_info()` function.

Note: A list can contain different data types and also different objects.

Ex. If the input is:

`plant Spirea 10 
flower Hydrangea 30 false lilac 
flower Rose 6 false white
plant Mint 4
-1`

the output is:

`Plant 1 Information:
   Plant name: Spirea
   Cost: 10

Plant 2 Information:
   Plant name: Hydrangea
   Cost: 30
   Annual: false
   Color of flowers: lilac

Plant 3 Information:
   Plant name: Rose
   Cost: 6
   Annual: false
   Color of flowers: white

Plant 4 Information:
   Plant name: Mint
   Cost: 4`