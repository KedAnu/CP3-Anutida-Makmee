usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "VIP" and passwordInput=="superrich":
    print("--------------------------")
    print("---Welcome VIP costumer---")
    print("--------------------------")
    print("our Car for rent")
    print("1. BMW X1     price 40000 baht/month")
    print("2. BMW 320d   price 45000 baht/month")
    print("--------------------------")
    carInput=int(input("please choose the car: "))
    if carInput==1:
        monthInput=int(input("month :"))
        print("--------------------------")
        print("You need to pay =", 40000*monthInput,"baht")
        print("--------------------------")
    elif carInput==2:
        monthInput=int(input("month :"))
        print("--------------------------")
        print("You need to pay =", 45000*monthInput,"baht")
        print("--------------------------")
    else:
        print("--------------------------")
        print("error. Please try again")

else:
    print("--------------------------")
    print("username or password Incorrect")

