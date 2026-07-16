# Exercise 5: Write a class called BankAccount 
# with deposit, withdraw, balance methods 
# handle edge cases like negative withdrawal 

class BankAccount:
    def __init__(self,name ,ac_number,balance):
        self.name = name
        self.ac_number = ac_number
        self.balance =balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully : ")
        else :
            print("please enter a valid amount")
    
    def withdraw(self,amount):
        if amount > 0:
            if amount > self.balance:
                print("Invalid Balance")
            else:
                self.balance -= amount
        else :
            print("please enter a valid amount")

    def account_balance(self):
        print(f"Balance for account {self.ac_number} is {self.balance}")

b=BankAccount("Pintu","123",5000)
b.deposit(int(input("Enter the amount to be deposited : ")))
b.account_balance()
b.withdraw(amount = int(input("Enter the amount to be withdrawn : ")))
b.account_balance()