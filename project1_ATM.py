# user details already given
u1_acno = 1001
u1_name = "Rohan Sharma"
u1_dob = "24-08-2025"
u1_pin = 2408
u1_bal = 10000

u2_acno = 1002
u2_name = "Priya Verma"
u2_dob = "16-04-2025"
u2_pin = 1234
u2_bal = 20000

u3_acno = 1003
u3_name = "Anil Kumar"
u3_dob = "21-09-2025"
u3_pin = None
u3_bal = 10000
print("Welcome !")
print()
while True:
    # show all options that we have and then ask user to select an option
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Pin generation")
    print("4. Mini statement")
    print("5. Exit")
    print()
    option = int(input("Choose your option: "))
    if option==5:
        print("Thank you!")
        break
    elif option==4:
        print("Mini statement")
        print()
        accno = int(input("Enter account number: "))
        pin = int(input("Enter pin: "))
        if accno == u1_acno:
            if u1_pin is None:
                print()
                print("Pin not generated yet")
            elif pin == u1_pin:
                print()
                print("**Account details**")
                print(f"Account number: {u1_acno}")
                print(f"Name: {u1_name}")
                print(f"DOB: {u1_dob}")
                print(f"Balance: {u1_bal}")
            else:
                print()
                print("Invalid pin!")
                print("Try again")
        elif accno == u2_acno:
            if u2_pin is None:
                print()
                print("Pin not generated yet")
            elif pin == u2_pin:
                print()
                print("**Account details**")
                print(f"Account number: {u2_acno}")
                print(f"Name: {u2_name}")
                print(f"DOB: {u2_dob}")
                print(f"Balance: {u2_bal}")
            else:
                print()
                print("Invalid pin!")
                print("Try again")
        elif accno == u3_acno:
            if u3_pin is None:
                print()
                print("Pin not generated yet")
            elif pin == u3_pin:
                print()
                print("**Account details**")
                print(f"Account number: {u3_acno}")
                print(f"Name: {u3_name}")
                print(f"DOB: {u3_dob}")
                print(f"Balance: {u3_bal}")
            else:
                print()
                print("Invalid pin!")
                print("Try again")
        else:
            print()
            print("Account does not exist!")
            print()

    elif option==3:
        print("Pin generation")
        print()
        accno =int(input("enter acct number: "))
        if accno == u1_acno:
            if u1_pin is not None:
                print("Pin already generated")
            else:
                pin1 = int(input("Enter pin: "))
                while True:
                    pin2 = int(input("Confirm pin: "))
                    if pin1==pin2:
                        u1_pin=pin1
                        print("Pin generated sucessfully")
                        break
                    else:
                        print("Confirm correct pin")
        elif accno == u2_acno:
            if u2_pin is not None:
                print("Pin already generated")
            else:
                pin1 = int(input("Enter pin: "))
                while True:
                    pin2 = int(input("Confirm pin: "))
                    if pin1==pin2:
                        u2_pin=pin1
                        print("Pin generated sucessfully")
                        break
                    else:
                        print("Confirm correct pin")
        elif accno == u3_acno:
            if u3_pin is not None:
                print("Pin already generated")
            else:
                pin1 = int(input("Enter pin: "))
                while True:
                    pin2 = int(input("Confirm pin: "))
                    if pin1==pin2:
                        u3_pin=pin1
                        print("Pin generated sucessfully")
                        break
                    else:
                        print("Confirm correct pin")
        else:
            print()
            print("Account doesnot exist!")
            print("try again")
            print()
    elif option==2:
        print("Deposit")
        print()
        acno = int(input("Enter account number: "))
        if u1_acno==acno:
            amt=int(input("Enter amount to deposit: "))
            u1_bal+=amt
            print("Deposit successful")
        elif u2_acno == acno:
            amt = int(input("Enter amount to deposit: "))
            u2_bal += amt
            print("Deposit successful")
        elif u3_acno == acno:
            amt = int(input("Enter amount to deposit: "))
            u3_bal += amt
            print("Deposit successful")
        else:
            print()
            print("Account number does not exist")
            print()
    elif option==1:
        print("Withdrawal")
        print()
        acno=int(input("Enter account number: "))
        if u1_acno==acno:
            if u1_pin is None:
                print("Pin not generated")
            else:
                pin=int(input("Enter pin: "))
                if pin==u1_pin:
                    amt=int(input("Enter amount: "))
                    if amt<=u1_bal:
                        u1_bal-=amt
                        print("Withdrawal successful")
                    else:
                        print("Insufficient balance")
                else:
                    print("Invalid pin")
        elif u2_acno==acno:
            if u2_pin is None:
                print("Pin not generated")
            else:
                pin = int(input("Enter pin: "))
                if pin == u2_pin:
                    amt = int(input("Enter amount: "))
                    if amt <= u2_bal:
                        u2_bal -= amt
                        print("Withdrawal successful")
                    else:
                        print("Insufficient balance")
                else:
                    print("Invalid pin")
        elif u3_acno==acno:
            if u3_pin is None:
                print("Pin not generated")
            else:
                pin = int(input("Enter pin: "))
                if pin == u3_pin:
                    amt = int(input("Enter amount: "))
                    if amt <= u3_bal:
                        u3_bal -= amt
                        print("Withdrawal successful")
                    else:
                        print("Insufficient balance")
                else:
                    print("Invalid pin")
        else:
            print()
            print("Account does not exist")
            print()
    else:
        print("Choose correct option")
        print()

