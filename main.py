"""Program Imports"""

import json
from os import system
from random import randint

VALID_CHOICES = {
    "rock": ["1", "r", "rock"],
    "paper": ["2", "p", "paper"],
    "scissors": ["3", "s", "scissors"],
}

VALID_WINS = (["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"])

with open("text.json", "r", encoding="utf-8") as file:
    MSG = json.load(file)


def clear_console():
    """Clears console"""
    system("clear")


def prompt(text):
    return f"==> {text}"


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
            """If choice is not valid it will check all the values in the VALID_CHOICES"""
            inner_choice = input("Try Again: \n").lower()
            for key in VALID_CHOICES:
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
        return MSG[language]["results"]["win"]
    if choice1 == choice2:
        return MSG[language]["results"]["tie"]
    else:
        return MSG[language]["results"]["lose"]


def main():
    """Main Function"""

    msg_user_choice = MSG[language]["results"]["user-choice"]
    msg_cpu_choice = MSG[language]["results"]["cpu-choice"]

    clear_console()
    player1 = ask_user_choice(prompt(MSG[language]["questions"]["user-choice"]))
    computer = get_cpu_choice()
    results = get_winner(player1, computer)
    print(prompt())
    print(prompt(results))


language = "en"
main()
