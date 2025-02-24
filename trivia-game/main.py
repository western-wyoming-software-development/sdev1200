#
# Grant Bossa
# February 11, 2025
# Trivia Game Programming Project
# SDEV 1200
#

# Instructions :
# In this programming exercise, you will create a simple trivia game for two players. The program will work like this:

# Starting with player 1, each player gets a turn at answering 5 trivia questions. 
# (There should be a total of 10 questions.) 
# When a question is displayed, 4 possible answers are also displayed. 
# Only one of the answers is correct, and 
# if the player selects the correct answer, he or she earns a point.

# After answers have been selected for all the questions, 
# the program displays the number of points earned by each player 
# and declares the player with the highest number of points the winner.

# The program should have a list or a dictionary containing 10 Question objects, one for each trivia question. 

import random;
import question;

# Initial Variables
my_dict = {
   '1' : ["Which movie did Marilyn Monroe sing Diamonds Are a Girl’s Best Friend?",
           "Some Like It Hot", "The Seven Year Itch", "Gentlemen Prefer Blondes",
           "There's No Business Like Show Business",3],
   '2' : ["Who is the author of 'The Great Gatsby'?", 
           "J.D. Salinger", "F. Scott Fitzgerald", "Harper Lee", "Ray Bradbury", 2],
   '3' : ["What is the national flower of Japan?", 
           "Cherry Blossom", "Sakura", "Himawari", "Tsubaki", 1],
   '4' : ["What term used for an arm or leg, also means branch of a tree?",
           "Root", "Extremity", "Trunk", "Limb", 4],
   '5' : ["How do you say Merry Christmas in Spanish?",
           "Buenos Dias","Feliz Navidad","Feliz Cumpleaños","Felices Pascuas",2],
   '6' : ["In the 1990’s, what was Pixar’s first feature-length movie?",
           "A Bug’s Life","Monsters, Inc.","Toy Story","Cars",3],
   '7' : ["What tennis score always follows deuce?",
           "Love","Ad In","Match","Advantage",4],
   '8' : ["Which Olympic sport is played with brooms and stones?",
           "Curling","Cricket","Lacrosse","Quidditch",1],
   '9' : ["What holiday is celebrated on the second Sunday in May in the US?",
           "May Day","Memorial Day","Mother's Day","Easter",3],
   '10' : ["What continent is the Capybara native to?",
            "Africa","Asia","North America","South America",4] 
}
   
def main():
   # Initial Variables
   score_player_1 = 0
   score_player_2 = 0
   player_1 = []
   player_2 = []
   list=[]
   # Set questions for players, player 1 gets questions 1-5, player 2 gets questions 6-10
   for j in range (1,6):
      player_1.append(question.Question(my_dict[str(j)][0],my_dict[str(j)][1],my_dict[str(j)][2],my_dict[str(j)][3],my_dict[str(j)][4],my_dict[str(j)][5]))
      player_2.append(question.Question(my_dict[str(j+5)][0],my_dict[str(j+5)][1],my_dict[str(j+5)][2],my_dict[str(j+5)][3],my_dict[str(j+5)][4],my_dict[str(j+5)][5]))

   # Question players
   for j in range(0,5):
      # display question and possible answers
      print(f"________________________________________________________________________")
      print(f"PLAYER 1 your question is:")
      print(f"")
      print(f"{player_1[j].get_trivia_question()}")
      print(f"")
      print(f"Possible Answers:")
      list.append("1. "+player_1[j].get_answer_1())
      list.append("2. "+player_1[j].get_answer_2())
      list.append("3. "+player_1[j].get_answer_3())
      list.append("4. "+player_1[j].get_answer_4())
     
      for l in range(0,4):
         print(f"{list[l]}")

      # input players answer and compare
      if (int(input("Which is the correct answer (1, 2, 3, or 4)? "))== player_1[j].get_correct_answer_number()):
         print(f"You are Correct! You score 1 point")    #     IF correct display message 'Correct'
         score_player_1 += 1                             #     score + 1   
      else :
         print(f"You are Incorrect! The correct answer was:")            #        display message 'Incorrect'
         print(f"{list[player_1[j].get_correct_answer_number()-1]}")     #        display correct answer
      list=[]
      
      # display question and possible answers
      print(f"************************************************************************")
      print(f"Player 2 your question is:")
      print(f"")
      print(f"{player_2[j].get_trivia_question()}")
      print(f"")
      print(f"Possible Answers:")
      list.append("1. "+player_2[j].get_answer_1())
      list.append("2. "+player_2[j].get_answer_2())
      list.append("3. "+player_2[j].get_answer_3())
      list.append("4. "+player_2[j].get_answer_4())
     
      for l in range(0,4):
         print(f"{list[l]}")

      # input players answer and compare
      if (int(input("Which is the correct answer (1, 2, 3, or 4)? "))== player_2[j].get_correct_answer_number()):
         print(f"You are Correct! You score 1 point")    #     IF correct display message 'Correct'
         score_player_2 += 1                             #     score + 1   
      else :
         print(f"You are Incorrect! The correct answer was:")            #        display message 'Incorrect'
         print(f"{list[player_2[j].get_correct_answer_number()-1]}")             #        display correct answer
      list=[]
      
   # Display players points
   print(f"Player 1 has {score_player_1} points, Player 2 has {score_player_2} points")
    #     Player ?? wins
   if (score_player_1==score_player_2):
      print(f"The scores are equal so I have to declare a TIE!!!")
   elif(score_player_1>score_player_2):
      print(f"Player 1 WINS!!!")
   else:
      print(f"Player 2 WINS!!!")       
    
# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__" :
    main()
