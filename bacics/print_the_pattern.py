def printPat(n):
    #Code here
    for i in range(n):
        for j in range(n,0,-1):
            x=n-i
            while(x>0):
                print(j,end=" ")
                x-=1
        print(end="$")
            
            
            
            


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        printPat(n)
# } Driver Code Ends