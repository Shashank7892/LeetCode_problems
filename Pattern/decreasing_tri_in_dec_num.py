def decreasing_tri_in_dec_num(n):
    for rows in range(n):
        for columns in range(rows,n):
            print(n-columns,end=" ")
        print()

n=int(input("enter the number of rows to be printed"))
decreasing_tri_in_dec_num(n)


# output: enter the number of rows to be printed 5
# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1