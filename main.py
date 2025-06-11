from gwn10package.teves import TevesProfile
from gwn10package.bataller import BatallerProfile
from gwn10package.gonato import GonatoProfile
from gwn10package.sario import SarioProfile

def display_main_menu():
    """Displays the main team menu and gets user input."""
    print("\n++ GWN10 Team Members ++")
    print("1. Gwen Teves")
    print("2. Bataller")
    print("3. Alexa Gonato")
    print("4. Gerald Sario")
    print("0. Exit")
    
    return input("Enter your choice: ").strip()

def handle_main_choice(choice):
    """Handles the main menu user selection."""
    match choice:
        case "1":
            teves = TevesProfile("Gwen Teves", 19, "BSIT 2-1")
            teves.menu()
        case "2":
            bataller = BatallerProfile(
                "Christian Bataller",
                "2nd year",
                "BSIT"
            )
            bataller.menu()
        case "3":
            gonato = GonatoProfile("Alexa Gonato", 20, "BSIT 2-1")
            gonato.menu()
        case "4":
            sario = SarioProfile("Gerald Sario", 20, "BSIT")
            sario.menu()
        case "0":
            print("\nExiting the program...")
            return False
        case _:
            print("\nInvalid choice. Please try again.")
    return True

# MAIN LOOP
while True:
    choice = display_main_menu()
    if not handle_main_choice(choice):
        break
