country=['india','america','pakistan','japan','turkey','korea','nepal']

def print_list(list):
    print(list[0])
    print(list[1])
    print(list[2])
    print(list[3])
    print(list[4])
    print(list[5])
    print(list[6])
    print(len(list))
    
print_list(country)   

#3 WAF to find the factorial of n.(n is the parameter)

# def factorial_num(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)

# n=int(input('enter the number:'))    
# factorial_num(n)        

#4 WAF to convert USD to INR

# def convert_money(inr):
#     usd=92
#     for i in range(1,inr):
#         i+=1
#     usd=usd*i
#     print(usd)

# inr=int(input('enter the amount:'))
# convert_money(inr)

#5 WAF to give the even and odd number

def even_odd(num):
    if (num%2==0):
        print('EVEN')
    else:
        print('ODD')    

num=int(input('enter the number:'))
even_odd(num)
    