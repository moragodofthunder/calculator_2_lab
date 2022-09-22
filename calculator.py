"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

#Previous while True loop that asks for user input:
    # while True:
    #     # This takes in the calculation from the user
    #     user_input = input("What do you want to calculate?: ")

import sys

numbers = sys.argv[1]

# For loop that uses number.txt file:
for equations in open(numbers):
    # This sets the input as a list, called token
    token = equations.split(" ")

    # token[1] is the operator, aka the first character typed by the user
    # token[0] and token[2] are the first and second numbers the user chooses 
    # for the calculation

    if token[-1] == "+":
        answer = ((add(token)))
        answer = float(answer)
        print(f"{answer:.3f}")

    elif token[-1] == "*":
        answer = ((multiply(token)))
        answer = float(answer)
        print(f"{answer:.3f}")

    elif token[1] == "-":
        answer = (subtract(float(token[0]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[1] == "/":
        answer = (divide(float(token[0]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[1] == "cube":
        answer = (cube(float(token[0]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[1] == "square":
        answer = (square(float(token[0]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[1] == "power":
        answer = (power(float(token[0]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[1] == "mod":
        answer = (mod(float(token[0]), float(token[2])))
        print(f"{answer:.3f}")

    # This will allow the user to quit calculator
    elif "q" in token:
        print("Okay bye")
        break

    # This will work the user about invalid input
    else:
        print("Sorry, that's invalid")