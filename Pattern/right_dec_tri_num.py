def right_dec_tri_num(n):
    for rows in range(n):
        for columns in range(rows+1):
            print(n-columns, end=" ")
        print()
        
n=int(input("enter the number of rows to be printed"))
right_dec_tri_num(n)


# output: enter the number of rows to be printed 5
# 5 
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1