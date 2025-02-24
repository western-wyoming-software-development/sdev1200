#
# Grant Bossa
# February 18, 2025
# Employee And ProductionWorker Classes Programming Project
# SDEV 1200
# 

# Instructions :
# In a particular factory, a shift supervisor is a salaried employee who supervises a shift. 
# In addition to a salary, the shift supervisor earns a yearly bonus when his or her shift meets production goals. 
# Write a `ShiftSupervisor` class that is a subclass of the `Employee` class that you created in the Employee 
# and ProductionWorker Classes Programming Project. 
# The `ShiftSupervisor` class should keep a data attribute for the annual salary, 
# and a data attribute for the annual production bonus that a shift supervisor has earned. 
# Demonstrate the class by writing a program that uses a `ShiftSupervisor` object.


class Employee:
    # Write an Employee class that keeps data attributes for the following pieces of information:
    # Employee name
    # Employee number	
    
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
    # Write a class named ProductionWorker that is a subclass of the Employee class. 
    # The ProductionWorker class should keep data attributes for the following information:

    # Shift number (an integer, such as 1, 2, or 3)
    # Hourly pay rate
    # The workday is divided into two shifts: day and night. 
    # The shift attribute will hold an integer value representing the shift that the employee works. 
    # The day shift is shift 1 and the night shift is shift 2. 
    # Write the appropriate accessor and mutator methods for each class.

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
    
class ShiftSupervisor(Employee):
    # Write a `ShiftSupervisor` class that is a subclass of the `Employee` class that you created in the Employee 
    # and ProductionWorker Classes Programming Project. 
    # The `ShiftSupervisor` class should keep a data attribute for the annual salary, 
    # and a data attribute for the annual production bonus that a shift supervisor has earned. 

	# The __init__method initalizes the attributes.
    def __init__(self, name, id_number, annual_salary, annual_production_bonus):
		# call the superclass __init__ method
        Employee.__init__(self, name, id_number)
		
        # The __init__method initalizes the attributes.
        self.__annual_salary = annual_salary
        self.__annual_production_bonus = round(annual_production_bonus,2)
        
    # The set_annual_salary method assigns a value to the `__annual_salary` field.
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    # The set_annual_production_bonus method assigns a value to the `__annual_production_bonus` field.
    def set_annual_production_bonus(self, annual_production_bonus):
        self.__annual_production_bonus = round(annual_production_bonus,2)
        
    # The get_annual_salary method returns the value of the `__annual_salary` field.
    def get_annual_salary(self):
        return self.__annual_salary

    # The get_annual_production_bonus method returns the value of the `__annual_production_bonus` field.
    def get_annual_production_bonus(self):
        return self.__annual_production_bonus