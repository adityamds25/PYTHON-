import secrets
import string

def generate_password():
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than zero.")
            return

        options = {
            "uppercase": input("Include uppercase letters? (yes/no): ").strip().lower(),
            "lowercase": input("Include lowercase letters? (yes/no): ").strip().lower(),
            "numbers": input("Include numbers? (yes/no): ").strip().lower(),
            "special": input("Include special characters? (yes/no): ").strip().lower()
        }

        for option in options.values():
            if option not in ("yes", "no"):
                print("Please enter yes or no for every option.")
                return

        pools = []

        if options["uppercase"] == "yes":
            pools.append(string.ascii_uppercase)

        if options["lowercase"] == "yes":
            pools.append(string.ascii_lowercase)

        if options["numbers"] == "yes":
            pools.append(string.digits)

        if options["special"] == "yes":
            pools.append(string.punctuation)

        if not pools:
            print("Please select at least one character type.")
            return

        if length < len(pools):
            print("Password length is too short for the selected types.")
            return

        characters = "".join(pools)

        password_chars = [
            secrets.choice(pool) for pool in pools
        ]

        for i in range(length - len(password_chars)):
            password_chars.append(secrets.choice(characters))

        secrets.SystemRandom().shuffle(password_chars)
        password = "".join(password_chars)

        valid = all(
            any(char in pool for char in password)
            for pool in pools
        )

        pool_size = len(set(characters))

        if length >= 12 and pool_size >= 60:
            strength = "Strong"
        elif length >= 8 and pool_size >= 30:
            strength = "Moderate"
        else:
            strength = "Basic"

        print("\n--- Password Generator Result ---")
        print("Generated Password:", password)
        print("Password Length:", len(password))
        print("Selected Types Included:", valid)
        print("Estimated Strength:", strength)

    except ValueError:
        print("Please enter a valid whole number for password length.")

generate_password()
