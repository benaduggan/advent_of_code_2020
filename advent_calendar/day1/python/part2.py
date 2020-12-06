"""Where I solve the puzzle yo"""
import os


def read_file(filename: str) -> str:
    """Reads contents of given file"""
    with open(filename, "r") as content_file:
        return content_file.read()


def main():
    expenses = read_file("input.txt").split("\n")
    for expense in expenses:
        for second_expense_idx in range(len(expenses) - 1):
            second_expense = int(expenses[second_expense_idx])
            for third_expense_idx in range(len(expenses) - 1):
                third_expense = int(expenses[third_expense_idx])
                if int(expense) + second_expense + third_expense == 2020:
                    print(int(expense) * second_expense * third_expense)
                    return


main()