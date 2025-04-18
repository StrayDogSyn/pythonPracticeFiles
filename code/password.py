# Password conditions
class PasswordError(Exception):
    """Custom exception for password validation errors."""
    pass

"""
1. Password must be at least 8 characters long.
2. Password must contain at least one uppercase letter.
3. Password must contain at least one lowercase letter.
4. Password must contain at least one digit.
"""
try:
    user_input = input("Enter a password: ")
    # Check if the password meets the conditions
    if len(user_input) < 8:
        raise PasswordError("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in user_input):
        raise PasswordError("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in user_input):
        raise PasswordError("Password must contain at least one lowercase letter.")
    if not any(char.isdigit() for char in user_input):
        raise PasswordError("Password must contain at least one digit.")
    print(f"Password '{user_input}' is valid!")
except PasswordError as e:
    print(f"Invalid password: {e}")
finally:
    print("Bye Felica!")

print(user_input)
# Print password outside the try-except block
