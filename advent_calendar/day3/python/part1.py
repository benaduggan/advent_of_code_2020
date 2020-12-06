"""Where I solve the puzzle yo"""

import os
import math


def read_file(filename: str) -> str:
    """Reads contents of given file"""
    with open(filename, "r") as content_file:
        return content_file.read()


def main():
    map = read_file("input.txt").split("\n")
    length_of_map = len(map)
    repeat_length = len(map[0])

    collisions = 0
    x_slope = 3
    y_slope = 1
    x_position = 0
    y_position = 0

    for i in range(length_of_map):
        line = map[y_position] * (math.ceil(x_position / repeat_length) + 1)
        if line[x_position] == "#":
            collisions += 1
        x_position += x_slope
        y_position += y_slope

    print(collisions)


main()