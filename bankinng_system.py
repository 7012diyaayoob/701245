# banking system
# 1.login(user)
# 2. registration
# 3. deposit
# 4. withdrawal
# 5. check balance
# 6. logout

class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
    def login(self,username,password):
        if self.username == username and self.password == password:
            print("login sucessfull")
            main()
        else:
            print("invalid username or password")

    def deposit(self,amount):
        self.balance += amount
        print(f"deposited{amount}units.current balance:{self.balance}")
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"withdrew {amount} units. current balance:{self.balance}")
        else:
            print("insufficient balance!")

#creating a bankaccount instance
account = BankAccount("sadiya 1","sadiya4045")
# logging in
def account_login():
    username = input("enter username:")
    password = input("enter password :")
    account.login(username,password)

# deposit funds
def deposit_funds():
    amount = float(input("enter the amount to deposit:"))
    account.deposit(amount)
# withdraw  funds
def withdraw_funds():
    amount = float(input("enter the amount to withdraw:"))
    account.withdraw(amount)
 #main program loop
def main() :
    while True:
        print("\nwelcome to HDFC")
        print("1.deposit funds ")
        print("2. withdraw funds")
        print("3.exit")
        choice= int(input("enter your choice(1-4):"))


        if choice ==1:
            deposit_funds()
        elif choice == 2:
            withdraw_funds()
        elif choice == 3:
            print("exiting ...")
            account_login()
        else:
            print("invalid choice. please try agin.")



account_login()












