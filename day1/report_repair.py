import math


def read_input():
    input_file = open("input.txt")
    expense_report = []
    for line in input_file:
        expense_report.append(int(line.strip("\n")))
    return expense_report


def find_all_combinations(expense_report, number_of_expenses):
    if number_of_expenses == 0:
        return [[]]

    expense_list = []
    for i in range(0, len(expense_report)):
        expense = expense_report[i]
        remaining_expense = expense_report[i + 1:]

        for another_expense in find_all_combinations(remaining_expense, number_of_expenses - 1):
            expense_list.append([expense] + another_expense)

    return expense_list


def find_product(expense_report, target, number_of_expenses):
    expense_combinations = find_all_combinations(expense_report, number_of_expenses)
    for element in expense_combinations:
        if sum(element) == target:
            print(element)
            return math.prod(element)


if __name__ == '__main__':
    expenses = read_input()
    print(find_product(expenses, 2020, 3))
    print(find_product(expenses, 2020, 2))
