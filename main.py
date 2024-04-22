"""Program Imports"""

from os import system
from random import randint

VALID_CHOICES = {
    "rock": ["1", "r", "rock"],
    "paper": ["2", "p", "paper"],
    "scissors": ["3", "s", "scissors"],
}

VALID_WINS = (["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"])

language = "en"


def clear_console():
    """Clears console"""
    system("clear")


def random_choice():
    """Gets random number for picking choice"""
    return randint(1, 3)


def get_cpu_choice():
    """Gets random choice from cpu"""
    cpu_choice = validate_choice(str(random_choice()))
    return cpu_choice


def validate_choice(choice):
    """Validates users and cpu input"""
    if choice in VALID_CHOICES["rock"]:
        return "rock"
    elif choice in VALID_CHOICES["paper"]:
        return "paper"
    elif choice in VALID_CHOICES["scissors"]:
        return "scissors"
    else:

        while True:
            inner_choice = input("Try Again: \n").lower()
            for key in VALID_CHOICES.keys():
                for value in VALID_CHOICES[key]:
                    if inner_choice == value:
                        return validate_choice(inner_choice)
                    else:
                        continue


def ask_user_choice(text):
    """Asks user for input for choice"""
    user_choice = validate_choice(input(text).lower())
    return user_choice


def get_winner(choice1, choice2):
    """Gets results of if user wins/loses/ties"""
    choices = [choice1, choice2]
    print("get_winner print:", choices)
    if choices in VALID_WINS:
        return f"You win!"
    if choice1 == choice2:
        return f"It's a tie"
    else:
        return f"You Lose"


def main():
    """Main Function"""
    clear_console()
    p1 = ask_user_choice("What do you pick?\n")
    cpu = get_cpu_choice()
    print(f"P1 choose: {p1}")
    print(f"CPU choose: {cpu}")
    results = get_winner(p1, cpu)
    print(results)


main()
