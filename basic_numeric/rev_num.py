# Python Program to Reverse a Number

def rev_num(n):
    rev=0
    
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
        
    print(rev)
    
n=int(input("enter the number"))
rev_num(n)