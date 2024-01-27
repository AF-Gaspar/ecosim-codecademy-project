#This is the creature class for critters in the ecosim

class Creature:
    def __init__(self, location = [0,0], mass = 100, metabolism = .2):
        self.location = location
        self.age = 0
        self.mass = mass
        self.metabolism = metabolism
        self.is_alive = True

    def excrete(self):
        return int(self.mass * self.metabolism)

    def metabolize(self):
        self.mass -= int(self.mass * self.metabolism)
        self.age += 1
        return self.excrete()
    
    def consume(self, creature):
        self.mass += creature.die()
        creature.mass = 0
        return self.metabolize()

    def move(self, velocity):
        self.location[0] += velocity[0]
        self.location[1] += velocity[1]
        return self.metabolize()

    def die(self):
        self.is_alive = False
        return self.mass

    def reproduce(self):
        baby = Creature(self.location, int(self.mass*.1), self.metabolism)
        self.mass -= int(self.mass*.1)
        return baby, self.metabolize()

    def think(self, local = []):
        if self.mass < self.metabolism * 500:
            for item in local:
                if item is Creature:
                    return self.consume(item)
                elif item is int and item > 0:
                    self.mass += item
                    item = 0
                    return self.metabolize()
        elif self.mass > self.metabolism * 1000:
            pass
        else:
            return self.metabolize()
