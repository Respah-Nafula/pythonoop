class Money:
 def __init__(self,account_name,account_number): 
    self.account_name = account_name
    self.account_number = account_number
    self.balance=0
    self.deposits=[]
    self.withdrawals=[]
    
 
    def withdraw(self,amount):
        if amount<=0:
            return f"Your withdrawal should be greater than zero"
        elif amount>self.balance:
            return f"your balance is {self.balance} you cant withdraw{amount}" 
        else:
         self.balance-=amount+100
    
         self.withdrawals.append(amount)

        return f"Hello{self.account_name} you have withdrawn {amount}. Your balance is {self.balance}. You have paid 100 for the transaction."



    def deposit(self,amount):
         if amount<=0:
            return f"deposit must be positive amount"
         else:
          self.balance+=amount
          self.deposits.append(amount)
          return f"You have deposited {amount} and your total balance is {self.balance}"

         
        

    def deposits_statement(self):
            for transaction in self.deposits:
             print (transaction,end="\n")

    def withdrawal_statement(self):
            for withdrawal in self.withdrwals:
             print(withdrawal,end="\n")

    def balance(self):
     return f" Hello, your current balance is {self.balance}"

                        
                

       
       
