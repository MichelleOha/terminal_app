import os
from item import Item
from input_output import InputOutput


class Main:

    def __init__(self, input_output):
        self.input_output = input_output
        self.running = True

    def app(self):

        while self.running:
            self.input_output.welcome_menu()
            # class and method then save it to a variable
            # method waits for input from user and I capture it menu_selection and store it
            menu_selection = self.input_output.user_input()
            if menu_selection == "6":
                self.running = False


main = Main(InputOutput)
main.app()
