def decreasing_triangle(n):
    for rows in range(n):
        for columns in range(rows,n):
            print("*", end=" ")
        print()
        


n=int(input("enter the number of rows to be printed"))
decreasing_triangle(n)

# o/p enter the number of rows to be printed 5
# * * * * * 
# * * * *
# * * *
# * *
# *