import random
import string

def generate_password(length):
  password = ""
  for i in range(length):
    char = random.choice(string.printable)
    if char in string.whitespace:
      char = random.choice(string.printable)
    else:
      password += (char)
  return password

print(generate_password(15))