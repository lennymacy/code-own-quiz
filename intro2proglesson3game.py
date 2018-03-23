#************IMPORTANT************
#coded using python 3.6.0

#get user info-name and print
name = input("Hello. So, what is your name?")
print ("Thanks for stopping by " + name + ".  This is a game about geometric shapes. So let's test your knowledge about shapes!")


"""input from user to determine game level output the level
   selected to use in game play to use correct Q&A"""
def game_level():
    input_level = input("Now I need you to pick how difficult you want the game. Select your choice by typing one of the following-- easy, medium, or hard:  ")
    while input_level not in ["easy", "medium", "hard"]:
        input_level = input("I didn't understand, please try again. Please choose from easy, medium or hard: ")
    choice_index = 0
    while input_level != user_choice[choice_index]:
        choice_index = choice_index + 1
    print (message[choice_index],"\n","\n","Ok. Here we go with your questions","\n","\n")
    return input_level

"""game control function
   sets 3 counters: one for moving thru blans to fill in, one to compare
   answers and one to set how many guess the user will get
   output will be leting user know if won or lost with print and speech"""
def play_game():

    level = game_level()
    quiz = quiz_data[level]['quiz']
    print (quiz)
    answers_list = quiz_data[level]['answers']
    for guess in range(0, len(blanks)):
        user_answer = input("The answer to question " + blanks[guess] + "? : ")
        tries = 1
        while user_answer != answers_list[guess]:
            tries += 1
            user_answer = input("Yikes! that is not correct. Try again. The answer to question " + blanks[guess] + "? : ")
            if tries == 3:
                print ("You lost the game. Let's go back and start over. Try an easier level, maybe. Ready?","\n","\n")
                play_game()
        else:
            print ("CHA CHING! That is correct!")
            quiz = quiz.replace(blanks[guess], user_answer.upper())
            print (quiz)
    print ("YAY! You won! You are a CHAMPION!!!")

#variables to prepare game level messages
user_choice = ["easy", "medium", "hard"]
message = ["Taking the easy road, eh? Okay...", "This may be a little bit of a challenge...", "Put your thinking cap on and GOOD LUCK!"]
blanks = ["__1__", "__2__", "__3__", "__4__"]

#questions for data dictionary as called from play_game
easy_questions = '''A triangle has __1__ sides, a square has __2__ sides, a hexagon has __3__ sides and an octogon has  __4__ sides.'''
medium_questions = '''A pentagon has __1__ sides, a trapezoid has  __2__ sides, a heptogon has __3__, sides, and a circle has  __4__ sides.'''
hard_questions = '''A nonagon has __1__. sides, a dodecagon has __2__sides, a rhombus has __3__ sides, and a digon has __4__ sides.'''

#answers for data dictionary as called from play game answer list variable
easy_answers = ["3", "4", "6", "8"]
medium_answers = ["5", "4", "7", "0"]
hard_answers = ["9", "12", "4", "2"]

#dictionay list for questions and answers
quiz_data = {
   'easy': {
        'quiz': easy_questions,
        'answers': easy_answers,
    },
   'medium': {
        'quiz': medium_questions,
        'answers': medium_answers,
    },
   'hard': {
        'quiz': hard_questions,
        'answers': hard_answers,
    }
}

play_game()

#Works Cited: github, stackoverflow, codecamedy, google,
# solollearn, my mentor, udacity videos and transcripts.

#During this project I reviewed python material in github, stackoverflow,
#codecamedy, google, solollearn, my mentor, udacity videos and transcripts.
