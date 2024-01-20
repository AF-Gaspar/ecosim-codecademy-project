#This is the main simulation file that contains the configuration and creatures

class Simulation:
    def __init__(self, config, creatures = None):
        self.config = config
        self.creatures = creatures or []

    def consume_config(self):
        pass

    def simulate_step(self):
        pass
