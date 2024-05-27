def printIncreasingPower(x):
    num=1
    while(num*num<=x):
        
        print (num*num, end = " ")
        num+=1
       
def main():
    
    
    testcases = int(input())
    
    
    while(testcases > 0):
        x = int(input())
        
        printIncreasingPower(x);
        print ()
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
