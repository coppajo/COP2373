import functools # importing for the reduce method

def main():
    expense_type_list = []
    expense_cost_list = []

    # explains expectations for input
    print("Input information about your monthly expenses below. When done hit enter without typing anything else.")

    # loop to get monthly expenses
    while True:
        expense_type = input("What type of expense is it? ")

        # end the loop if nothing is input
        if expense_type == "":
            break

        expense_cost = input("How much does it cost you? ")

        # try except for input validation
        try:
            expense_cost = float(expense_cost)
        except Exception:
            print("Error: Input wasn't valid")
            continue

        # add the information to their respective lists
        expense_type_list.append(expense_type)
        expense_cost_list.append(expense_cost)

    total_expense = functools.reduce(lambda x, y: x + y, expense_cost_list)

    # finding lowest expense and highest expense and
    lowest_expense = min(expense_cost_list)
    lowest_expense_name = expense_type_list[expense_cost_list.index(lowest_expense)]

    highest_expense = max(expense_cost_list)
    highest_expense_name = expense_type_list[expense_cost_list.index(highest_expense)]

    # displaying info
    print(f'The total expense is ${total_expense:.2f} a month.'
          f'\nThe highest expense is {highest_expense_name} and it is ${highest_expense:.2f} a month.'
          f'\nThe lowest expense is {lowest_expense_name} and it is ${lowest_expense:.2f} a month.')


main()