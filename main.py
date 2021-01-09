from utils.wallet import Wallet
from heading import header

wallet = Wallet()

print(header)
CHOICE = """1. Add amount
2. Spend amount
3. view total amount
0. Quit
: """
choice = int(input(CHOICE))


while choice != 0:
    if choice in [1, 2, 3]:
        if choice == 1:
            amount = int(input("Enter an amount: "))
            wallet.add_amount(amount)
            print("Amount added. \n")
        elif choice == 2:
            amount = int(input("Enter an amount: "))
            wallet.spend_amount(amount)
            print("Amount deducted. \n")
        elif choice == 3:
            print(
                "\nRemaining amount: {} | Amount added: {} | Amount Spent: {}\n".format(
                    wallet.get_total_amount(), wallet.AMOUNT_ADDED, wallet.AMOUNT_SPENT
                )
            )
        choice = int(input(CHOICE))
    else:
        print("Invalid option.")
        break