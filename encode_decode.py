def encodes(s):
    newst1=""
    count=1
    prev_element=s[0]
    
    for i in range(1,len(s)):
        if s[i]==prev_element:
            count+=1
        else:
            if count > 1:
                newst1+=prev_element+str(count)
            else:
                newst1+=s[i-1]
            prev_element=s[i]
            count=1
                
    if count==1:
        newst1+=prev_element
    else:
        newst1+=prev_element+str(count)
    
    return newst1

def decode(st):
    newst=""
    
    for i in range(len(st)):
        if st[i].isalpha():
            newst+=st[i]
        elif st[i].isnumeric():
            newst+=st[i-1]*(int(st[i])-1)
        
    return newst

s=input("enter the String to be enoded")
encod=encodes(s)
print(encod)
decod=decode(encod)
print("The Decoded String is",decod)
    