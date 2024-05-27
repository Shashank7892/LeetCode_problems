# Python Program to Check if a Number is a Palindrome

def palin_num(n):
    temp=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    print(rev)
    if temp==rev:
        print("its a palindrome")
    else:
        print("its not a palindrome")

n=int(input("enter the number"))
palin_num(n)
        
        

# tracing
  
# n=1221
# rem=5
# temp=0*10+1=1
# n=122

# n=122
# rem=2
# temp=1*10+2=12

# n=12
# rem=2
# temp=12*10+2=120+2=122

# n=1
# rem=1
# temp=122*10+1=1220+1=1221

# n=0
