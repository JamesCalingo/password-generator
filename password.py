import random
import string

"""This generates a string of randomized characters of a user-defined length"""

def generate_password(length = 15):
  length = int(input("How long would you like your password to be? "))
  while length < 8 or length > 20:
    print("Your password should probably be between 8 and 20 characters. Try again.")
    length = int(input("How long would you like your password to be? "))

  password = ""
  for i in range(length):
    char = random.choice(string.printable)
    if char in string.whitespace:
      char = random.choice(string.printable)
    # elif char == password[i - 1]:
    #   char = random.choice(string.printable)
    else:
      password += (char)
  return password

print(generate_password())
