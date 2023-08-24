
from prettycli import red, blue, green
from simple_term_menu import TerminalMenu
from models import Uld

class Cli():


    def start(self):

        #self.clear_screen(44)

        print(blue("Welcome to ULD Manager"))
        options = ["List All ULD", "Find ULD", "Update ULD", "Add ULD", "Delete ULD", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Add ULD":
            self.add()

        elif options[menu_entry_index] == "List All ULD":
            self.list()

        elif options[menu_entry_index] == "Find ULD":
            self.find()
            pass

        elif options[menu_entry_index] == "Delete ULD":
            self.delete()

        elif options[menu_entry_index] == "Update ULD":
            self.handle_update()
            pass
        else:
            #exit app
            pass



        print(green(f"You have selected {options[menu_entry_index]}"))

    def handle_add(self, numb, uld_type):
        is_number = numb.isdigit()
        if is_number:
            selection = len(numb)
            if selection == 4:
                Uld.add_uld(numb, uld_type)
                self.start()
                print("acceptable")
                pass
            else:
                print(red("input 4 digit ULD number"))
                self.add()
    
    def handle_update(self):
        print("in handle update")
        print("Select ULD type:\n")
        options = ["AAX", "LAY", "DQF", "AKE", "Main Menu"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        uld_type = options[menu_entry_index]
        if options[menu_entry_index] == "Main Menu":
            self.start()
        else:
            uld_numb = input("Type ULD Number:\n")
            self.handle_update_selection(uld_numb, uld_type )
        pass

    def handle_update_selection(self,uld_numb,uld_type):
        #selection to update uld_name, caster_deck, status
        self.clear_screen(44)
        print("What would you like to update:\n")
        options = ["Uld Name", "Caster Deck", "Status", "Main Menu"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        uld_selection = options[menu_entry_index]
        
        self.clear_screen(44)
        if uld_selection == "Uld Name":
            pass
            Uld.handle_name_change(uld_numb,uld_type)
        elif uld_selection == "Caster Deck":
            Uld.handle_caster_change(uld_numb,uld_type)
            pass
        elif uld_selection == "Status":
            Uld.handle_uld_status(uld_numb,uld_type)
        elif uld_selection == "Main Menu":
            self.start()
        else: 
            self.clear_screen(44)
            self.start()            
        pass
        self.start()

    def delete(self):
        print("Select ULD type:\n")
        options = ["AAX", "LAY", "DQF", "AKE", "Main Menu"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        uld_type = options[menu_entry_index]
        

        if options[menu_entry_index] == "Main Menu":
            self.start()
        else:
            uld_numb = input("Type ULD Number:")
            Uld.delete_uld(uld_numb, uld_type)
        self.start()
        pass
        
    def add(self):
        print("Select ULD type:\n")
        options = ["AAX", "LAY", "DQF", "AKE", "Main Menu"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        uld_type = options[menu_entry_index]
        if options[menu_entry_index] == "Main Menu":
            self.start()
        else:
            uld_numb = input("Type ULD Number:")
            self.handle_add(uld_numb,uld_type)

        print(green(f"You have selected {options[menu_entry_index]}"))

    def find(self):
        self.clear_screen(44)
        print(blue("Select ULD type:\n"))
        options = ["AAX", "LAY", "DQF", "AKE", "Main Menu"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        uld_type = options[menu_entry_index]
        if options[menu_entry_index] == "Main Menu":
            self.start()
        else:
            uld_numb = input("Type ULD Number:")
            self.clear_screen(44)
            Uld.find(uld_numb,uld_type)
            self.start()
    
    def list(self):
        self.clear_screen(44)
        print(blue("List of all ULDs"))
        print(Uld.list_uld())
        self.start()

    def change_status(self):
        self.clear_screen(44)
        print(blue("Select ULD type:\n"))
        options = ["AAX", "LAY", "DQF", "AKE"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        uld_type = options[menu_entry_index]
        uld_numb = input("Type ULD Number:")
        self.clear_screen(44)
        Uld.handle_uld_status(uld_numb, uld_type)
        self.start()
        pass

    def clear_screen(self,lines):
        print("\n" * lines)

app = Cli()
app.start()