#
# Grant Bossa
# February 6, 2025
# Pet Class Programming Project
# SDEV 1200
#
# Instructions  

# Write a program that creates an object of the class and 
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
    myPet.set_age(int(input("Please enter your pet's age : ")))
 
    # Display the entered information
    print("You entered the following information:")
    print(f"Your pet's name: \t {myPet.get_name()}")
    print(f"Your pet's type: \t {myPet.get_animal_type()}")
    print(f"Your pet's age: \t {myPet.get_age()}")

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__" :
    main()
