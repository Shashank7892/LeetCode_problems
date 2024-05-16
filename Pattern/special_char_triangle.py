def special_char_tri(n):
    special_list=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','?','{','}','[',']']
    i=0
    for rows in range(n):
        for columns in range(rows+1):
            print(special_list[i],end=" ")
            if i == len(special_list)-1:
                i=0
            else:
                i+=1    
        print()

n=int(input("enter the number of rows to be printed"))
special_char_tri(n)


# o/p enter the number of rows to be printed 10
# ! 
# @ #
# $ % ^
# & * ( )
# _ - + = ?
# { } [ ] ! @
# # $ % ^ & * (
# ) _ - + = ? { } 
# [ ] ! @ # $ % ^ &
# * ( ) _ - + = ? { }