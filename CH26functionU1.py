# block of statements that perform a specific task
a=3
b=2
sum=a+b
print(sum)
               #insead of printing again and again use function

#function definition
def sumofnum(a,b):
    sum=a+b
    print(sum)
    return sum

#function call
sumofnum(6,4)
sumofnum(4,8)
sumofnum(6,6)
sumofnum(8,5)

def multi_num(c,d):
    return c*d

multiple=multi_num(2,5)
print(multiple)


#average of numbers
def avgofnum(m,n,o):
    sum=m+n+o
    avg=sum/3
    print(avg)
    return avg

avgofnum(3,4,6)

