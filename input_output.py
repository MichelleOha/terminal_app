import json
import os
from brand import brand
from item import Item

# Deals with user input and terminal output


class InputOutput:
    def __init__(self, user_input, user_output):
        self.user_input = user_input
        self.user_output = user_output


def welcome_menu():
    print("Welcome to My Wardrobe. Please select what you would like to do from the following:   ")
    print("1. Add a new label and item to your wardrobe")
    print("2. Updated items in your wardrobe")
    print("3. Delete an item in you wardrobe")
    print("4. View my wardrobe")
    print("5. Reset your wardrobe")
    print("6. Quit")

    def create_new_brand():
        os.system('clear')
        print(f"Please enter the name of the brand:{self.name}")
        name = user_input
        print(
            f"Please enter the country where purchased:{self.country_of_origin} ")
        country_of_origin = user_input
