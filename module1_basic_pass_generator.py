import secrets
import string

print("===== RANDOM PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += secrets.choice(characters)

print("Generated Password:", password)
