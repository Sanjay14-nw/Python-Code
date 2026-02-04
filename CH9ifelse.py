#correct email abcgmail
#correct password 1234

email=input("enter your email:")
password=input("enter your password: ")

if email=="abcgmail" and password=="1234":
 print("welcome")
elif email=="abcgmail" and password != "1234":
    print("incorrect password")
    password=input("enter pasword again:")
    if password=="1234":
        print("correct password, now restart the website ")
    else:
        print("incorrect again")    
else:
     print("incorrect detail") 