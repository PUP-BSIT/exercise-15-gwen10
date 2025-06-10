class BatallerProfile:
    """Bataller's class profile with menu options."""

    def __init__(self, name, level, course):
        self.name = name
        self.level = level 
        self.course = course

    def welcome(self, message="\nHello, world!"):
        print(message)
        print(f"Hey there! I'm {self.name}.")

    def display_info(self):
        print("\n--- About Bataller ---")
        print(f"My current level is {self.level}.") 
        print(f"I'm studying {self.course}.")
        print("Currently live in Taguig City.")

    def ambition(self):
        print("\n--- My Ambitions ---")
        print("I aim to master programming and contribute to tech innovation.")

    def favorite_activities(self):
        print("\n--- My Favorite Activities ---")
        print("I enjoy deep conversations and exploring new ideas.")
        print("I also appreciate relaxing walks under the night sky.")

    def inspirational_thoughts(self):
        print("\n--- My Favorite Quotes ---")
        print("• “Strive for progress, not perfection.”")
        print("• “Success is built on the foundation of perseverance.”")

    def menu(self):
        # Display menu until user selects exit
        while True:
            print("\n+++ Bataller's Menu +++")
            print("1. Welcome Message")
            print("2. Personal Information")
            print("3. Ambitions")
            print("4. Favorite Activities")
            print("5. Inspirational Thoughts")
            print("0. Exit Menu")

            choice = input("Enter your choice: ").strip()

            # Process user choice
            match choice:
                case "1":
                    self.welcome()
                case "2":
                    self.display_info()
                case "3":
                    self.ambition()
                case "4":
                    self.favorite_activities()
                case "5":
                    self.inspirational_thoughts()
                case "0":
                    # Exit the menu and return to main menu
                    print("\nExiting menu...")
                    break
                    # If the user selects 0, exit the menu
                case _:
                    print("\nInvalid choice. Please try again.")
