from simulation import *
from configuration import *

config = Configuration()
sim = Simulation()

sim.consume_config(config)

print(sim.map)