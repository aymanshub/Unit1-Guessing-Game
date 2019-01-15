"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
Developed by: Ayman Said
Jan-2019
"""

import random
numbers_range = [1,10]
tries_counter = 0


def set_new_play(sorted_range):
    global tries_counter
    tries_counter = 0
    #pick a new random number
    return random.randint(sorted_range[0],sorted_range[1])

def game_settings():
    global numbers_range
    while True:
        try:
            numbers_range[0] = int(input("Please, select an integer as the lower bound of the numbers range: "))
            numbers_range[1] = int(input("Please, select an integer as the higher bound of the numbers range: "))
        except ValueError:
            print("Incorrect settings!!, please enter valid numbers")
            continue
        else:                    
            numbers_range.sort()
            print("Thanks, the guessing range is set to: {}".format(numbers_range))
            break
            
            
def display_help():
    print("\t ---------------------------- Number Guessing Game ----------------------------")
    print("\
					\n\t Description:\
					\n\t\t Given a random number from a given numbers range, you need to guess\
					\n\t\t what is that number, the game run will end the moment you guess right.\
					\n\t\t The highest score would be for the one who tries the less attempts guessing the right number!\
					\n\
					\n\t SETTINGS:\
					\n\t\t Here, you can change the guessing numbers range, the more you extend the range\
					\n\t\t the harder will be the game ;)\
					\n\t\t By default the range is: {}\
					\n\t\t ".format(numbers_range))
    input("\nPress Enter key to continue...")
          
		
def start_game():
    
    global tries_counter
    highest_score = -1	#a variable that will keep on holding during the game, the highest score
    gamming_on = True
             
    welcome_msg = "Hello, and welcome to the Number Guessing Game"
    print("-" * len(welcome_msg))
    print(welcome_msg)
    print("-" * len(welcome_msg))
    
    while gamming_on:
        game_flow = input("Please, choose an option (PLAY\SETTINGS\HELP\QUIT): ")
        if game_flow.upper() == 'QUIT':
            print("Quitting...Hope to see you soon!")
            break
        elif game_flow.upper() == 'HELP':
            #display help
            display_help()
            continue
            
        elif game_flow.upper() == 'SETTINGS':
            game_settings()
                
        elif game_flow.upper() == 'PLAY':            
            # Get a new random number in the the given range 
            randomized_number = set_new_play(numbers_range)
            while True:
                try:
                    player_guess = int(input("Pick an integer number between {} and {}: ".format(numbers_range[0], numbers_range[1])))
                    if ((player_guess <  numbers_range[0]) or (player_guess > numbers_range[1])):
                        raise IndexError ("Your guess is OUT of the guessing numbers range!")
                                    
                except ValueError:
                    print("Please enter a valid integer number!!!\n")
                    continue
                except IndexError as err:
                    print(err)
                    print("Please try again!\n")
                    continue
                else:
                    tries_counter += 1                                    
                    if player_guess < randomized_number:
                        print("It is higher!")                        
                        continue
                        
                    elif player_guess > randomized_number:
                        print("It is lower!")                        
                        continue
                    else:
                        print("-----> You got it! it took you {} tries.".format(tries_counter))
                        if (tries_counter < highest_score or highest_score == -1):
                            print("Youuu have hit the HIGHEST SCORE")
                            highest_score = tries_counter
                            
                    play_again = input("Would you like to play again? [y]es/[n]o: ")
                    if play_again.lower() == "y":
                        print("\n\nThe HIGHSCORE is ", highest_score)
                        randomized_number = set_new_play(numbers_range)                                      
                        continue
                    else:
                        print("Quitting...Hope to see you soon!")
                        gamming_on = False
                        break                                       
                                       
if __name__ == '__main__':
    # Game Kicks off by calling the start_game function.
    
    start_game()
