def fibbo(n):
    fib1=0
    fib2=1
    if n==0 or n==1:
        print(n)
    else:
        print(fib1)
        print(fib2)
        while(n-2 > 0):
            fib=fib1+fib2
            fib1=fib2
            fib2=fib
            print(fib)
            n-=1

n=int(input("enter the number of series to be printed "))
fibbo(n)