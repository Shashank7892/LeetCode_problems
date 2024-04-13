n=int(input("enter the array size"))
lst=[]
for i in range(n):
    x=input()
    lst.append(x)
pos=int(input("enter the position the element to be inserted"))
ele=input()
print("the array before insertion:",lst)
lst.insert(pos-1,ele)
print("the array after insertion is:",lst)