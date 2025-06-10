class TevesProfile:
    """Teves' class profile with menu options."""

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def greet(self):
        print("\nWhat's up, madlang people!!")
        print(f"Hi! My name is {self.name}.")

    def show_info(self):
        print("\n--- Basic Information About Gwen ---")
        print(f"My age is {self.age}.")
        print(f"I am from the course {self.course}.")
        print("I live in Taguig City.")

    def my_goal(self):
        print("\n--- Gwen's Goals ---")
        print("My goal is to become an expert programmer",
              "and live peacefully.")

    def share_hobby(self):
        print("\n--- Gwen's Hobbies ---")
        print("I love sleeping and night walks.")
        print("I enjoy reading books of wisdom.")

    def say_quote(self):
        print("\n--- Gwen's Favorite Quotes ---")
        print("• “Do something today that your future self",
              "will thank you for.”")
        print("• “Failure is success in progress.”")

    def display_menu(self):
        print("\n+++ Gwen's Menu +++")
        print("1. Greetings")
        print("2. Basic Information")
        print("3. Goals in Life")
        print("4. Hobbies")
        print("5. Favorite Quotes")
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
