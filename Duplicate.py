def Duplicate(array):
    d={}

    for i in array:
        d[i]=array.count(i)
    
    for x in d:
        if d[x]>1:
            return x
        


array=[3,3,3,3]
print(Duplicate(array))