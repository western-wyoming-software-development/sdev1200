#
# Grant Bossa
# February 6, 2025
# Employee Class Programming Project
# SDEV 1200
#

# Instructions 

# Write a program that creates three Employee objects to hold the following data:

# | Name | ID Number | Department | Job Title |
# | ---- | --------- | ---------- | --------- |
# | Luke Skywalker | 47899 | Training | Jedi Master |
# | The Hulk | 39119 | Construction | Demolition Worker |
# | Bullwinkle Moose | 81774 | Animation | Cartoon Character |

# The program should store this data in the three objects, 
# then display the data for each employee on the screen.

import employee as emp

def main():
    # Create three Employee objects to hold the following data:
    # | Name | ID Number | Department | Job Title |
    # | ---- | --------- | ---------- | --------- |
    # | Luke Skywalker | 47899 | Training | Jedi Master |
    # | The Hulk | 39119 | Construction | Demolition Worker |
    # | Bullwinkle Moose | 81774 | Animation | Cartoon Character |

    # Initial Variables
    emp_info = ("Luke Skywalker", 47899, "Training", "Jedi Master", "The Hulk", 39119, "Construction", "Demolition Worker", "Bullwinkle Moose", 81774, "Animation", "Cartoon Character")
    employee = []

    # The program should store this data in the three objects, 
    for i in range(0, 3):
        ndx=i*4
        employee.append(emp.Employee(emp_info[ndx],emp_info[ndx+1],emp_info[ndx+2],emp_info[ndx+3]))
   
    # then display the data for each employee on the screen.
    print("The employee information:")
    print(f"Name                \t ID Number \t Department \t Job Title")
    for i in range(0,3):
        print(f"{employee[i].get_name():<20} \t {employee[i].get_id_number():^9} \t {employee[i].get_department()} \t {employee[i].get_job_title()}")

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__' :
   main()
