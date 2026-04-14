"""
1. String Manipulation Basics
Write a Python program that:
Takes a string input from the user
Prints:
Length of the string
First and last character
The string in uppercase and lowercase
The reversed string
"""

user_input = input("Enter user name:")

print("Length of the string:", len(user_input))

first_character = user_input[0]
last_character = user_input[len(user_input) - 1]
last_char = user_input[-1]

#print(first_character)
#print(last_character)
print(f"First and last character:{first_character}, {last_char}")
#print("First and last character:{} , {}", user_input[0], user_input[len(user_input)-1])

print("string in uppercase", user_input.upper())
print("string in lowercase", user_input.lower())

print("".join(reversed(user_input)))
print(user_input[::-1])