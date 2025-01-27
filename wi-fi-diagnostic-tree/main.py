#
# Grant Bossa
# January 26, 2025
# Wi-Fi Diagnostic Tree Programming Project
# SDEV 1200 
#

# Instructions:
# The Wi-Fi Diagnostic Tree Flowchart shows a simplified flowchart for troubleshooting a bad Wi-Fi connection. 
# Use the flowhart to create a program that leads a person through the steps of fixing a bad Wi-Fi connection. 
# Here is an example of the program's output:
#
# ![](Flowchart.png)
#
# ```python
# Reboot the computer and try to connect.
# Did that fix the problem? no [Enter]
# Reboot the router and try to connect.
# Did that fix the problem? yes [Enter]
# ```

# Notice the program ends as soon as a solution is found to the problem. Here is another example of the program�s output:

# ```python
# Reboot the computer and try to connect. 
# Did that fix the problem? no [Enter] 
# Reboot the router and try to connect. 
# Did that fix the problem? no [Enter] 
# Make sure the cables between the router and modem are plugged in firmly. 
# Did that fix the problem? no [Enter] 
# Move the router to a new location. 
# Did that fix the problem? no [Enter] 
# Get a new router.
# ```


# set variable for question based on level of decision
instuction = ["Reboot the computer and try to connect.", "Reboot the router and try to connect.", "Make sure the cables between the router and modem are plugged in firmly.", "Move the router to a new location." ]
fix = ""     # Use this variable for answering if the problem is fixed

for i in range(1,5):                            # use a loop to ask each question
  print(f"{instuction[i-1]}")                   # display instruction
  fix = input("Did that fix the problem? ")     # Ask if the problem is fixed
  if (fix != 'yes'):                            # if not 'yes' go to next instruction message
     continue
  else :                                        # if 'yes' end processing
     break

if (fix != 'yes'):                              # if all questions are asked without 'yes' then process final instruction
  print("Get a new router.")

