def isPalindrome(x):
    x=str(x)
    if x[::-1]==x:
        return True
    else:
        return False
    
    # return x==x[::-1]
    
    # using ternary operator
    # return True if x==x[::-1] else False

    
x=int(input("enter the number"))#-121
print(isPalindrome(x))#false
