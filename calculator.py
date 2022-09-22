"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_unlimited, multiply_unlimited)

#Previous while True loop that asks for user input:
    # while True:
    #     # This takes in the calculation from the user
    #     user_input = input("What do you want to calculate?: ")

import sys

numbers = sys.argv[1]
# numbers = open(number.txt) ### if wanted to open this way. 

# For loop that uses number.txt file:
for equation_line in open(numbers):
    # This sets the input as a list, called token
    token = equation_line.split(" ")

    # token[1] is the operator, aka the first character typed by the user
    # token[0] and token[2] are the first and second numbers the user chooses 
    # for the calculation



    # for unlimited equations: 
    if len(token) > 2:

        if token[0] == "+":
            answer = ((add_unlimited(token)))
            answer = float(answer)
            print(f"{answer:.3f}")

        elif token[0] == "*":
            answer = ((multiply_unlimited(token)))
            answer = float(answer)
            print(f"{answer:.3f}")


    elif token[1] == "-":
        answer = (subtract(float(token[0]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[1] == "/":
        answer = (divide(float(token[0]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[1] == "*":
        answer = (multiply(float(token[0]), float(token[2])))
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