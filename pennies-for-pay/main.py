#
# Grant Bossa
# January 26, 2025
# Pennies for Pay Programming Project
# SDEV 1200 
#

# Instructions: 
# Write a program that calculates the amount of money a person would earn over a period of time 
# if their salary is one penny the first day, two pennies the second day, and continues to double each day. 
# The program should ask the user for the number of days. 
# Display a table showing what the salary was for each day, 
# then show the total pay at the end of the period. 
# The output should be displayed in a dollar amount, not the number of pennies.

def display_table(i, pay):
   print (f"day {i:^3} wages ${pay:10,.2f}")

def main() :
   days = int(input("Enter the number of days to be paid for.  "))
   pay = 0.0
   total_pay = 0.0

   if (days > 0) :
      for i in range(1, days+1) :
         pay = (2**(i - 1)/100)
         total_pay += pay
         display_table(i, pay) 
   print(f"        Total ${total_pay:10,.2f}")

main()

