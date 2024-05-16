def right_number_triangle(n):
    for rows in range(n):
        for columns in range(rows+1):
            print(columns+1, end=" ")
        print()

n=int(input("enter the number of rows to print triangle"))
right_number_triangle(n)

# o/p enter the number of rows to print triangle 5
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5