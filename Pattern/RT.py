def RT(n):
    for i in range(n):
        for j in range(i+1):
            print("* ",end=" ")
        print()

n=int(input("Enter the n value"))
RT(n)