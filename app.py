#import the random module
import random

#create a variable to store the user's score
user_score = 0
#create a variable to store the computer's score
computer_score = 0
#create a variable to store the number of rounds played
rounds_played = 0


#create a function to randomly select an option from a list of options
def get_random_option():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

# Path: app.py
#create a function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    #create a variable to store the winner
    winner = None
    #create a condition to determine if the game is a tie
    if user_choice == computer_choice:
        winner = "Tie"
    #create a condition to determine if the user wins
    elif user_choice == "rock":
        if computer_choice == "paper":
            winner = "Computer"
        elif computer_choice == "scissors":
            winner = "User"
    #create a condition to determine if the user wins
    elif user_choice == "paper":
        if computer_choice == "rock":
            winner = "User"
        elif computer_choice == "scissors":
            winner = "Computer"
    #create a condition to determine if the user wins
    elif user_choice == "scissors":
        if computer_choice == "rock":
            winner = "Computer"
        elif computer_choice == "paper":
            winner = "User"
    #return the winner
    return winner

#create a function to welcome the user to the game
def welcome():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    #print("The first player to win 2 out of 3 rounds wins the game.")
    print("Good luck!")
    print(" ")

#create a function to get the user's choice
def get_user_choice():
    #create a variable to store the user's choice
    user_choice = input("Enter your choice: ").lower()
    #create a condition to check if the user's choice is valid
    if user_choice in ["rock", "paper", "scissors"]:
        return user_choice
    #create a condition to check if the user's choice is not valid
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()

#create a function to start the game
def start_game():
    global user_score, computer_score, rounds_played

    #create a condition to check if the number of rounds played is less than 3
    #while rounds_played < 3:
    #call the get_user_choice function and store the user's choice
    user_choice = get_user_choice()
    #call the get_random_option function and store the computer's choice
    computer_choice = get_random_option()
    #call the determine_winner function and store the winner
    winner = determine_winner(user_choice, computer_choice)
    #create a condition to check if the game is a tie
    if winner == "Tie":
        print("It was a tie!")
    #create a condition to check if the user wins
    elif winner == "User":
        print("You won this time!")
        #increment the user's score
        user_score += 1
    #create a condition to check if the computer wins
    elif winner == "Computer":
        print("The computer won this time!")
        #increment the computer's score
        computer_score += 1
    #increment the number of rounds played
    rounds_played += 1
    #print the user's score
    print("Your score: " + str(user_score))
    #print the computer's score
    print("Computer score: " + str(computer_score))
    #print the number of rounds played
    print("Rounds played: " + str(rounds_played))
    print(" ")
        
    #call the play_again function
    play_again()


# create a function to ask the user if they want to play again
def play_again():
    #create a variable to store the user's choice
    user_choice = input("Do you want to play again? (y/n): ").lower()
    #create a condition to check if the user wants to play again
    if user_choice == "y":
        #call the start_game function
        start_game()
    #create a condition to check if the user does not want to play again
    elif user_choice == "n":
        print(" ")
        #print a message to the user
        #create a condition to check if the user wins the game
        if user_score > computer_score:
            print("You won!")
        #create a condition to check if the computer wins the game
        elif computer_score > user_score:
            print("The computer won!")
        #create a condition to check if the game is a tie
        else:
            print("It is a tie!")

        print("Your score: " + str(user_score))
        #print the computer's score
        print("Computer score: " + str(computer_score))
        #print the number of rounds played
        print("Rounds played: " + str(rounds_played))
        print(" ")
        print("Thanks for playing!")
    #create a condition to check if the user's choice is not valid
    else:
        print("Invalid choice. Please try again.")
        #call the play_again function
        play_again()


#call the welcome function
welcome()

#call the start_game function
start_game()