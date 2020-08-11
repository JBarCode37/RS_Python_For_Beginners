import os
import json

def get_goals():
    filename = './data/goals.txt'
    if os.path.exists(filename):
        with open(filename) as f:
            goals = f.readlines()
            goals = [goal.rstrip() for goal in goals]
            for i, goal in enumerate(goals):
                print(f'#{i}: {goal}')
    else:
        # Get goals from user
        n = input('Enter the number of goals: ')
        n = int(n)
        
        goals = []
        for i in range(n):
            goal = input(f'Enter your #{i+1} goal: ')
            goals.append(goal + '\n')
        
        with open(filename, 'w') as f:
            f.writelines(goals)

def get_savings():
    savings = input('Enter your savings balance (e.g. 3.99): ')
    return float(savings)

def get_income():
    income = input('Enter your monthly income (e.g. 49.99): ')
    return float(income)

def print_savings(savings_in):
    print(f'Great! You have ${savings_in:,.2f} in savings.')

def print_income(income_in):
    print(f'You make ${income_in:,.2f} each month!')

def get_bill_amounts(bills_in: list = []) -> list:
    bills_file = './data/bills.json'

    if os.path.exists(bills_file):
        with open(bills_file) as f:
            bills = json.load(f)
    else:
        # You could ask the user for a list of bills,
        # then split the string
        bills = dict().fromkeys(bills_in, 0.00) # or list()
        for bill in bills.keys():
            bill_amount = input(f'Enter the amount for your {bill} bill: ')
            bills[bill] = float(bill_amount)

        # store in a json file
        with open(bills_file, 'w') as f:
            json.dump(bills, f)

    return bills

def print_bills(bills_in):
    for bill, amount in bills_in.items():
        print(f'{bill}: ${amount:,.2f}')

    print(f'Total Bills: ${sum(bills_in.values()):,.2f}')

def main():
    # savings = get_savings()
    # print_savings(savings)
    # income = get_income()
    # print_income(income)
    get_goals()
    bills_list = ['rent', 'car', 'food', 'total utilities', 'pet food']
    bills = get_bill_amounts(bills_list)
    print_bills(bills)

if __name__ == '__main__':
    main()
    