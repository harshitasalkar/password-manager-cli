def add_account():
    while True:
        website=input("Enter website:")
        username=input("Enter username:")
        password=input("Enter password:")

        with open("passwords.txt","a") as f:
            f.write(website+","+username+","+password+"\n")

        print("Account saved!")
        add_more=input("Do you want to add more accounts?(y/n):").lower()
        if add_more=="y":
            continue
        elif add_more=="n":
            break
        else:
            print("Invalid input.")

def view_accounts():
    try:
        with open("passwords.txt","r") as f:
            accounts=f.readlines()
        if len(accounts)==0:
            print("No accounts available.")
            return
        for i in range(len(accounts)):
            website,username,password=accounts[i].strip().split(",")
            print(i+1,".",website,"|",username,"|","******")       
    except FileNotFoundError:
        print("No accounts found.")

def search_account():
    try:
        with open("passwords.txt","r") as f:
            accounts=f.readlines()

        if len(accounts)==0:
            print("No tasks to replace.")
            return
        word=input("Enter word to search:").lower()
        found=False
        for i in range(len(accounts)):
            if word in accounts[i].lower():
                website,username,password=accounts[i].strip().split(",")
                print(i+1,".",website,"|",username,"|","******") 
                found=True
        if found:
            print("Word found!")
        else:
            print("No matching found!")

    except FileNotFoundError:
        print("No accounts saved yet.")


while True:
    print("1. Add account")
    print("2. View accounts")
    print("3. Search account")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_account()
    elif choice == "2":
        view_accounts()
    elif choice == "3":
        search_account()
    elif choice == "4":
        break
    else:
        print("Invalid choice")