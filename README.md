# password-generator
Generate a string of random characters to use as a strong password

# How to use it
I've made a few versions of this - currently, JavaScript and Python.

To run one of them, simply use

`
node password.js
`

or

`
python3 password.py
`

and it will generate a password for you.

Each has a unique feature that I'd like to "standardize", if you will:

- The JS version has the ability to make sure that you don't end up with all the same character, but it's "set" to a length of 15 characters - though this can be changed.
- The Python version has the user inputting how long they'd like their password to be, but it lacks the "character safety" that the JS version has (which means that, though it's EXTREMELY unlikely, you could end up with a password that's all one character.
