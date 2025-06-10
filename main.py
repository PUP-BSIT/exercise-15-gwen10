from gwn10package.teves import TevesProfile
from gwn10package.bataller import BatallerProfile
from gwn10package.gonato import GonatoProfile

def main_menu():
    """Main program to display team member profiles."""
    print("\n++ GWN10 Team Members ++")
    print("1. Gwen Teves")
    print("2. Christian Bataller")
    print("3. Alexa Gonato")
    print("0. Exit")
    
    return input("Enter your choice: ").strip()

# Main program loop to display the main menu and handle user choices
while True:
    choice = main_menu()

    match choice: # Using match-case for better readability
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
        case "0":
            print("\nExiting the program...")
            break
        case _:
            print("\nInvalid choice. Please try again.")
