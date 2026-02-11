#when a function calls itself repeatedly

def show(n):
    for i in range(1,n+1):
        if (n==0):
            return            # without recursion
        else:
            print(n)
            n-=1
show(5)

print(sep=' ')


def show2(m):
    if (m==0):
        return                # with recursion
    print(m)
    show2(m-1)
show2(5)


def fact(x):
    if(x==0 or x==1):
        return 1
    return fact(x-1) * x
print(fact(5))