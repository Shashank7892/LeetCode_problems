def fibonacci(n):
    fib1=0
    fib2=1
    if n==0 or n==1:
        print(n)
    else:
        print(fib1)
        print(fib2)
        for i in range(n-2):
            fib=fib1+fib2
            fib1=fib2
            fib2=fib
            print(fib)
        

n=int(input("enter the number of series to be printed "))
fibonacci(n)