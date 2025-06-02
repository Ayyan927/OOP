class Account:
    def __init__(self, account_name, pin, balance):
        self.account_name = account_name
        self.pin = pin
        self.balance = balance

    def check_pin(self, input_pin):
        return self.pin == input_pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_name] = account

    def authenticate(self, account_name, pin):
        account = self.accounts.get(account_name)
        if account and account.check_pin(pin):
            return account
        return None

    def run(self):
        account_number = input("Enter name: ")
        pin = input("Enter PIN: ")
        account = self.authenticate(account_number, pin)

        if not account:
            print("Authentication failed.")
            return

        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                print("Balance:", account.get_balance())
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                if account.withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance.")
            elif choice == '4':
                break
            else:
                print("Invalid option.")


atm = ATM()
atm.add_account(Account("haroon", "1234", 3000))
atm.add_account(Account("Ayyan", "2008", 5000))
atm.run()