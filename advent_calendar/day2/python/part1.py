"""Where I solve the puzzle yo"""

import os


def read_file(filename: str) -> str:
    """Reads contents of given file"""
    with open(filename, "r") as content_file:
        return content_file.read()


def main():
    valid_passwords = 0
    password_db = read_file("input.txt").split("\n")
    for password in password_db:
        min_max, letter_chunk, password = password.split(" ")
        min_count_str, max_count_str = min_max.split("-")
        min_count, max_count = int(min_count_str), int(max_count_str)
        letter = letter_chunk[0]
        count_of_letter = password.count(letter)
        if count_of_letter >= int(min_count) and count_of_letter <= int(max_count):
            valid_passwords += 1

    print(valid_passwords)


main()