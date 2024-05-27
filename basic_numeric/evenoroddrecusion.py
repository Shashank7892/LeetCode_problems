# Python Program to Check if a Number is Odd or Even using recursion
def checkodd(n):
    if n < 2 :
        return n%2==0
    return checkodd(n-2)

n=int(input("enter the number"))
if checkodd(n)==True:
    print("Even")
else:
    print("Odd")
    