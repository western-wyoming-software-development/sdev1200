#
# Grant Bossa
# February 6, 2025
# Pet Class Programming Project
# SDEV 1200
#
# Instructions  

# Write a class named `Pet`, which should have the following data attributes:
# - `__name` (for the name of a pet)
# - `__animal_type` (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
# - `__age` (for the pet’s age)

# The Pet class should have an `__init__` method that creates these attributes. 
# 
# It should also have the following methods:
# - `set_name`
# This method assigns a value to the `__name` field.

# - `set_animal_type`
# This method assigns a value to the `__animal_type` field.

# - `set_age`
# This method assigns a value to the `__age` field.

# - `get_name`
# This method returns the value of the `__name` field.

# - `get_animal_type`
# This method returns the value of the `__animal_type` field.

# - `get_age`
# This method returns the value of the `__age` field.

# Once you have written the class, write a program that creates an object of the class and 
# prompts the user to enter the name, type, and age of his or her pet. 
# This data should be stored as the object’s attributes. 
# Use the object’s accessor methods to retrieve the pet’s name, type, and age and 
# display this data on the screen. 

# Review [The Pet Class Problem]
# (https://mediaplayer.pearsoncmg.com/assets/gaddis_sowp6e_The_Pet_Class) VideoNotes. 
# You will see the output you should have for this programming challenge as well as the code.

import pet

def main():
    # Initial Variables
    myPet = pet.Pet("", "", 0)
 
    # Prompts the user to enter the name, type, and age of his or her pet.
    myPet.set_name(input("Please enter your pet's name : "))
    myPet.set_animal_type(input("Please enter your pet's type : "))
    myPet.set_age(float(input("Please enter your pet's age : ")))
 
    # Display the entered information
    print("You entered the following information:")
    print(f"Your pet's name: \t {myPet.get_name()}")
    print(f"Your pet's type: \t {myPet.get_animal_type()}")
    print(f"Your pet's age: \t {myPet.get_age():.2f}")

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__" :
    main()