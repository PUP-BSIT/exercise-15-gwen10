from gwn10package.teves import TevesProfile

def display_main_menu():
    """Displays the main team menu and gets user input."""
    print("\n++ GWN10 Team Members ++")
    print("1. Gwen Teves")
    print("0. Exit")
    
    return input("Enter your choice: ").strip()

def handle_main_choice(choice):
    """Handles the main menu user selection."""
    match choice:
        case "1":
            teves = TevesProfile("Gwen Teves", 19, "BSIT 2-1")
            teves.menu()
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
