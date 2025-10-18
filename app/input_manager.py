def get_user_name() -> str:
    """Ask for the user's name."""
    return input("Enter your name: ")


class InvalidAgeErorr(Exception):
    pass


def get_user_age() -> int:
    """Ask for user's age"""
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 150:
                raise InvalidAgeErorr("Provide a valid age: ")
            return age

        except ValueError:
            print("❌ Please enter a valid number for your age.")
        except InvalidAgeErorr as e:
            print("❌", e)

            
