from app.input_manager import get_user_name, get_user_age

def greet_user() -> str:
    """Return a greeting massage baased on the user's age."""
    name = get_user_name()
    age = get_user_age()


    if age < 18:
        return f"Hello {name}, sorry! you are not allowed to enter this site."
    else:
        return f"Hello {name}! Welcome to ###.com"



