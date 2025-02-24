#
# Grant Bossa
# February 18, 2025
# Employee And ProductionWorker Classes Programming Project
# SDEV 1200
# 

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
 
 
class Employee:
	# The __init__method initalizes the attributes.
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    # The set_name method assigns a value to the `__name` field.
    def set_name(self, name):
        self.__name = name

    # The set_id_number method assigns a value to the `__id_number` field.
    def set_id_number(self, id_number):
        self.__id_number = id_number
        
    # The get_name method returns the value of the `__name` field.
    def get_name(self):
        return self.__name
        
    # The get_id_number method returns the value of the `__id_number` field.
    def get_id_number(self):
        return self.__id_number
  
class ProductionWorker(Employee):
	# The __init__method initalizes the attributes.
    def __init__(self, name, id_number, shift, pay_rate_hourly):
		# call the superclass __init__ method
        Employee.__init__(self, name, id_number)
		
        # The __init__method initalizes the attributes.
        self.__shift = shift
        self.__pay_rate_hourly = round(pay_rate_hourly,2)
        
    # The set_shift method assigns a value to the `__shift` field.
    def set_shift(self, shift):
        self.__shift = shift

    # The set_pay_rate_hourly method assigns a value to the `__pay_rate_hourly` field.
    def set_pay_rate_hourly(self, pay_rate_hourly):
        self.__pay_rate_hourly = round(pay_rate_hourly,2)
        
    # The get_shift method returns the value of the `__shift` field.
    def get_shift(self):
        return self.__shift

    # The get_pay_rate_hourly method returns the value of the `__pay_rate_hourly` field.
    def get_pay_rate_hourly(self):
        return self.__pay_rate_hourly