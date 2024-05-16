def decrementing_right_tri(n):
    count=0
    for i in range(n+1):
        count+=i
    
    for rows in range(n):
        for columns in range(rows+1):
            if count > 9:
                print(count, end=" ")
            else:
                print(count,end="  ")
            count-=1
        print()
        
        

n=int(input("enter the number of rows to be printed"))
decrementing_right_tri(n)

# output : enter the number of rows to be printed 6
# 21 
# 20 19
# 18 17 16
# 15 14 13 12
# 11 10 9  8  7
# 6  5  4  3  2  1