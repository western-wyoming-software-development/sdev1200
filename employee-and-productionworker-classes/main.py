#
# Grant Bossa
# February 18, 2025
# Employee And ProductionWorker Classes Programming Project
# SDEV 1200
# main.py

# Instructions :
# Write an Employee class that keeps data attributes for the following pieces of information:

# Employee name
# Employee number
# Next, write a class named ProductionWorker that is a subclass of the Employee class. 
# The ProductionWorker class should keep data attributes for the following information:
# Shift number (an integer, such as 1, 2, or 3)
# Hourly pay rate
# The workday is divided into two shifts: day and night. 
# The shift attribute will hold an integer value representing the shift that the employee works. 
# The day shift is shift 1 and the night shift is shift 2. 
# Write the appropriate accessor and mutator methods for each class.

# Once you have written the classes, write a program that creates an object of the 
# ProductionWorker class and prompts the user to enter data for each of the object’s 
# data attributes. 
# Store the data in the object, then 
# use the object’s accessor methods to retrieve it and display it on the screen.

import employee;

def main():
    # Local variables
	name = ''
	id_number = ''
	shift = ''
	pay_rate_hourly = ''


    # Get data attributes for these classes.
	name = input('Name: ')
	id_number = input('Id Number: ')
	shift = int(input('Enter Day Shift = 1 or Night Shift = 2: '))
	pay_rate_hourly = float(input('Hourly Pay Rate: '))

    # Create an instance of ProductionWorker class
	my_worker = employee.ProductionWorker(name, id_number, shift, pay_rate_hourly)

    # Display information.
	print('Production Worker Information')
	print('____________________')
	print('Name: ', my_worker.get_name())
	print('Id Number: ', my_worker.get_id_number())
	print('Shift: ', my_worker.get_shift())
	print(f'Hourly Pay Rate: {my_worker.get_pay_rate_hourly()}')

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__" :
    main()