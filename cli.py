
from prettycli import red, blue, green
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
            self.delete()
            pass
        else:
            pass



        print(green(f"You have selected {options[menu_entry_index]}"))

    def handle_add(self, numb, uld_type):
        is_number = numb.isdigit()
        if is_number:
            selection = len(numb)
            if selection == 4:
                Uld.add_uld(numb, uld_type)
                self.clear_screen(44)
                self.start()
                print("acceptable")
                pass
            else:
                print(red("input 4 digit ULD number"))
                self.add()

    def delete(self):
        print("in delete")
        pass
        
    def add(self):
        print("Select ULD type:\n")
        options = ["AAX", "LAY", "DQF", "AKE"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        uld_type = options[menu_entry_index]
        uld_numb = input("Type ULD Number:")

        self.handle_add(uld_numb,uld_type)

        print(green(f"You have selected {options[menu_entry_index]}"))
        #Uld.add_uld(uld_numb, options[menu_entry_index])

        #self.clear_screen(44)
        #handle is this selection correct. displays selected uld, back, exit
        #print("Type ULD ID:\n\n")
        #uld = input("Type ULD ID:\n\n")

        #take input of uld id 
        #handle uld and persist into db
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