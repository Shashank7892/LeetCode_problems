#Python Program to Print All Odd Numbers in a Range

def odd_in_range(n):
    for i in range(1,n+1):
        if i%2==1:
            print(i)

n=int(input("enter the range of numbers to be printed"))
odd_in_range(n)