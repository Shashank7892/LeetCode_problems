def right_triangle(n):
    for rows in range(n):
        for columns in range(rows+1):
            print("*", end=" ")
        print()

n=int(input("Enter the number of rows to print triangle"))
right_triangle(n)

# Enter the number of rows to print triangle 5
# * 
# * *
# * * *
# * * * *
# * * * * *