#
# Grant Bossa
# February 16, 2025
# Trivia Game Programming Project
# SDEV 1200
#

# Instructions: 

# The Question class should have attributes for the following data:
# 
# A trivia question
# Possible answer 1
# Possible answer 2
# Possible answer 3
# Possible answer 4
# The number of the correct answer (1, 2, 3, or 4)

# The Question class also should have an appropriate __init__ method, accessors, and mutators.
 
# A class named `Question` that holds the following data about trivia questions in attributes: 
#   A trivia question, Possible answer 1, Possible answer 2, Possible answer 3, Possible answer 4,
#   and the number of the correct answer (1, 2, 3, or 4)
class Question:
    # The __init__method initalizes the attributes.
    def __init__(self, trivia_question, answer_1, answer_2, answer_3, answer_4, correct_answer_number):
        self.__trivia_question = trivia_question
        self.__answer_1 = answer_1
        self.__answer_2 = answer_2
        self.__answer_3 = answer_3
        self.__answer_4 = answer_4
        self.__correct_answer_number = correct_answer_number

    # The set_name method assigns a value to the `__trivia_question` field.
    def set_trivia_question(self, trivia_question):
        self.__trivia_question = trivia_question
    
    # The set_name method assigns a value to the `__answer_1` field.
    def set_answer_1(self, answer_1):
        self.__answer_1 = answer_1
    
    # The set_name method assigns a value to the `__answer_2` field.
    def set_answer_2(self, answer_2):
        self.__answer_2 = answer_2
    
    # The set_name method assigns a value to the `__answer_3` field.
    def set_answer_3(self, answer_3):
        self.__answer_3 = answer_3
    
        # The set_name method assigns a value to the `__answer_4` field.
    def set_answer_4(self, answer_4):
        self.__answer_4 = answer_4
    
    # The set_name method assigns a value to the `__correct_answer_number` field.
    def set_correct_answer_number(self, correct_answer_number):
        self.__correct_answer_number = correct_answer_number
    
    # The get_name method returns the value of the `__trivia_question` field.
    def get_trivia_question(self):
        return self.__trivia_question
    
    # The get_name method returns the value of the `__answer_1` field.
    def get_answer_1(self):
        return self.__answer_1
    
    # The get_name method returns the value of the `__answer_2` field.
    def get_answer_2(self):
        return self.__answer_2
    
    # The get_name method returns the value of the `__answer_3` field.
    def get_answer_3(self):
        return self.__answer_3
    
    # The get_name method returns the value of the `__answer_4` field.
    def get_answer_4(self):
        return self.__answer_4
 
     # The get_name method returns the value of the `__correct_answer_number` field.
    def get_correct_answer_number(self):
        return self.__correct_answer_number
