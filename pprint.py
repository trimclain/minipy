#!/usr/bin/env python3

import os
import subprocess
from time import sleep
from string import ascii_uppercase

LETTERS = ascii_uppercase
LAG = 0.02

# IDEA: add colors
# from colorama import Fore, Style
# print(f"{Fore.RED}Red Text Here{Style.RESET_ALL}"

def pretty_print(string: str):
    string = string.upper()
    for i in range(len(string)):
        for letter in LETTERS:
            print(string[0:i] + letter)
            sleep(LAG)
            if letter == string[i]:
                break

def pretty_print_filled_char(string: str):
    width = os.get_terminal_size()[0]
    pretty_print(string * width)

def pretty_print_all_letters():
    for letter in LETTERS:
        pretty_print_filled_char(letter)
    print("OMG, you crazy if you watched it all, HOLY SHIT!")

def print_help_menu():
    print("\n" + "*"*60)
    print("Commands:")
    print("cl, clear -- clear the screen")
    print("q, exit -- quit the program")
    print("h, help -- print this help menu")
    print("p, print -- prettily print out a text")
    print("l, loading -- see a loading with a chosen letter")
    print("a, loadall -- see a loading with every letter")
    print("*" * 60)

def prepare_for_start():
    print("Starting in 3")
    sleep(1)
    print("Starting in 2")
    sleep(1)
    print("Starting in 1")
    sleep(1)
    print("GO")
    sleep(1)

def main():
    print_help_menu()

    while True:
        input_ = input("\n" + "> ")
        if input_ == "q" or input_ == "exit":
            break

        elif input_ == "h" or input_ == "help":
            print_help_menu()

        elif input_ == "cl" or input_ == "clear":
            _ = subprocess.run(["clear"])
            print_help_menu()

        elif input_ == "p" or input_ == "print":
            text = input("Enter text: ")
            pretty_print(text)
            sleep(LAG)

        elif input_ == "l" or input_ == "loading":
            char = input("Choose a letter: ")
            prepare_for_start()
            pretty_print_filled_char(char)

        elif input_ == "a" or input_ == "loadall":
            prepare_for_start()
            pretty_print_all_letters()

        else:
            print("Unknown Command")
            sleep(LAG)

if __name__ == "__main__":
    main()
