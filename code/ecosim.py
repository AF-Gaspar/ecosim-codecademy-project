# This is the main ecosystem simulation file

from menu import *

def main():
    # Define menu options
    main_menu_dict = {1: 'Config',
             2: 'Creatures',
             3: 'Run Sim',
             'name': 'Main'}

    config_menu_dict = {1: 'Show Config',
                2: 'Edit Config',
                3: 'Load Config',
                4: 'Save Config',
                5: 'Back',
                'name': 'Configuration'}

    creature_menu_dict = {1: 'Show Creatures',
                2: 'Edit Creatures',
                3: 'Load Creatures',
                4: 'Save Creatures',
                5: 'Back',
                'name': 'Creatures'}

    run_menu_dict = {1: 'Run Simulation',
                2: 'Back',
                'name': 'Run'}

    # Define all the menus as Menu classes
    main_menu = Menu(main_menu_dict)
    config_menu = Menu(config_menu_dict)
    creature_menu = Menu(creature_menu_dict)
    run_menu = Menu(run_menu_dict)

    sub_menu_dict = {1: config_menu,
                     2: creature_menu,
                     3: run_menu}

    while True:
        # Display main menu
        main_menu.print_menu()
        sub_menu = sub_menu_dict[main_menu.menu_input()]
        # Display sub menu
        sub_menu.print_menu()
        sub_choice = sub_menu.menu_input()
        if sub_menu.back_test(sub_choice):
            print("Going back to main menu.")
        else:
            print("You selected ", str(sub_choice))

main()