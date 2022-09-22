"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    # This takes in the calculation from the user
    user_input = input("What do you want to calculate?: ")
    # This sets the input as a list, called token
    token = user_input.split(" ")

    # token[0] is the operator, aka the first character typed by the user
    # token[1] and token[2] are the first and second numbers the user chooses 
    # for the calculation
    if token[0] == "+":
        answer = ((add(float(token[1]), float(token[2]))))
        print(f"{answer:.3f}")

    elif token[0] == "-":
        answer = (subtract(float(token[1]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[0] == "*":
        answer = (multiply(float(token[1]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[0] == "/":
        answer = (divide(float(token[1]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[0] == "cube":
        answer = (cube(float(token[1]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[0] == "square":
        answer = (square(float(token[1]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[0] == "power":
        answer = (power(float(token[1]), float(token[2])))
        print(f"{answer:.3f}")

    elif token[0] == "mod":
        answer = (mod(float(token[1]), float(token[2])))
        print(f"{answer:.3f}")

    # This will allow the user to quit calculator
    elif "q" in token:
        print("Okay bye")
        break

    # This will work the user about invalid input
    else:
        print("Sorry, that's invalid")

# import sys

# numbers = sys.argv[1]
# for equations in open(numbers):
#     print(power(int(token[1]), int(token[2])))