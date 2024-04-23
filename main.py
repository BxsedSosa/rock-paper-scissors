"""Program Imports"""

import json
import sys

from os import system
from random import randint
from pyfiglet import Figlet

VALID_LANGUAGE = ["en", "es"]

VALID_CHOICES = {
    "rock": ["1", "r", "rock"],
    "paper": ["2", "p", "paper"],
    "scissors": ["3", "s", "scissors"],
}

VALID_WINS = (["Rock", "Scissors"], ["Paper", "Rock"], ["Scissors", "Paper"])

VALID_RETRY = ["y", "yes"]

with open("text.json", "r", encoding="utf-8") as file:
    MSG = json.load(file)


def clear_console():
    """Clears console"""
    system("clear")


def display_welcome():
    """Displays welcome to console"""
    sign = Figlet(font="slant")
    print(sign.renderText("Welcome"))
    print("======================================================\n")


def display_title():
    """Display title to console"""
    sign = Figlet(font="slant")
    print(sign.renderText(MSG[language]["intro"]))
    print("======================================================\n")


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


def validate_language():
    """Validates user input of language selection"""
    selected_language = input(prompt(MSG["en"]["questions"]["select-lang"])).lower()

    while selected_language not in VALID_LANGUAGE:
        selected_language = input(prompt(MSG["en"]["errors"]["select-lang"])).lower()

    return selected_language


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
    return result


def ask_retry():
    """Gives user option to retry another game"""
    valid_answer = ["y", "yes", "n", "no"]
    user_answer = input(prompt(MSG[language]["questions"]["retry"])).lower()

    while user_answer not in valid_answer:
        user_answer = input(prompt(MSG[language]["errors"]["retry"])).lower()

    return user_answer


def main():
    """Main Function"""
    player1 = ask_user_choice(prompt(MSG[language]["questions"]["user-choice"]))
    computer = get_cpu_choice()
    result = get_winner(player1, computer)
    print(prompt(result))


clear_console()
display_welcome()
language = validate_language()

while True:

    clear_console()
    display_title()
    main()

    retry = ask_retry()
    if retry not in VALID_RETRY:
        sys.exit()
