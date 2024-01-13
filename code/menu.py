#This is the menu class that controls the user interface

class Menu:
    def __init__(self, menu_dict):
        self.menu_dict = menu_dict

    def print_menu(self):
        #This function takes a menu key and prints that menu from the dictionary
        print(self.menu_dict['name'])
        for choice_key in self.menu_dict.keys():
            if type(choice_key) is int:
                print(choice_key, '--', self.menu_dict[choice_key])

    def menu_input(self):
        #Loops until user enters a valid choice
        while True:
            choice = int(input('Enter your choice: '))
            if choice in self.menu_dict.keys():
                return choice
            else:
                print('No such choice.')

    def back_test(self, user_choice):
        #Checks if the menu selection is the string "Back"
        if self.menu_dict[user_choice] == 'Back':
            return True
        else:
            return False