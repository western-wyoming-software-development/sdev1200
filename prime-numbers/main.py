#
# Grant Bossa
# January 30, 2025
# Rock, Paper, Scissors Game Programming Project
# SDEV 1200
#

# Instructions  
# A prime number is a number that is only evenly divisible by itself and 1. 
# For example, the number 5 is prime because it can only be evenly divided by 1 and 5. 
# The number 6, however, is not prime because it can be divided evenly by 1, 2, 3, and 6. 

# Write a Boolean function named `is_prime` which takes an integer as an argument and 
# returns true if the argument is a prime number, or false otherwise. 
# Use the function in a program that prompts the user to enter a number 
# then displays a message indicating whether the number is prime.

import math

def is_prime(number):
    if (number <= 1) :                              # if number is <= 1 it is automatically false
        return False
    for i in range(2, int(math.sqrt(number)+1)) :   # if a factorial is not found before the square root, it will not be found
        if (number % i == 0) :                      # a factorial number will not have a remainder
            return False
    return True                                     # by reaching this point, a factorial has not been found
        


def main():
    # Input number, save it, then call is_prime function which returns True or False
    if (is_prime((number := int(input("Please enter a Prime Number.  "))))) :    
        print(f"{number} is a Prime Number")
    else :
        print(f"{number} is not a Prime Number.")

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__' :
    main()