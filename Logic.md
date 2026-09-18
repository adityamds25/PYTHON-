# Module 1 - Basic Random Password Generator

## 1. Problem Statement

Develop a basic Python-based Random Password Generator that generates a random password according to the length specified by the user. The password should contain letters, numbers, and special characters.

## 2. Objective

- To generate random passwords using Python.
- To take the required password length from the user.
- To use letters, numbers, and special characters.
- To understand the use of Python modules.
- To generate passwords automatically.

## 3. Input

The user enters the required password length.

Example:

10

## 4. Output

The program generates and displays a random password.

Example:

G7@kP2#xLm

## 5. Algorithm / Logic

1. Start the program.
2. Import the `secrets` and `string` modules.
3. Ask the user to enter the required password length.
4. Create a collection containing letters, numbers, and special characters.
5. Run a loop according to the required password length.
6. Select a random character from the collection using the `secrets` module.
7. Add the selected character to the password.
8. Repeat until the required length is reached.
9. Display the generated password.
10. End the program.

## 6. Program Flow

START
↓
Enter Password Length
↓
Create Character Collection
↓
Select Random Character
↓
Repeat Until Required Length
↓
Generate Password
↓
Display Password
↓
END

## 7. Explanation

### Importing Modules

The program uses two Python modules:

- `secrets` - used to select random characters.
- `string` - provides letters, numbers, and special characters.

### Taking User Input

```python
length = int(input("Enter password length: "))
