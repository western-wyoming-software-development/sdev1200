#
# Grant Bossa
# February 6, 2025
# Employee Class Programming Project
# SDEV 1200
#

# Instructions 

# Write a class named `Employee` that holds the following data about an employee in attributes: 
# name, ID number, department, and job title. 

# A class named `Employee` that holds the following data about an employee in attributes: 
# name, ID number, department, and job title.
class Employee:
    # The __init__method initalizes the attributes.
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    # The set_name method assigns a value to the `__name` field.
    def set_name(self, name):
        self.__name = name

    # The set_id_number method assigns a value to the `__id_number` field.
    def set_id_number(self, id_number):
        self.__id_number = id_number

    # The set_department method assigns a value to the `__department` field.
    def set_department(self, department):
        self.__department = department

    # The set_job_title method assigns a value to the `__job_title` field.
    def set_job_title(self, job_title):
        self.__job_title = job_title
        
    # The get_name method returns the value of the `__name` field.
    def get_name(self):
        return self.__name
        
    # The get_id_number method returns the value of the `__id_number` field.
    def get_id_number(self):
        return self.__id_number
        
    # The get_department method returns the value of the `__department` field.
    def get_department(self):
        return self.__department
        
    # The get_job_title method returns the value of the `__job_title` field.
    def get_job_title(self):
        return self.__job_title
