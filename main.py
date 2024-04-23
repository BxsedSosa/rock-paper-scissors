"""Program Imports"""

import json
from os import system
from random import randint

VALID_CHOICES = {
    "rock": ["1", "r", "rock"],
    "paper": ["2", "p", "paper"],
    "scissors": ["3", "s", "scissors"],
}

VALID_WINS = (["Rock", "Scissors"], ["Paper", "Rock"], ["Scissors", "Paper"])

with open("text.json", "r", encoding="utf-8") as file:
    MSG = json.load(file)


def clear_console():
    """Clears console"""
    system("clear")


def prompt(text):
    """Gives output with arrows to start"""
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
        return "Rock"

    if choice in VALID_CHOICES["paper"]:
        return "Paper"

    if choice in VALID_CHOICES["scissors"]:
        return "Scissors"

    while True:
        inner_choice = input(prompt(MSG[language]["errors"]["user-choice"])).lower()
        for key in VALID_CHOICES.items():
            for value in key[1]:
                if inner_choice == value:
                    return validate_choice(inner_choice)


def ask_user_choice(text):
    """Asks user for input for choice"""
    user_choice = validate_choice(input(text).lower())
    print()
    return user_choice


def get_winner(choice1, choice2):
    """Gets results of if user wins/loses/ties"""
    choices = [choice1, choice2]
    msg_user_choice = MSG[language]["results"]["user-choice"]
    msg_cpu_choice = MSG[language]["results"]["cpu-choice"]

    if choices in VALID_WINS:
        result = MSG[language]["results"]["win"]
    if choice1 == choice2:
        result = MSG[language]["results"]["tie"]
    else:
        result = MSG[language]["results"]["lose"]

    print(f"{prompt(msg_user_choice)} {choice1}\n==> {msg_cpu_choice} {choice2}")
    print(prompt(result))


def main():
    """Main Function"""
    clear_console()
    player1 = ask_user_choice(prompt(MSG[language]["questions"]["user-choice"]))
    computer = get_cpu_choice()
    get_winner(player1, computer)


LANGUAGE = "en"
main()
