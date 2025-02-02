#
# Grant Bossa
# January 30, 2025
# Rock, Paper, Scissors Game Programming Project
# SDEV 1200
#

# Instructions :

# Write a program that lets the user play the game of Rock, Paper, Scissors against the computer. 
# The program should work as follows:

# 1. When the program begins, a random number in the range of 1 through 3 is generated. 
#  If the number is 1, then the computer has chosen rock. 
#  If the number is 2, then the computer has chosen paper. 
#  If the number is 3, then the computer has chosen scissors. 
#  (Don't display the computer's choice yet.) 
# 2. The user enters his or her choice of rock, paper, or scissors at the keyboard. 
# 3. The computer's choice is displayed. 
# 4. A winner is selected according to the following rules:
#  If one player chooses rock and the other player chooses scissors, then rock wins. (Rock smashes scissors.) 
#  If one player chooses scissors and the other player chooses paper, then scissors wins. (Scissors cuts paper.) 
#  If one player chooses paper and the other player chooses rock, then paper wins. (Paper wraps rock.) 
#  If both players make the same choice, the game must be played again to determine the winner.

# import for using random functions. 
import random

def main():
#Initial Variables

   choice = ("Rock", "Paper", "Scissors")    
   user_choice = 0
   cpu_choice = 0

   while user_choice == cpu_choice :     # set up loop in case both choose the same value multiple times

      # 1. When the program begins, a random number in the range of 1 through 3 is generated. 
      # If the number is 1, then the computer has chosen rock. 
      # If the number is 2, then the computer has chosen paper. 
      # If the number is 3, then the computer has chosen scissors. 
      cpu_choice =  random.randint(1, 3)

      # 2. The user enters his or her choice of rock, paper, or scissors at the keyboard. 
      user_choice = int(input("Please enter your choice for Rock (1), Paper (2), or Scissors (3).  "))

      # 3. The choices are displayed. 
      print(f"You chose {choice[user_choice - 1]}")
      print(f"The computer chose {choice[cpu_choice - 1]}")

      # 4. A winner is selected according to the following rules:
      #  If one player chooses rock and the other player chooses scissors, then rock wins.
      if ((user_choice == 1 and cpu_choice ==3)
          or (user_choice == 3 and cpu_choice ==1 )):
          print ("Rock smashes scissors. ") 
          if (user_choice == 1) :
            print("You Win!!!")
          else :
            print("Computer Wins!!!")

      #  If one player chooses scissors and the other player chooses paper, then scissors wins. 
      if ((user_choice == 2 and cpu_choice ==3)
         or (user_choice == 3 and cpu_choice ==2 )):
         print (f"Scissors cuts paper.") 
         if (user_choice == 3) :
            print("You Win!!!")
         else :
            print("Computer Wins!!!")

      #  If one player chooses paper and the other player chooses rock, then paper wins. 
      if ((user_choice == 1 and cpu_choice ==2)
         or (user_choice == 2 and cpu_choice ==1 )):
         print (f"Paper wraps rock.") 
         if (user_choice == 2) :
            print("You Win!!!")
         else :
            print("Computer Wins!!!")

      #  If both players make the same choice, the game must be played again to determine the winner.
      if (cpu_choice == user_choice):
         print("Tied, Choose again.")
         # replay - falls through to while loop

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__' :
    main()