#private attrubutes & methods are meant to be used only within the class and are now accessible from outside the class

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  #this (__ double underline keeps the object private)
        
    def resetpass(self):
        print(self.__acc_pass)    
        
acc1=Account(12345,'abcde')
# print(acc1.__acc_pass)  #this will give error b/c pass was private
print(acc1.resetpass()) 
       
        
        