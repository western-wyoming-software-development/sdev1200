#
# Joe   
# 1 24 2025
# Pennies for Pay Programming Project
# SDEV 1200 
#

def calculate_daily_salary(days):
  """
  Calculates the daily salary for a given number of days, 
  where the salary doubles each day, starting from 1 penny.

  Args:
    days: The number of days to calculate the salary for.

  Returns:
    A list of daily salaries in dollars.
  """
  daily_salaries = []
  salary = 0.01  # Starting salary in dollars
  for _ in range(days):
    daily_salaries.append(salary)
    salary *= 2
  return daily_salaries

def display_salary_table(daily_salaries):
  """
  Displays a table showing the daily salary for each day.

  Args:
    daily_salaries: A list of daily salaries in dollars.
  """
  print("\nDaily Salary Table:")
  print("Day\tSalary")
  for day, salary in enumerate(daily_salaries, start=1):
    print(f"{day}\t${salary:.2f}")


if __name__ == "__main__":
  num_days = int(input("Enter the number of days: "))
  daily_salaries = calculate_daily_salary(num_days)
  display_salary_table(daily_salaries)
  total_pay = sum(daily_salaries)
  print(f"\nTotal Pay: ${total_pay:.2f}") 