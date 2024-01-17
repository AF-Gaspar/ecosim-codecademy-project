#This is the configuration class that reads in and stores the simulation configuration

from input_scrub import *

class Configuration:
    def __init__(self, steps = 1000, mass = 1000, length = 100, width = 100):
        self.config = {'steps':steps,
                       'mass':mass,
                       'length':length,
                       'width':width}
        self.organisms = []

    def report_config(self):
        #This method prints out the current config settings
        print('Simulation steps = ' + str(self.config['steps']))
        print('Total available biomass = ' + str(self.config['mass']))
        print('Field size L x W = ' + str(self.config['length']) + ' x ' + str(self.config['width']))
        print('Starting organisms are:')
        for organism in self.organisms:
            print(organism)

    def edit_config(self):
        #This file loops through the integer settings allowing the user to change them.
        for key in self.config.keys():
            print('Enter new value for ' + key + ":")
            new = input_scrub_int()
            if new > 0:
                self.config[key] = new
            else:
                print('Input failed, no change made.')
