class GonatoProfile:
    """Gonato's class profile with menu options."""

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def greet(self, message="\nHi champ! What's poppin?"):
        print(message)
        print(f"Hi! My name is {self.name}.")

    def show_info(self):
        print("\n--- Basic Information About Alexa ---")
        print(f"My age is {self.age}.")
        print(f"And I am from the course {self.course}.")
        print("I live in Pembo, Taguig City.")

    def my_goal(self):
        print("\n--- Alexa's Goals ---")
        print("My goal is to become a professional F1 racer.")

    def share_hobby(self):
        print("\n--- Alexa's Hobbies ---")
        print("I love wandering at night.")
        print("I love to read e-Books.")

    def say_quote(self):
        print("\n--- Alexa's Favorite Quotes ---")
        print("• “Ride your own race.”")
        print("• “You only live once.”")
        print("• “Fall seven times. Stand up eight.”")

    def menu(self):
        choice = ""
        while choice != "0":
            choice = self.display_get_choice()

    def display_get_choice(self):
        print("\n+++ Alexa's Menu +++")
        print("1. Greetings")
        print("2. Basic Information")
        print("3. Goals in Life")
        print("4. Hobbies")
        print("5. Favorite Quotes")
        print("0. Back to Main Menu")

        menu_choice = input("Enter your choice: ").strip()

        match menu_choice:
            case "1":
                self.greet()
                return "1"
            case "2":
                self.show_info()
                return "2"
            case "3":
                self.my_goal()
                return "3"
            case "4":
                self.share_hobby()
                return "4"
            case "5":
                self.say_quote()
                return "5"
            case "0":
                print("\nReturning to main menu...")
                return "0"
            case _:
                print("\nInvalid choice. Please try again.")
                return ""