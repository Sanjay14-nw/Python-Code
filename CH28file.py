# f=open('CH28.txt','r') # to open the file
# data=f.read(15)          # to read the file
# print(data)          
# print(type(data))
# f.close()              #to close the file 

# 'r' =open for reading 
# 'w' =open for writing 
# 'x' =crate a new file and open it for writing 
# 'a' =open for writing 
# 'b' =binary mode 
# 't' =text mode 
# '+' =open a disk file for updating 

# f=open('CH28.txt','r')
# data2=f.readlines()
# print(data2)

#WRITING TO A FILE
# f=open('CH28.txt','w')
# f.write('\n and also with campusx')  #overwrites the enrtire file 
# f.close()

# f=open('CH28.txt','a')
# f.write('and also with campusx')     #adds to the file 

                            #WITH Syntax
with open('CH28.txt','a') as f:
    data=f.read( )          # it close the file automatically
    print(data)
    
    

