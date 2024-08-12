# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import re

def assess_password_strength(password):
    """
    Assess the strength of a password based on length, and the presence of uppercase letters,
    lowercase letters, numbers, and special characters.
    
    :param password: The password string to assess.
    :return: A string with feedback on the password's strength.
    """
    # Define criteria
    min_length = 8
    length_criteria = len(password) >= min_length
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assess the strength
    if length_criteria and uppercase_criteria and lowercase_criteria and number_criteria and special_char_criteria:
        return "Password is Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and (number_criteria or special_char_criteria):
        return "Password is Moderate"
    elif length_criteria or (uppercase_criteria or lowercase_criteria) and (number_criteria or special_char_criteria):
        return "Password is Weak"
    else:
        return "Password is Very Weak"

def main():
    password = input("Enter a password to assess its strength: ")
    strength = assess_password_strength(password)
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
