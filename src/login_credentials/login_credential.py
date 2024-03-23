def login(login_title :str,login_name :str):
    default_username='admin'
    default_password='admin'
    while(True):
        print("-"*45)
        print("\t\tGENERAL AI")
        print("-"*45)
        print(login_name)
        print(login_title +"...")
        print("-"*45)
        username=input("Enter the username:")
        password=input("Enter the password:")
        temp=0
        if default_username == username and default_password == password:
            print(f"Login Sucessfull!")
            print("-"*45)
            temp=1
            return True
        else:
            print("Sorry,Credentials didn't match!Please try again.")
        if temp==1:
            break
