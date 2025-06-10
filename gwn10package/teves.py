class TevesProfile:
    """Teves' class profile with menu options."""

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def greet(self, message="\nWhat's up, madlang people!!"):
        print(message)
        print(f"Hi! My name is {self.name}.")

    def show_info(self):
        print("\n--- Basic Information About Gwen ---")
        print(f"My age is {self.age}.")
        print(f"And I am from the course {self.course}.")
        print("I live in Taguig City.")

    def my_goal(self):
        print("\n--- Gwen's Goals ---")
        print("My goal is to become an expert programmer",
              "and have a peaceful life.")

    def share_hobby(self):
        print("\n--- Gwen's Hobbies ---")
        print("I love sleeping and night walks.")
        print("I love to read books of wisdom.")

    def say_quote(self):
        print("\n--- Gwen's Favorite Quotes ---")
        print("• “Do something today that your future self", 
              "will thank you for.”")
        print("• “Failure is success in progress.”")

    def menu(self):
        while True:
            print("\n+++ Gwen's Menu +++")
            print("1. Greetings")
            print("2. Basic Information")
            print("3. Goals in Life")
            print("4. Hobbies")
            print("5. Favorite Quotes")
            print("0. Back to Main Menu")

            choice = input("Enter your choice: ").strip()

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
                    break
                case _:
                    print("\nInvalid choice. Please try again.")
