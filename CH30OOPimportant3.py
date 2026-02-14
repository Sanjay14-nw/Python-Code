                                                              #INDERITANCE
#single inderitance
class car:
    @staticmethod
    def start():
     print('car started')
     
    @staticmethod
    def stop():
        print('car stop')
    
class toyotacar(car):
    def __init__(self,brand):
        self.brand=brand
        
c2=toyotacar('thar')
print(c2.start())        
                

#MULTI-LEVEL inheritanceclass 
class car:
    @staticmethod
    def start():
     print('car started')
     
    @staticmethod
    def stop():
        print('car stop')
    
class toyotacar(car):
    def __init__(self,brand):
        self.brand=brand
        
class fortuner(toyotacar):
    def __init__(self,type):
         self.type=type
                         
                         
car1=fortuner('petrol')
print(car1.start())   

#making many class like single inheritance

#MULTOPLE INHERITANCE
class A:
    vara='welcome to class A'
    
class B:
    varb='welcome to class b'
    
class C(A,B):
    varc='welcome to class c'  
    
    
c1=C()
print(c1.varc)
print(c1.varb)
print(c1.vara)          