#
# Grant Bossa
# March 2, 2025
# annual_salarySupervisor Class Programming Project
# SDEV 1200
#
# Instructions: 
# In a particular factory, a shift supervisor is a salaried employee who supervises a shift. 
# In addition to a salary, the shift supervisor earns a yearly bonus when his or her shift 
# meets production goals. 
# Write a `ShiftSupervisor` class that is a subclass of the `Employee` class that you created 
# in the Employee and Productionshift_supervisor Classes Programming Project. 
# The `ShiftSupervisor` class should keep a data attribute for the annual salary, 
# and a data attribute for the annual production bonus that a shift supervisor has earned. 
# Demonstrate the class by writing a program that uses a `ShiftSupervisor` object.

import employee;

def main():
    # Local variables
	name = ""
	id_number = ""
	annual_salary = 0.0
	annual_production_bonus = 0.0


	# Get data attributes for these classes.
	print("---------------------------------------------")
	print("Please Enter the Shift Supervisor Information")
	print("_____________________________________________")
	name = 				input("                             Name: ")
	id_number = 		input("                        Id Number: ")
	annual_salary = float(input("          Enter the Annual Salary: $ "))
	annual_production_bonus = float(input("Enter the Annual Production Bonus: $ "))

	# Create an instance of ShiftSupervisor class
	my_shift_supervisor = employee.ShiftSupervisor(name, id_number, annual_salary, annual_production_bonus)

	# Display information.
	print("----------------------------")
	print("Shift Supervisor Information")
	print("____________________________")
	print(f"{'Name: ':>29}{my_shift_supervisor.get_name()}")
	print(f"{'Id Number: ':>29}{my_shift_supervisor.get_id_number()}")
	print(f"{'Annual Salary: $':>30}{my_shift_supervisor.get_annual_salary():.2f}")
	print(f"{'Annual Production Bonus: $':>30}{my_shift_supervisor.get_annual_production_bonus():.2f}")

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__" :
    main()