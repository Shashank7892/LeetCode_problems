def evenodd(n):
    if n & 1==0:
        print("even")
    else:
        print("odd")
    
n=int(input("enter the number"))
evenodd(n)