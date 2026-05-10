import os 
import time 

#variables
tryes = 0
flag = False
found = False
acount_flag = False

#list of accounts in the system, each account is represented as a dictionary with its information
acounts =[{"uid": 0, "user": "0", "balance": 0, "pasword": 0, "history": [], "is_LOCKED": False},
             {"uid": 1, "user": "Admin", "balance": 5000, "pasword": 1111, "history": [], "is_LOCKED": False},
             {"uid": 2, "user": "User1", "balance": 3000, "pasword": 2222, "history": [], "is_LOCKED": False},
             {"uid": 3, "user": "User2", "balance": 7000, "pasword": 3333, "history": [], "is_LOCKED": False} ]

#seting up an infinite loop to keep the program running 
while True:
    flag = False
    found = False
    os.system("cls")
    print("Welcome to the ATM!")
    print("enter your userid")
    #getting the user id input and searching for the account with the given uid
    uid = input(":-")
    #searching for the account with the given uid and storing its information in variables for later use
    for account in acounts:
        if int(account["uid"]) == int(uid):
            print("Account_Found")
            user = account["user"]
            password = int(account["pasword"])
            balance = account["balance"]
            history = account["history"]
            is_LOCKED = account["is_LOCKED"]
            found = True
            break


    #checking if the account is found and if it's not the admin account, then allowing the user to access their account
    if found == True and int(uid) > 1:
        os.system("cls")
        print(f"welcome {user}")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. View Transaction History")
        print("5. Exit")
        #getting the user's choice and PIN input
        choice = input("Please select an option (1-5): ")
        pin = input("Please enter your PIN: ")
        #checking if the account is locked and preventing access if it is
        if is_LOCKED == True and int(uid) != 1:
            print("Your account is locked. Please contact the bank.")
            time.sleep(5)
        #dealing with incorrect PIN entry and locking the account after 3 failed attempts
        while pin != password and is_LOCKED == False:
            print("Incorrect PIN. Please try again.")
            pin = input("Please enter your PIN: ")
            tryes += 1
            if tryes == 2:
                is_LOCKED = True
                print("Your account has been locked due to too many incorrect attempts. Please contact the bank.")
                time.sleep(5)
                break
            time.sleep(5)
        #checking the user's provided PIN against the stored password and allowing access to the account if it matches
        if pin == password and is_LOCKED == False:
            #checking the user's choice and performing the corresponding action
            #displaying the balance
            if choice == 1:
                print(f"Your balance is: {int(balance)}")
            #withdrawing money and updating the transaction history
            elif choice == 2:
                amount = input("enter the amount you want to withdraw:-")
                #making sure the user enters a valid amount
                if amount > int(balance):
                    print("Insufficient funds.")
                #proceeding if the amount is valid
                else:
                    balance-=int(amount)
                    print(f"You have withdrawn {amount}. Your new balance is: {int(balance)}") 
                    history.append(f"withdrawn :- {amount} balance after transaction :- {balance}")

            #depositing money and updating the transaction history        
            elif choice == 3:
                amount = int(input("enter the amount you want to deposit:-"))
                #making sure the user enters a valid amount
                if amount <= 0:
                    print("invalid amount, please enter a positive number")
                    time.sleep(5)
                #priceding if the amount is valid
                else:
                    balance+=amount
                    print(f"You have deposited {amount}. Your new balance is: {balance}")
                    history.append(f"deposited :- {amount} balance after transaction :- {balance}")

            #displaying the transaction history in a more readable format    
            elif choice == 4:
                os.system("cls")
                print(f"Transaction history for {user}:")
                for transaction in history:
                    print(transaction)
                time.sleep(25)
            
            #displaying the exit message and making sure the user can exit the program
            elif choice == 5:
                print("Thank you for using the ATM. Goodbye!")

            #making sure the user enters a valid option
            else:
                print("invalid input, please choose a valid option between 1 and 5")
                time.sleep(5)   
            


    #Admin panel
    if found == True and (uid) == 1:
        #Admin login
        print("please enter the admin password:-")
        input_password = input(":-")
        #checking the admin password
        if input_password != password:
            print("incorrect password, you will be redirected to the login page")
            time.sleep(5)
        #suposing the admin enters the correct password, he will be directed to the admin menu
        else:
            while flag== False:
                acount_flag = False
                #clear the screen
                os.system("cls")

                #Admin menu
                print(f"welcome Admin")
                print("1. view all accounts")
                print("2. lock/unlock an account")
                print("3. add an account")
                print("4. exit")
                choice = int(input("enter your choice:-"))

                #All accounts view
                if choice == 1:
                    os.system("cls")
                    print("all accounts in the system:-")
                    for account in acounts:
                        print(f"uid:- {account['uid']} / user:- {account['user']} / balance:- {account['balance']} / is_LOCKED:- {account['is_LOCKED']}")
                    input("\nPress Enter to return to Admin Menu...")   

                #lock/unlock account       
                elif choice == 2:
                    os.system("cls")
                    print("enter the uid of the account you want to lock/unlock:-")
                    #get the uid of the account to be edited
                    input_uid = int(input(":-"))
                    #find the account with the given uid and edit its lock status
                    for edit_account in acounts:
                        if int(edit_account["uid"]) ==  input_uid:
                            #check lock status and change it accordingly
                            if edit_account["is_LOCKED"] == True:
                                print(f"account {edit_account['user']} is currently locked, do you want to unlock it? (y/n)")
                                input1 = input("enter your choice:-")
                                if input1 == "y":
                                    edit_account["is_LOCKED"] = False
                                    print(f"account {edit_account['user']} has been unlocked")
                                elif input1 == "n":
                                    print(f"account {edit_account['user']} will remain locked")
                            else:
                                print(f"account {edit_account['user']} is currently unlocked, do you want to lock it? (y/n)")
                                input1 = input("enter your choice:-")
                                if input1 == "y":
                                    edit_account["is_LOCKED"] = True
                                    print(f"account {edit_account['user']} has been locked")
                                elif input1 == "n":
                                    print(f"account {edit_account['user']} will remain unlocked")
                                time.sleep(2)
                
                elif choice == 3:
                    #Adding a new account
                    #Making sure the new account has a unique uid by taking the last account's uid and adding 1 to it
                    os.system("cls")
                    last_account_uid = acounts[-1]["uid"]
                    new_account_uid = last_account_uid + 1
                    #Getting the new account's username and password from the admin
                    print("enter the username for the new account:-")
                    new_account_user = input(":-")
                    #Making sure the admin enters the password correctly by asking for confirmation and comparing the two inputs
                    while acount_flag ==False:
                        #clear the screen and ask for the password and confirmation
                        os.system("cls")
                        print("enter the password for the new account:-")
                        new_account_password = int(input(":-"))
                        print("please re-enter the password for confirmation:-")
                        confirm_password = int(input(":-"))
                        if new_account_password == confirm_password:
                            new_account = {"uid": new_account_uid, "user": new_account_user,"balance":1000 , "password":new_account_password, "history": [], "is_LOCKED": False}
                            acounts.append(new_account)
                            print(f"account for {new_account_user} has been created with uid {new_account_uid} and a initial balance of 1000")
                            acount_flag = True
                            input("Press Enter to return to Admin Menu...")

                        else:
                            print("passwords do not match, please try again")
                            input("Press Enter to try again...")
                        


                #Making sure the admin can exit the admin panel and return to the login page
                elif choice == 4:
                    print("you will be logged out and redirected to the login page")
                    time.sleep(5)
                    flag = True

                #Making sure the admin enters a valid option
                else:
                    print("invalid input, please chose a valid option between 1 and 3")

    #Updating the account information after the transaction
    elif found:
        account["balance"]= balance
        account["history"]= history
        account["is_LOCKED"]= is_LOCKED
    time.sleep(2)


    #showing an error message if the account is not found
    if found == False:
        print("account not found")
        time.sleep(2)