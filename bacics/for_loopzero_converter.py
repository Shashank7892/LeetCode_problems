def pos(n):
    for i in range(n,0,-1):
        print(i-1,end=" ")
    
        
    
def neg(n):
    for i in range(n,1,1):
        print(i,end=" ")
    


def main():
    testcases=int(input()) 
    while(testcases>0):
        n = int(input())
        if(n > 0):
            pos(n)
        elif(n < 0):
            neg(n)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        


if __name__=='__main__':
    main()