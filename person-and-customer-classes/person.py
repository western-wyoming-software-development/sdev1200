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


class Person:
	# The __init__method initalizes the attributes.
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
	
	# The set_name method assigns a value to the `__name` field.
    def set_name(self, name):
        self.__name = name
	
	# The set_address method assigns a value to the `__address` field.
    def set_name(self, address):
        self.__address = address
	
	# The set_phone method assigns a value to the `__phone` field.
    def set_phone(self, phone):
        self.__phone = phone
		
    # The get_name method returns the value of the `__name` field.
    def get_name(self):
        return self.__name

    # The get_address method returns the value of the `__address` field.
    def get_address(self):
        return self.__address

    # The get_phone method returns the value of the `__phone` field.
    def get_phone(self):
        return self.__phone

class Customer(Person):
	# The __init__method initalizes the attributes.
    def __init__(self, name, address, phone, customer_number, mailing_list):
		# call the superclass __init__ method
        Person.__init__(self, name, address, phone)
		
		# The __init__method initalizes the attributes.
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list
		
    # The set_customer_number method assigns a value to the `__customer_number` field.
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    # The set_mailing_list method assigns a value to the `__mailing_list` field.
    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list
        
    # The get_customer_number method returns the value of the `__customer_number` field.
    def get_customer_number(self):
        return self.__customer_number

    # The get_mailing_list method returns the value of the `__mailing_list` field.
    def get_mailing_list(self):
        return self.__mailing_list
