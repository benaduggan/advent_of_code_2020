"""Where I solve the puzzle yo"""

import os
import math


def read_file(filename: str) -> str:
    """Reads contents of given file"""
    with open(filename, "r") as content_file:
        return content_file.read()


def check_collisions_for_slope(x_slope, y_slope):
    map = read_file("input.txt").split("\n")
    length_of_map = len(map)
    repeat_length = len(map[0])

    collisions = 0
    x_position = 0
    y_position = 0

    for i in range(length_of_map):
        if y_position >= length_of_map:
            break
        line = map[y_position] * (math.ceil(x_position / repeat_length) + 1)
        if line[x_position] == "#":
            collisions += 1
        x_position += x_slope
        y_position += y_slope

    return collisions


def main():
    to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = []

    for thing in to_check:
        result.append(check_collisions_for_slope(thing[0], thing[1]))
    print(result)
    print(math.prod(result))


main()