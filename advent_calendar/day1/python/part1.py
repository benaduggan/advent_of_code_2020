"""Where I solve the puzzle yo"""

import os


def read_file(filename: str) -> str:
    """Reads contents of given file"""
    with open(filename, "r") as content_file:
        return content_file.read()


def main():
    expenses = read_file("input.txt").split("\n")
    for expense in expenses:
        for other_expense_idx in range(len(expenses) - 1):
            other_expense = int(expenses[other_expense_idx])
            if int(expense) + other_expense == 2020:
                print(int(expense) * other_expense)
                return


main()