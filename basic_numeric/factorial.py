def fact(n):
    facts=1
    for i in range(1,n+1):
        facts=facts*i
    print(facts)
    
n=int(input("enter the number "))
fact(n)