#This is the menu class that controls the user interface

class Menu:
    def __init__(self, name, items=None):
        self.name = name
        self.items = items or []

    def add_item(self, item):
        self.items.append(item)
        if item.parent != self:
            item.parent = self

    def remove_item(self, item):
        self.items.remove(item)
        if item.parent == self:
            item.parent = None
    
    def print_menu(self):
        #This function takes a menu key and prints that menu from the dictionary
        print(self.name)
        for item in self.items:
            item.print_item()

    def show_menu(self):
        while True:
            self.print_menu()
            while True:
                user_choice = input("Enter choice>")
                try:
                    if int(user_choice) > 0 and int(user_choice) <= len(self.items):
                        break
                    else:
                        print("Bad choice.")
                except:
                    print("Bad input.")
            self.items[int(user_choice)-1].function()