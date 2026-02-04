# import random
# jackpot=random.randint(1,100)
# guess=int(input("guess the number:"))
# count=1

# while guess != jackpot:
#     if guess<jackpot:
#         print("guess higher")
#     else:
#         print("guess lower")
            
#     guess=int(input("guess the number:"))
#     count+=1
    
# print("correct guess")
# print("total guesses",count)

# import random
# chances=random.randint(1,6)
# guess=int(input("i have three chances guess it right: "))
# count=1
# while guess!=chances:
#     if guess<chances:
#         print("guess higher")
#         print("try again")
#     elif count==3:
#         break    
#     else :
#         print("guess lower")
#     guess=int(input("i have three chances guess it right: "))
#     count+=1
# print("correct")  
        
        
import random
chances=random.randint(1,50)
chances=random.randint(1,50)
chances=random.randint(1,50)
chances=random.randint(1,50)
guess=int(input("guess the number:"))
while guess!=chances:
    print("try again")
    guess=int(input("guess the number:"))
        
print("correct")