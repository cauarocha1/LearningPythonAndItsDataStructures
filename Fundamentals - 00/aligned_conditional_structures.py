normal_account = False
university_account = True
special_account = False

balance = 2000
withdraw = 1500
special_check = 500

if normal_account:
    
    if balance >= withdraw:
        print("Withdraw made with sucess!")
    elif withdraw <= balance + special_check:
        print("Withdraw sucess using Special Check!")
    else:
        print("insufficient balance!")
        
elif university_account:
    
    if balance >= withdraw:
        print("Withdraw made with sucess!")
    else:
        print("insufficient balance!")
        
elif special_account:
    print("Special Account chosen")
    
else:
    print("Your account doesnt exists, please contact your master")