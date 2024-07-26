def squarepattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
n=int(input("enter the number"))
squarepattern(n)
