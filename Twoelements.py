def repeated(A):
    l=[]
    s=[]
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]==A[j]:
                l.append(A[j])
                s.append(j)
    print(l)
    print(s)
    
    for x in range(0,len(s)):
        for y in range(x+1,len(s)):
            if s[x]>s[y]:
                l[x],l[y]=l[y],l[x]
    print(l)

A=[1,2,3,3,1,2]
repeated(A)