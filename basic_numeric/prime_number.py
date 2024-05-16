def prime_number(n):
    k=0
    print(n)
    for i in range(2,n//2+1):
        if n % i == 0:
            k+=1
            break
    if k < 1:
        print(n,"It's a prime number")
    else:
        print(n,"It's not a prime number")

n=int(input("enter the number"))
prime_number(n)   