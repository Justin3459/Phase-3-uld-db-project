
from prettycli import red, blue, green, yellow
from simple_term_menu import TerminalMenu
from models import Uld, Caster_deck
import ipdb
class Cli():


    def start(self):

        #self.clear_screen(44)

        print(blue("Welcome to ULD Manager"))
        options = ["List All ULD", "Find ULD", "Add ULD", "Delete Uld"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Add ULD":
            self.add()
        elif options[menu_entry_index] == "List All ULD":
            self.list()
            pass
        elif options[menu_entry_index] == "Find ULD":
            pass
        elif options[menu_entry_index] == "Delete ULD":
            pass
        else:
            pass



        print(green(f"You have selected {options[menu_entry_index]}"))

        
    def add(self):
        print("Select ULD type:\n")
        options = ["AAX", "LAY", "DQF", "AKE"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(green(f"You have selected {options[menu_entry_index]}"))
        
        self.clear_screen(44)
        #handle is this selection correct. displays selected uld, back, exit
        #print("Type ULD ID:\n\n")
        #uld = input("Type ULD ID:\n\n")

        #take input of uld id 
        #handle uld and persist into db
        pass

    def delete(self):
        pass

    def find(self):

        pass 
    
    def list(self):
        self.clear_screen(44)
        print(blue("List of all ULDs"))
        print(Uld.list_uld())
        self.start()


    def change_status(self):
        pass

    def clear_screen(self,lines):
        print("\n" * lines)

app = Cli()
app.start()