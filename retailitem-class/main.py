#
# Grant Bossa
# February 6, 2025
# RetailItem Class Programming Project
# SDEV 1200
#

# Instructions : 
# 
# Write a program that creates three `RetailItem` objects 
# and stores the following data in them:
#|         | Description    | Units in Inventory | Price |
#| ------- | -------------- | ------------------ | ----- |
#| Item #1 | Jacket         | 12                 | 59.95 |
#| Item #2 | Designer Jeans | 40                 | 34.95 |
#| Item #3 | Shirt          | 20                 | 24.95 |

include retailitem.py

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
