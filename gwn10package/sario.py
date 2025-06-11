class SarioProfile:
    """Sario's class profile with menu options."""
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet(self, message="\n--- Im here, Everyone!!! ---"):
        print(message)
        print(f"Hello! I am {self.name}.")

    def show_info(self):
        print("\n--- Hi, Here's my basic info!! ---")
        print(f"I am {self.age} years old.")
        print(f"I am currenty taking {self.course}")
        print(f"I live in Taguig City")

    def state_goal(self):
        print("\n--- These are my goals in life!! ---")
        print("My goal is to become a billionaire.")
        print("Travel around the world")

    def share_hobby(self):
        print("\n--- Learn about my Hobbies :P ---")
        print("I love playing online games.")
        print("i love watching K-Drama")
    
    def say_quote(self):
        print("\n--- Words I Live By ---")
        print("NO ONE IS BETTER THAN ME AND " \
               "I AM BETTER THAN NO ONE")
        
    def display_menu(self):
        print("\n+++ Gerald's Menu +++")
        print("1. Greetings")
        print("2. Basic Info")
        print("3. Goals in Life")
        print("4. My Hobbies")
        print("5. My Quote in Life")
        print("0. Back to Main Menu")

    def handle_choice(self, choice):
            
        match choice:
            case "1": 
                self.greet()  
            case "2":
                self.show_info()     
            case "3":
                self.state_goal()
            case "4":
                self.share_hobby()
            case "5":
                self.say_quote()
            case "0":
                print("\nReturning to main menu...")
                return False
            case _:
                print("Invalid choice. Please try again.")
        return True
    
    def menu(self):
        """Main menu loop."""
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()
            if not self.handle_choice(choice):
                break




