def is_valid_password(password):
    """
    Check if the password is valid.
    A valid password must:
    - Be at least 8 characters long
    - Contain at least one uppercase letter
    - Contain at least one lowercase letter
    - Contain at least one digit
    - Contain at least one special character
    """
    # TODO: Add code to check the length of the password

    # TODO: Add code to check for at least one uppercase letter

    # TODO: Add code to check for at least one lowercase letter

    # TODO: Add code to check for at least one digit

    # TODO: Add code to check for at least one special character

    return True  # Change this to return the actual result

def main():
    password = input("Enter a password to check: ")
    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid.")

if __name__ == "__main__":
    main()