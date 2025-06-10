from gwn10package.teves import TevesProfile

def main_menu():
    """Main program to display team member profiles."""
    print("\n++ GWN10 Team Members ++")
    print("1. Gwen Teves")
    print("0. Exit")
    return input("Enter your choice: ").strip()

# Main program loop to display the main menu and handle user choices
while True:
    choice = main_menu()

    match choice: # Using match-case for better readability
        case "1":
            teves = TevesProfile("Gwen Teves", 19, "BSIT 2-1")
            teves.menu()
        case "0":
            print("\nExiting the program...")
            break
        case _:
            print("\nInvalid choice. Please try again.")
