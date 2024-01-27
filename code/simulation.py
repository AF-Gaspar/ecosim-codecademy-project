#This is the main simulation file that contains the configuration and creatures

class Simulation:
    def __init__(self, config, creatures = None):
        self.config = config
        self.creatures = creatures or []
        self.width = 0
        self.length = 0
        self.step = 0
        self.max_step = 0
        self.map = []

    def consume_config(self):
        self.max_step = self.config.config['steps']
        self.length = self.config.config['length']
        self.width = self.config.config['width']
        self.map = [[0 for x in range (self.width)] for y in range(self.length)]

        unused_mass = self.config.config['mass']
        while unused_mass > 0:
            for l in range(self.length):
                for w in range(self.width):
                    self.map[l][w] += 1
                    unused_mass -= 1

        for creature in self.creatures:
            creature.location = [int(self.width/2),int(self.length/2)]

    def simulate_step(self):
        for creature in self.creatures:
            local = []
            if creature.location[0] > 0:
                local.append(self.map[creature.location[0]-1][creature.location[1]])
            if creature.location[1] > 0:
                local.append(self.map[creature.location[0]][creature.location[1]-1])
            if creature.location[0] < self.width-1:
                local.append(self.map[creature.location[0]+1][creature.location[1]])
            if creature.location[1] < self.length-1:
                local.append(self.map[creature.location[0]][creature.location[1]+1])
            self.map[creature.location[0]][creature.location[1]] = creature.think()
        self.step += 1

    def run_sim(self):
        self.consume_config()
        while self.step < self.max_step:
            self.simulate_step()
            print('Running step: ' + str(self.step))
