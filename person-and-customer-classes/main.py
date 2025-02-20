#
# Grant Bossa
# February 18, 2025
# Person and Customer Classes Programming Project
# SDEV 1200
# 

# Instructions :
 
# Write a class named Person with data attributes for a person’s name, address, and telephone number. 
# Next, write a class named Customer that is a subclass of the Person class. 
# The Customer class should have a data attribute for a customer number, and a Boolean data attribute 
# indicating whether the customer wishes to be on a mailing list. 

# Demonstrate an instance of the Customer class in a simple program.



import person

def main():
    # Local variables
	name = ''
	address = ''
	phone = ''
	customer_number = ''
	mail = ''
	mailing_list = False

    # Get data attributes for these classes.
	name = input('Name: ')
	address = input('Address: ')
	phone = input('Phone: ')
	customer_number = input('Customer Number: ')
	mail = input('Include in mailing list? (y/n): ')
	
	# Determine True or False for mailing list.
	if mail.lower() == 'y':
		mailing_list = True
	else:
		mailing_list = False

    # Create an instance of Customer class
	my_customer = person.Customer(name, address, phone, customer_number, mailing_list)

    # Display information.
	print('Customer Information')
	print('____________________')
	print('Name: ', my_customer.get_name())
	print('Address: ', my_customer.get_address())
	print('Phone: ', my_customer.get_phone())
	print('Customer Number: ', my_customer.get_customer_number())
	print('Mailing List: ', my_customer.get_mailing_list())


# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__" :
    main()