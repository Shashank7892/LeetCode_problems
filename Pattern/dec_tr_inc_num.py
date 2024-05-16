def dec_tr_inc_num(n):
    i=1
    for rows in range(n):
        for columns in range(rows,n):
            if i <= 9:
                print(i,end="  ")
            else:
                print(i,end=" ")
            i+=1
        print()
n=int(input("enter the number of rows to be printed"))
dec_tr_inc_num(n)

# output: enter the number of rows to be printed 5
# 1  2  3  4  5  
# 6  7  8  9
# 10 11 12
# 13 14
# 15