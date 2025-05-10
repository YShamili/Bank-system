class Account:
    def __init__(self,acc_no, name, balance, pin):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.pin = pin
    def displaying_info(self):
        print("Account number: ",self.acc_no)
        print("Account name: ",self.name)
        print("Account balance: ",self.balance)
    def deposit(self, amount):
        if amount < 0:
            print("The amount should be greater than 0 in order to deposit")
            return
        self.balance += amount
        print(f"The balance in the account is {self.balance}")
    def withdraw(self, amount):
        if amount <= 0:
            print("The amount should be greater than 0 in order to withdraw")
            return
        if amount > self.balance:
            print("The balance is not sufficient in order to withdraw the money")
            return
        self.balance -= amount
        print(f"The amount been withdrawn is {amount} and the remaining balance is {self.balance}")
    def transfer(self,transfered_acc, amount):
        if amount <= 0:
            print("The amount should be greater than 0 in order to withdraw")
            return
        if amount > self.balance:
            print("The balance is not sufficient in order to withdraw the money")
            return
        self.balance -= amount
        transfered_acc.balance += amount
        print(f"Transfered {amount} to the account number {transfered_acc}")
        print(f"The remaining balance is {self.balance}")


class Banksystem:
    def __init__(self):
        self.accounts_lst = []
    def create_account(self, acc_no, name, balance, pin):
        new_acc = Account(acc_no, name, balance, pin)
        self.accounts_lst.append(new_acc)
        print("created successfully")
    def find_acc(self, acc_no):
        for accounts in self.accounts_lst:
            if acc_no == accounts.acc_no:
                return accounts
        return None
    def login(self, acc_no, pin):
        account = self.find_acc(acc_no)
        if account and account.pin == pin:
            print("login successful")
            return account
        else:
            print("Invalid account number or pin")
            return None
        
        
bank = Banksystem()
while True:
    print("---Welcome to the bank system---")
    print("1. Create New account")
    print("2. Login to existing account")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        acc_no = int(input("Enter the account number: "))
        name = input("Enter the name of the account: ")
        balance = int(input("Enter the amount for the balance: "))
        pin = input("Enter the pin of the account: ")
        bank.create_account(acc_no, name, balance, pin)

    elif choice == '2':
        acc = int(input("Enter the account number for login: "))
        pin = input("Enter the pin for login: ")
        a = bank.login(acc, pin)
        if a:
            print(f"Welcome {a.name}")
            while True:
                print("\n1-View account info\n2-Deposit money\n3-Withdraw money\n4-Transfer money\n5-Logout")
                opt = input("Enter your choice: ")
                
                if opt == '1':
                    a.displaying_info()

                elif opt == '2':
                    am = int(input("Enter the amount to be deposited: "))
                    a.deposit(am)

                elif opt == '3':
                    am = int(input("Enter the amount to be withdrawn: "))
                    a.withdraw(am)

                elif opt == '4':
                    to = int(input("Enter the account number to transfer to: "))
                    am = int(input("Enter the amount to be transferred: "))
                    target_acc = bank.find_acc(to)
                    if target_acc:
                        a.transfer(target_acc, am)
                    else:
                        print("Target account not found.")

                elif opt == '5':
                    print("Logged out.")
                    break

                else:
                    print("Invalid option.")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")