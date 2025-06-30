# Real-World Virtual ATM Machine Minor Project
import bank_balance
pin=1234
print("\t\t\t\t\t\t\tWelcome to HDFC ATM")
if "card"==input("Insert your card"):
    print("Welcome")
    if pin==int(input("Enter your pin")):
        print('''\t\t\t\t\t\t\t1) Check Balance\n\t\t\t\t\t\t\t2) Cash Withdraw''')
        option=int(input("Select your option"))
        if option==1:
            print("Your current balance is:",bank_balance.amount)
        elif option==2:
            user_amount=int(input("Enter your amount"))
            bank_balance=bank_balance.amount-user_amount
            file=open('bank_balance.py','w')
            file.write(f"amount={bank_balance}")
            file.close()
        else:
            print("Invalid Input")
    else:
        print("Wrong Pin")
else:
    print("Invalid Card")