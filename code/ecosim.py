# This is the main ecosystem simulation file

from menu import *
from item import *
from configuration import *
from simulation import *
from creature import *

def test_function():
    print("Test")

def main():
    org1 = Creature()
    config = Configuration()
    sim = Simulation([org1])
    main_menu = Menu("Main Menu")

    # Define sub menus

    config_menu_items = [Item("1: Show Config",config.report_config),
                         Item("2: Edit Config",config.edit_config),
                         Item("3: Load Config",test_function),
                         Item("4: Save Config",test_function),
                         Item("5: Back",main_menu.show_menu)]

    creature_menu_items = [Item("1: Show Creatures",test_function),
                           Item("2: Edit Creatures",test_function),
                           Item("3: Load Creatures",test_function),
                           Item("4: Save Creatures",test_function),
                           Item("5: Back",main_menu.show_menu)]

    run_menu_items = [Item("1: Run simulation",sim.run_sim(config)),
                      Item("2: Back",main_menu.show_menu)]
    
    config_menu = Menu("Configuration Menu", config_menu_items)
    creature_menu = Menu("Creature Menu", creature_menu_items)
    run_menu = Menu("Run Menu", run_menu_items)

    # Define the main menu

    main_menu.add_item(Item("1) Config",config_menu.show_menu))
    main_menu.add_item(Item("2) Creatures",creature_menu.show_menu))
    main_menu.add_item(Item("3) Run Sim",run_menu.show_menu))
    main_menu.add_item(Item("4) Quit", quit))

    while True:
        # Display menu
        main_menu.show_menu()

if __name__ == "__main__":
    main()