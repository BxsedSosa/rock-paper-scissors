"""File Imports"""

from time import sleep
from os import system
from random import randint
from pyfiglet import Figlet

VALID_CHOICES = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors",
}

VALID_WINS = [
    ["Rock", "Scissors"],
    ["Paper", "Rock"],
    ["Scissors", "Paper"],
]


def clear_console():
    """Clears console"""
    system("clear||cls")


class Display:

    def __init__(self, text):
        self.text = text

    def logo(self):
        """Displays ASCII welcome"""
        sign = Figlet(font="slant")
        print(sign.renderText(f"{self.text}"))
        print("======================================================\n")


class Game:

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.player_wins = 0
        self.computer_wins = 0

    def get_result(self):
        choices = [self.player, self.computer]

        if choices in VALID_WINS:
            self.player_wins += 1
            return f"Player wins"

        self.computer_wins += 1
        return "Computer wins"

    def display_result(self):
        print(f"The score is Player: {self.player_wins} Computer: {self.computer_wins}")

        while self.player_wins < 5 and self.computer_wins < 5:
            return True

        return False


class Player:

    def __init__(self, choice):
        self.choice = choice

    def choice_validation(self):
        if self.choice in VALID_CHOICES:
            print(f"You chose: {VALID_CHOICES.get(self.choice)}")
            return VALID_CHOICES.get(self.choice)

        while self.choice not in VALID_CHOICES:
            self.choice = input(f"Please enter a valid option!\n")

        print(f"You chose: {VALID_CHOICES.get(self.choice)}")
        return VALID_CHOICES.get(self.choice)


class Computer(Player):

    def __init__(self):
        self.choice = 0

    def random_choice(self):
        return randint(1, 3)

    def cpu_choice(self):
        computer_choice = str(Computer.random_choice(self))

        if computer_choice in VALID_CHOICES:
            print(
                f"This is what the Computer choose: {VALID_CHOICES.get(computer_choice)}"
            )
            return VALID_CHOICES.get(computer_choice)


welcome = Display("Welcome")
rps_logo = Display("Rock, Paper, Scissors")


def main():
    clear_console()
    rps_logo.logo()
    player = Player(input("What is your choice?\n"))
    computer = Computer()

    player_choice = player.choice_validation()
    cpu_choice = computer.cpu_choice()
    result = Game(player_choice, cpu_choice)
    print(result.get_result())

    while True:

        result.display_result()


clear_console()
welcome.logo()
sleep(1)

main()
