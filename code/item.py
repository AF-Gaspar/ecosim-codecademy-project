#This is the item class that is used in the menu class

class Item:
    def __init__(self, name, function, parent=None):
        self.name = name
        self.function = function
        self.parent = parent
        if parent:
            parent.add_item(self)

    def print_item(self):
        print(" " + self.name)