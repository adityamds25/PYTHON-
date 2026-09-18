# Module 1 - Basic Random Password Generator

## Logic

1. Import the `secrets` and `string` modules.
2. Ask the user to enter the required password length.
3. Create a character set containing letters, numbers, and special characters.
4. Start with an empty password.
5. Use a loop to generate characters until the required length is reached.
6. Use `secrets.choice()` to randomly select a character from the character set.
7. Add each selected character to the password.
8. Display the generated password.

## Working

The program takes the required password length from the user. It combines letters, numbers, and special characters into one character set. The `secrets.choice()` function randomly selects characters from this set. The process continues until the password reaches the required length. Finally, the generated password is displayed.
