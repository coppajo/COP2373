class BankAcct:
    def __init__(self, name, account_num, amount, interest_rate):
        self.name = name
        self.account_num = account_num
        self.amount = amount
        self.interest_rate = interest_rate

    # mutator methods
    def adjust_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def withdraw(self, amount, withdraw_amnt):
        self.amount = amount - withdraw_amnt

    def deposit(self, amount, deposit_amnt):
        self.amount = amount + deposit_amnt

    # calculate interest based on number of days
    def calc_interest(self, principal, time):
        # I don't really know what that is supposed to mean
        # using simple interest formula A = P(1+r(t/365))
        # A is final amount, P is principal, r is rate, t is time in days
        # 365((A/P) - 1)/t = r   is the formula solved for the interest rate

        # I will assume that the current account balance is the final amount
        rate = ((self.amount/principal) - 1) * 365 / time

        return rate

    # accessor methods
    def get_balance(self):
        return self.amount

    def __str__(self):
        return f'Your account balance is ${self.amount:.2f}. \nYour interest rate is %{self.interest_rate}'


def test():
    # input info to be put into bank account object
    name = input('What is your name? ')

    while True:
        acc_num = input('What is your account number? ')
        try:
            acc_num = int(acc_num)
        except ValueError:
            continue
        else:
            break

    while True:
        balance = input('What is your account balance? ')
        try:
            balance = float(balance)
        except ValueError:
            continue
        else:
            break

    while True:
        interest = input('What is the interest rate? ')
        try:
            interest = float(interest)
        except ValueError:
            continue
        else:
            break

    # create bank account object
    Bank_Account = BankAcct(name, acc_num, balance, interest)

    # make user choose what method to use

    while True:
        # options
        print('\n'
              '1: Adjust interest rate\n'
              '2: Withdraw from the account\n'
              '3: Deposit to the account\n'
              '4: Calculate interest\n'
              '5: Get account balance\n'
              '6: __str__ method (Display balance and interest rate)\n'
              '7: Close program\n')

        choice = input('What do you want to do? ')

        if choice == '1':
            print(f'The current interest rate is %{Bank_Account.interest_rate}')
            new_interest = input("What do you want to set it to? ")
            Bank_Account.adjust_interest_rate(new_interest)
        elif choice == '2':
            withdraw_amnt = float(input('How much will you withdraw? '))
            Bank_Account.withdraw(balance, withdraw_amnt)
        elif choice == '3':
            deposit_amnt = float(input('How much will you deposit? '))
            Bank_Account.deposit(balance, deposit_amnt)
        elif choice == '4':
            print(f'Your current balance is ${Bank_Account.amount:.2f}')
            principal = float(input('What was your starting balance? '))
            time = float(input('How much time (in days) has passed? '))

            rate = Bank_Account.calc_interest(principal, time)
            print(f'Your interest rate should be %{rate:.4f} then.')

        elif choice == '5':
            acc_bal = Bank_Account.get_balance()
            print(f'Your account balance is ${acc_bal:.2f}')
        elif choice == '6':
            print(Bank_Account.__str__())
        elif choice == '7':
            break
        else:
            print('Invalid input. Choose 1-7')



test()
