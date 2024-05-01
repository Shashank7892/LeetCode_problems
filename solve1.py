
def solve(s,ch):
    newstr=""
    
    if ch not in s:
        return s
    else:
        a=s.index(ch)
        for i in s:
            if i==ch:
                newstr=i+newstr
                break
            newstr=i+newstr
        
        
        for d in range(a+1,len(s)):
            newstr+=s[d]
        
        return newstr

s=input("enter the string")#abcdefghij
ch=input("enter the character")#e
print(solve(s,ch))
