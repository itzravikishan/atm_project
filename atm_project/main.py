from services.atm import *

def atm():
    while True:
        print('\n ATM Menu')
        print('1.Check Balance')
        print('2.Deposit')
        print('3.Withdraw')
        print('4.Transactions')
        print('5.Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            show_transactions()
        elif choice == 5:
            print('Thank You!')
            break
        else:
            print('Invalid choice')

atm()