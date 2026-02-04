# for i in range(1,11,2):
#     print(i) 
    
# for i in range(11,1,-2):
#     print(i)    

# for i in 'sanjay':
#     print(i)


row=int(input("enter rows:"))
for i in range(0, row+1):
    for j in range(0,i):
        print('*',end=' ')
    print("")
          