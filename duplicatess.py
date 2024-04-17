def duplicates(self, arr, n):
    d={}
    x=[]
    for i in arr:
    	if i in d:
    	    d[i]+=1
        else:
    	    d[i]=1	        
    for i in d.keys():
    	if d[i]>1:
    	    x.append(i)
    x.sort()
    if len(x)!=0:
    	return x
    else:
    	return [-1]