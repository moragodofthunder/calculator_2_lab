"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

user_input = input("What do you want to calculate?: ")
token = user_input.split(" ")

if token[0] == "+":
    print(add(int(token[1]), int(token[2])))

elif token[0] == "-":
    print(subtract(int(token[1]), int(token[2])))

elif token[0] == "*":
    print(multiply(int(token[1]), int(token[2])))

elif token[0] == "/":
    print(divide(int(token[1]), int(token[2])))

elif token[0] == "cube":
    print(cube(int(token[1]), int(token[2])))

elif token[0] == "square":
    print(square(int(token[1]), int(token[2])))

elif token[0] == "power":
    print(power(int(token[1]), int(token[2])))

elif token[0] == "modulo":
    print(mod(int(token[1]), int(token[2])))