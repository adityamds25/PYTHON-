import secrets
import string

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than zero.")
    else:
        characters = ""

        upper = input("Include uppercase letters? (yes/no): ").strip().lower()
        lower = input("Include lowercase letters? (yes/no): ").strip().lower()
        numbers = input("Include numbers? (yes/no): ").strip().lower()
        special = input("Include special characters? (yes/no): ").strip().lower()

        if upper == "yes":
            characters += string.ascii_uppercase

        if lower == "yes":
            characters += string.ascii_lowercase

        if numbers == "yes":
            characters += string.digits

        if special == "yes":
            characters += string.punctuation

        if not characters:
            print("Please select at least one character type.")
        else:
            password = ""

            for i in range(length):
                password += secrets.choice(characters)

            print("Generated Password:", password)

except ValueError:
    print("Please enter a valid whole number for password length.")
