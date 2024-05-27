def cat_hat(str):
    #using slicing
    i=j=0
    for x in range(len(str)):
        if str[x:x+3]=="cat":
            i+=1
        if str[x:x+3]=="hat":
            j+=1
    if i==j:
        return True
    else:
        return False
    # c_cat=str.count("cat")
    # c_hat=str.count("hat")
    # if c_cat==c_hat:
    #   return True
    # else:
    #   return False
    

def main():   
       
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(cat_hat(str))
        testcases-=1
        


if __name__=='__main__':
    main()
