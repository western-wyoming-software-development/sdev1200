#
# Grant Bossa
# 1/19/2025
# Ingredient Adjuster Programming Project
# SDEV 1200 
# 

# Instructions: A cookie recipe calls for the following ingredients:
#
# * 1.5 cups of sugar
# * 1 cup of butter
# * 2.75 cups of flour

# The recipe produces 48 cookies. Write a program that asks the user how many cookies they want to make, 
# then displays the number of cups of each ingredient needed for the specified number of cookies. 
# Be sure to format your numeric output to two decimal points.


# Declare variables.
# Recipe variables are based upon 1 cookie, Hence, the calculations in the definitions.

original_yield = 48
sugar = 1.5/original_yield
butter = 1/original_yield
flour = 2.75/original_yield

def main():
    input_yield = float(input("How many cookies would you like to make?   "))   # Request number of cookies

    # Display results of recipe conversion...The conversion is included in output statement
    print (f"The recipe for {input_yield:.2f} cookies calculates to:")  
    print (f"{input_yield * sugar:.2f} cups of sugar")
    print (f"{input_yield * butter:.2f} cups of butter")
    print (f"{input_yield * flour:.2f} cups of flour")
# end of function main

# Call the main function
main()

# End of Program