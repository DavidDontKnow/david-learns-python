import random


def get_choices():
    player_choice = input("Enter a choice: Rock Paper or Scissors, ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices


def check_win(player, computer):
    print(f"You chose: {player}, computer chose: {computer}")
    if player == computer:
        return ("It is a tie")
    elif player == "rock":
        if computer == "scissors":
            return "Player Wins!"
        else:
            return "Computer Wins!"
    elif player == "paper":
        if computer == "rock":
            return "Player Wins!"
        else:
            return "Computer Wins!"
    elif player == "Scissors":
        if computer == "paper":
            return "Player Wins!"
        else:
            return "Computer Wins!"


def play_again():
    answer = input("Do you want to play again? y/n:")
    if answer == "y":
        start_game()
    else:
        print("Thank you for playing!")


def start_game():
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)
    play_again()


start_game()
