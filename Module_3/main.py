import secrets
import string

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than zero.")
    else:
        choices = {
            "uppercase": input("Include uppercase letters? (yes/no): ").strip().lower(),
            "lowercase": input("Include lowercase letters? (yes/no): ").strip().lower(),
            "numbers": input("Include numbers? (yes/no): ").strip().lower(),
            "special": input("Include special characters? (yes/no): ").strip().lower()
        }

        pools = []

        if choices["uppercase"] == "yes":
            pools.append(string.ascii_uppercase)

        if choices["lowercase"] == "yes":
            pools.append(string.ascii_lowercase)

        if choices["numbers"] == "yes":
            pools.append(string.digits)

        if choices["special"] == "yes":
            pools.append(string.punctuation)

        if not pools:
            print("Please select at least one character type.")

        elif length < len(pools):
            print("Password length is too short for the selected types.")

        else:
            characters = "".join(pools)

            password_chars = [
                secrets.choice(pool) for pool in pools
            ]

            for i in range(length - len(password_chars)):
                password_chars.append(secrets.choice(characters))

            secrets.SystemRandom().shuffle(password_chars)
            password = "".join(password_chars)

            checks = {
                "Uppercase": not choices["uppercase"] == "yes"
                or any(c in string.ascii_uppercase for c in password),

                "Lowercase": not choices["lowercase"] == "yes"
                or any(c in string.ascii_lowercase for c in password),

                "Numbers": not choices["numbers"] == "yes"
                or any(c in string.digits for c in password),

                "Special": not choices["special"] == "yes"
                or any(c in string.punctuation for c in password)
            }

            valid = all(checks.values())

            print("Generated Password:", password)
            print("Length:", len(password))
            print("All selected types included:", valid)

            pool_size = len(set(characters))

            if length >= 12 and pool_size >= 60:
                strength = "Strong"
            elif length >= 8 and pool_size >= 30:
                strength = "Moderate"
            else:
                strength = "Basic"

            print("Estimated Strength:", strength)

except ValueError:
    print("Please enter a valid whole number for password length.")
