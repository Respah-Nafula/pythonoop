class Account:
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0


    def deposit(self,amount):
        if amount<=0:
            return f"deposit must be positive amount"
        else:
         self.balance+=amount
        return f"Hello {self.account_name} you have deposited{amount} and your account balance is {self.balance}"
