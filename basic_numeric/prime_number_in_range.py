def prime_in_range(n):
    for i in range(2,n+1):
        k=0
        for x in range(2,i//2+1):
            if i % x ==0:
                k+=1
        if k < 1:
            print(i)
    

n=int(input("enter the range"))
prime_in_range(n)
