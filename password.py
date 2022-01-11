import random
import string
# import pyperclip as pc

"""
This generates a string of randomized characters of a user-defined length
"""


def generate_password():
    length_input = input(
        "How long would you like your password to be?\n(NOTE: It should probably be between 8 and 30 characters.) ")
    while not length_input.isdigit():
        print("I can't interpret that into a password length. Try again.")
        length_input = input(
            "How long would you like your password to be?\n(NOTE: It should probably be between 8 and 30 characters.) ")

    length = int(length_input)
    password = ""
    for i in range(length):
        char = random.choice(string.printable)
        if char in string.whitespace:
            char = random.choice(string.printable)
        # elif char == password[i - 1]:
        #   char = random.choice(string.printable)
        else:
            password += (char)
#     pc.copy(password)
    return (f"Your new password is: {password}.\nBe sure to copy this (or memorize it if you can...)")


print(generate_password())

# Pyperclip is a package designed to copy the password to the clipboard, however I have yet to verify that it works.
