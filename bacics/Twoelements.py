def check_status(a, b, flag):
    
    if ((a<0 and b>0) and flag==False) or ((a>0 and b<0) and flag==False) or((a<0 and b<0) and flag==True) :
        return True
    else:
        return False
    
def main():
    testcases=int(input())
    while(testcases > 0):
        a=int(input())
        b=int(input())
        flag=input()
        if flag=="True":
            flag=True
        else:
            flag=False
            
        if (check_status(a,b,flag) is True):
            print("True")
        else:
            print("False")
        
        testcases-=1
    
if __name__=="__main__":
    main()        
    