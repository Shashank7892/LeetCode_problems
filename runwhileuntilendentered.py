# terminate the loop when user enters end and also with else clause

#i.e loop with break statement

while True:
    user_input=input("enter the name")
    
    if user_input=="end":
        print("the loop terminated")
        break;
    
    print(f'Hi{user_input}')

