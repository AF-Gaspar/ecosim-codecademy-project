#This is the creature class for critters in the ecosim

class Creature:
    def __init__(self, location = [0,0], mass = 100, metabolism = 10):
        self.location = location
        self.age = 0
        self.mass = mass
        self.metabolism = metabolism
        self.is_alive = True

    def consume(self, mass):
        pass

    def excrete(self, mass):
        pass

    def metabolize(self):
        pass

    def move(self):
        pass

    def die(self):
        pass

    def decompose(self):
        pass

    def reproduce(self):
        pass

    def think(self):
        pass
