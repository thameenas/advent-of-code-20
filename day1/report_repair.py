def read_input():
    input_file = open("input.txt")
    expense_report = []
    for line in input_file:
        expense_report.append(int(line.strip("\n")))
    return expense_report


def product_of_two_expense(expense_report, target):
    for i, expense in enumerate(expense_report[:-1]):
        if target - expense in expense_report[i + 1:]:
            return expense * (target - expense)


def find_product(expense_report, number_of_expense, target):
    if number_of_expense == 2:
        return product_of_two_expense(expense_report, target)

    for i, expense in enumerate(expense_report[:-1]):
        new_target = target - expense
        product = find_product(expense_report[i + 1:], number_of_expense - 1, new_target)
        if product:
            return expense * product


if __name__ == '__main__':
    expenses = read_input()
    print(find_product(expenses, 3, 2020))
    print(find_product(expenses, 2, 2020))
