class Account:
    def __init__(self, acc_number, acc_owner, bal=0):
        self.__acc_number = acc_number
        self.__acc_owner = acc_owner
        self.__bal = bal
    
    def deposit(self, amount):
        self.__bal += amount
        print(f"Deposit of {amount} successful. Current balance: {self.__bal}")
    
    def withdraw(self, amount):
        if self.__bal >= amount:
            self.__bal -= amount
            print(f"Withdrawal of {amount} successful. Current balance: {self.__bal}")
        else:
            print("Insufficient balance.")
    
      
    def transfer(self, recipient_account, amount):
        if self.__bal >= amount:
            self.__bal -= amount
            recipient_account.deposit(amount)
            print(f"Transfer of {amount} to account {recipient_account.__acc_number} successful.")
        else:
            print("Insufficient balance for transfer.")
    
    def get_account_info(self):
        return {
            "Account Number": self.__acc_number,
            "Account Holder": self.__acc_owner,
            "Balance": self.__bal
        }


# Creating objects
account1 = Account(1, "Robert",1000)
account2 = Account(2, "Michael")


# Testing methods
account1.deposit(1000)
account1.withdraw(500)

account1.transfer(account2, 200)


account_info = account1.get_account_info()
print(account_info)
