def magicstring(input1):
    s1=input1[-1]
    count=0
    for i in input1:
        if i !=s1:
            count+=1
    return(count)
    
input1=input("enter the String")
print(magicstring(input1))