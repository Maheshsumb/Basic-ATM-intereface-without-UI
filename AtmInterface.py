# Creating a class ATM
class BankAccount:
    # Creating Constuctor to intialize information
    def __init__(self,Name,Account_Number,Balance=0):
        self.Name=Name
        self._Account_Number=Account_Number
        self.__Balance=Balance
    # Created a Deposite Method
    def deposit(self,amount):
        self.__Balance+=amount
        # Create a Withdraw Method
    def withdraw(self,amount):
        if self.__Balance>=amount:
            self.__Balance-=amount
        else:
            print("Insufficient Funds")
    #Create Method To check Balance
    def get_balance(self):
        return self.__Balance
    #Created a method to Transfer to the money to another account
    def transfer(self,amount,other_account):
        if amount<=self.__Balance:
            self.withdraw(amount)
            self.__Balance-=amount
    #Create a method to Print the Account Information
    def get_account_info(self):
        return f"Name: {self.Name},\nAccount number: {self._Account_Number},\nBalance: {self.__Balance}"
#Created Class ATM 
class ATM:
    #Created a Constructor to Initialize 
    def __init__(self,account):
        self.account = account
    #Created a Method to show Menu to Users
    def show_menu(self):
        print("\n---ATM Menu---")
        print("1.Check Balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Transfer Money")
        print("5.View Account")
        print("6.Exit")
    #Method for taking input from user to perform the various operations 
    def run(self):
        while True:
            self.show_menu()
            choice=int(input("Choose an Option"))
            if choice==1:
                print(f"Your Balance is: {self.account.get_balance()}")
            elif choice==2:
                amount=float(input("Enter amount to deposit: "))
                self.account.deposit(amount)
                print(f"Your New Balance is: {self.account.get_balance()}")
            elif choice==3:
                amount=float(input("Enter amount to Withdraw: "))
                self.account.withdraw(amount)
                print(f"Your New Balance is: {self.account.get_balance()}")
            elif choice==4:
                account_number=input("Enter account number  to transfer to: ")
                amount=float(input("Enter amount to Transfer: "))
                other_account=BankAccount("Recipient",account_number)
                self.account.transfer(amount,other_account)
                print(f"Transferred {amount} to account {account_number}. New Balance is {self.account.get_balance()}")
            elif choice==5:
                print(self.account.get_account_info())
            elif choice==6:
                print("Exiting ATM. Have a great day!")
                break
#
            #
            
            else:
                print("Invalid Choice. Please Try Again!!!!!")
# Created Object for BankAccount Class
account=BankAccount("Alice","12345",1000)
#Object For ATM Class
atm=ATM(account)
# called run Method from atm class
atm.run()

