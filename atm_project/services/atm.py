balance = 1000
transactions = []

def check_balance():
    print('Current Balance:', balance)


def deposit():
    global balance
    amount = int(input('Enter amount to deposit: '))
    balance += amount
    transactions.append('Deposited ' + str(amount))
    print('Amount deposited')


def withdraw():
    global balance
    amount = int(input('Enter amount to withdraw: '))
    
    if amount <= balance:
        balance -= amount
        transactions.append('Withdrawn ' + str(amount))
        print('Amount withdrawn')
    else:
        print('Insufficient balance')


def show_transactions():
    if len(transactions) == 0:
        print('No transactions yet')
    else:
        print('Transaction History:')
        for t in transactions:
            print(t)