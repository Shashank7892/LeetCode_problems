# Calculate the sum of numbers until user enters 0 and get the count of greater than zero numbers

number=int(input("enter the number"))

sums=0
count=0

while number!=0:
    sums+=number
    count+=1
    number=int(input("enter the number again"))
else:
    print("stopped")
    
print("The sum of all numbers before entering zero is",sums)
print("The number of times the user entered greater the zero number is",count)