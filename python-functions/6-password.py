#!/usr/bin/python3
def validate_password(password):
    # Check password length
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    # Check for spaces
    if ' ' in password:
        return False

    # Check if all conditions are met
    if has_uppercase and has_lowercase and has_digit:
        return True
    else:
        return False