#Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength of the password. 
#Implement a Python function called check_password_strength that takes a password string as input.
#The function should check the password against the following criteria:
#Minimum length: The password should be at least 8 characters long.
#Contains both uppercase and lowercase 
#Contains at least one digi
#Contains at least one special character (e.g., !, @, #
#The function should return a boolean value indicating whether the password meets the c
#Write a script that takes user input for a password and calls the check_password_strength function to vali
#Provide appropriate feedback to the user based on the strength of the password.  


import re

def check_password_strength(password):
    """
    Check if the given password meets security criteria:
    - At least 8 characters long
    - Contains both uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

if __name__ == "__main__":
    user_password = input("Enter your password: ")

    if check_password_strength(user_password):
        print(" Password is strong.")
    else:
        print(" Password is weak. Make sure it has:")
        print("   - At least 8 characters")
        print("   - Both uppercase and lowercase letters")
        print("   - At least one digit")
        print("   - At least one special character (e.g., !, @, #, etc.)")
