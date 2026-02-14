class car:
    def __init__(self,type):
        self.type=type
        
    @staticmethod    
    def start():
        print('car started')
        
    @staticmethod    
    def stop():
        print('car stopped')
        
class toyotacar(car):
    def __init__(self,brand,type):
        self.brand=brand 
        super().__init__(type)  
        super().start()             
                       
c1=toyotacar('thar', 'disel')
print(c1.brand)   
print(c1.type)
print(c1.start())#if you want to call its parent class use super methods                   