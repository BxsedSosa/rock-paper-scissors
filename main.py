"""Program Imports"""

import json
import sys

from os import system
from random import randint
from pyfiglet import Figlet


with open("text.json", "r", encoding="utf-8") as file:
    MSG = json.load(file)


def clear_console():
    """Clears console"""
    system("clear||cls")


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


def get_random_choice():
    """Gets random number for picking choice"""
    return randint(1, 5)


def get_cpu_choice():
    """Gets random choice from cpu"""
    cpu_choice = validate_choice(str(get_random_choice()))
    return cpu_choice


def ask_language():
    """Validates user input of language selection"""
    valid_language = ["en", "es"]
    selected_language = input(prompt(MSG["en"]["questions"]["select-lang"])).lower()

    while selected_language not in valid_language:
        selected_language = input(prompt(MSG["en"]["errors"]["select-lang"])).lower()

    return selected_language


def validate_choice(choice):
    """Validates users and cpu input"""
    valid_choices = MSG[language]["choices"]
    answer = list(MSG[language]["choices"].items())
    rock = answer[0][1][0]
    paper = answer[1][1][0]
    scissors = answer[2][1][0]
    lizard = answer[3][1][0]
    spock = answer[4][1][0]

    if choice in valid_choices["rock"]:
        return rock.capitalize()

    if choice in valid_choices["paper"]:
        return paper.capitalize()

    if choice in valid_choices["scissors"]:
        return scissors.capitalize()

    if choice in valid_choices["lizard"]:
        return lizard.capitalize()

    if choice in valid_choices["spock"]:
        return spock.capitalize()

    while True:
        inner_choice = input(prompt(MSG[language]["errors"]["user-choice"])).lower()
        for key in valid_choices.values():
            for value in key:
                if inner_choice == value:
                    return validate_choice(inner_choice)


def ask_user_choice(text):
    """Asks user for input for choice"""
    user_choice = validate_choice(input(text).lower())
    print()
    return user_choice


def get_winner(choice1, choice2):
    """Checks who the winner is"""
    valid_wins = list(MSG[language]["wins"].values())
    choices = [choice1, choice2]

    for wins in valid_wins:
        for win in wins:
            if choices == win:
                return MSG[language]["results"]["win"]

    if choice1 == choice2:
        return MSG[language]["results"]["tie"]

    return MSG[language]["results"]["lose"]


def display_winner(choice1, choice2):
    """Gets results of if user wins/loses/ties"""
    msg_user_choice = MSG[language]["results"]["user-choice"]
    msg_cpu_choice = MSG[language]["results"]["cpu-choice"]

    print(prompt(get_winner(choice1, choice2)))
    print(f"{prompt(msg_user_choice)} {choice1}\n==> {msg_cpu_choice} {choice2}\n")


def ask_retry():
    """Gives user option to retry another game"""
    valid_retry = MSG[language]["retry"]["yes"]
    valid_answer = MSG[language]["retry"]["valid-retry"]
    user_answer = input(prompt(MSG[language]["questions"]["retry"])).lower()

    while user_answer not in valid_answer:
        user_answer = input(prompt(MSG[language]["errors"]["retry"])).lower()

    if user_answer not in valid_retry:
        print(prompt(MSG[language]["exit"]["thank"]))
        print(prompt(MSG[language]["exit"]["close"]))
        sys.exit()


def main():
    """Main Function"""
    player1 = ask_user_choice(prompt(MSG[language]["questions"]["user-choice"]))
    computer = get_cpu_choice()
    display_winner(player1, computer)


clear_console()
display_welcome()
language = ask_language()

while True:

    clear_console()
    display_title()
    main()

    ask_retry()
