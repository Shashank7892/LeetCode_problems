def decreasing_num_tri(n):
    for rows in range(n):
        for columns in range(rows,n):
            print(columns+1, end=" ")
        print()

n=int(input("enter the number of rows to be printed"))
decreasing_num_tri(n)

# o/p enter the number of rows to be printed 5
# 1 2 3 4 5 
# 2 3 4 5
# 3 4 5
# 4 5
# 5
