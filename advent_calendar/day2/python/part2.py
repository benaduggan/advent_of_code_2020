"""Where I solve the puzzle yo"""

import os


def read_file(filename: str) -> str:
    """Reads contents of given file"""
    with open(filename, "r") as content_file:
        return content_file.read()


def main():
    valid_passwords = 0
    password_db = read_file("input.txt").split("\n")
    for password_and_rule in password_db:
        min_max, letter_chunk, password = password_and_rule.split(" ")
        position_one_str, position_two_str = min_max.split("-")
        letter_to_validate = letter_chunk[0]
        position_one_letter = password[int(position_one_str) - 1]
        position_two_letter = password[int(position_two_str) - 1]

        if position_one_letter == position_two_letter:
            continue
        if letter_to_validate in f"{position_one_letter}{position_two_letter}":
            valid_passwords += 1

    print(valid_passwords)


main()