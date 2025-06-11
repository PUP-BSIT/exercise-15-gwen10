class BatallerProfile:
    """Bataller's class profile with menu options."""

    def __init__(self, name, level, course):
        self.name = name
        self.level = level
        self.course = course

    def greet(self):
        print("\nHello, world!")
        print(f"Hey there! I'm {self.name}.")

    def show_info(self):
        print("\n--- About Bataller ---")
        print(f"My current level is {self.level}.")
        print(f"I'm studying {self.course}.")
        print("Currently live in Taguig City.")

    def my_goal(self):
        print("\n--- My Ambitions ---")
        print("I aim to master programming and contribute to tech innovation.")

    def share_hobby(self):
        print("\n--- My Favorite Activities ---")
        print("I enjoy deep conversations and exploring new ideas.")
        print("I also appreciate relaxing walks under the night sky.")

    def say_quote(self):
        print("\n--- My Favorite Quotes ---")
        print(" “Strive for progress, not perfection.”")
        print(" “Success is built on the foundation of perseverance.”")

    def display_menu(self):
        print("\n+++ Bataller's Menu +++")
        print("1. Greetings")
        print("2. Personal Information")
        print("3. Ambitions")
        print("4. Favorite Activities")
        print("5. Inspirational Thoughts")
        print("0. Back to Main Menu")

    def handle_choice(self, choice):
        match choice:
            case "1":
                self.greet()
            case "2":
                self.show_info()
            case "3":
                self.my_goal()
            case "4":
                self.share_hobby()
            case "5":
                self.say_quote()
            case "0":
                print("\nReturning to main menu...")
                return False
            case _:
                print("\nInvalid choice. Please try again.")
        return True

    def menu(self):
        """Main menu loop."""
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()
            if not self.handle_choice(choice):
                break
