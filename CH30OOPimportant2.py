 #ENCAPSULATION
#wrapping data and functions into a single until (object)

#Q1  Create account class with 2 attuibutes - balanced & account no 
#    create methods for debit, credit &printing the balanced

class account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
        
    def debit(self,amount):
        self.balance-=amount
        print('rs',amount,'debited')
        print('total balanced',self.get_balanced(),'rs')
        
    def credit(self,amount):
        self.balance+=amount
        print('rs',amount,'created')
        print('total balanced',self.get_balanced(),'rs')
        
    def get_balanced(self):
        return self.balance
            
        
acc1=account(10000,1415)
print(acc1.balance)
print(acc1.acc_no)  
acc1.debit(1000)
acc1.debit(9000)
acc1.credit(40000)
acc1.debit(563)
      