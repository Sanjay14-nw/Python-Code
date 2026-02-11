def sum_n(num):
    if (num==0 or num==1):
        return 1
    return sum_n(num-1)+num
        
sum=sum_n(10)
print(sum)