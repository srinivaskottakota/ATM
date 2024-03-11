from main import passencript,passcodeencription
def ATM():
    userdetails={'srinivas':'utkpkxcu_14','ganesh':'Icpguj_60','bindu':'dkpfw30'}
    userpin={'srinivas':5488,'ganesh':8744,'bindu':8684}
    userammount={'charan':50000,'ganesh':60000,'bindu':80000}
    try:
        username=input("Enter User Name :")
        password=userdetails[username]
        passcount=1
        flag=0
        passcode=input("Enter your password :")
        passcode=passencript(passcode)
        while(passcount<3 and flag!=1):
            if passcode==password:
                flag=1
                break
            else:
                passcode=input("You have only {} chance \nEnter your password :".format(3-passcount))
                passcode=passencript(passcode)
                passcount=passcount+1
        else:
            print("You account is blocked")
            return
        if flag==1:
            print("1)Withdraw\n2)Deposite\n3)Balance\n4)Reset password")
            choice=int(input("Enter your choice :"))
        if choice==1:
            amount=int(input("Enter the ammount :"))
            pin=int(input("Enter your pin :"))
            pin=passcodeencription(pin)
            if ((userpin[username])==pin):
                if ((userammount[username])>=amount):
                    print("Please take your money :",amount)
                    print("\nDo you what to check balance\n1)Yes\n2)No")
                    bal=int(input("Enter your choice :"))
                    if bal==1:
                        print("Your remaining ammount:",(userammount[username])-amount)
                        userammount[username]=(userammount[username])-amount
                        return
                    else:
                        userammount[username]=(userammount[username])-amount
                        return
                else:
                    print("Insufficient funds")
                    return
            else:
                print("You entered worng pin")
                return
        if choice==2:
            useramt=int(input("Enter amount to be deposite :"))
            userval=userammount[username]
            pins=int(input("Enter your pin :"))
            pins=passcodeencription(pins)
            if ((userpin[username])==pins):
                userammount[username]=userval+useramt
                print("Your account balance :",userammount[username])
                return
            else:
                print("You have entered worng pin")
                return
        if choice==3:
            pinss=int(input("Enter your pin :"))
            pinss=passcodeencription(pinss)
            if userpin[username]==pinss:
                print("Your account balance :",userammount[username])
                return
            else:
                print("You have entered Wrong pin ")
                return
        if choice==4:
            p=int(input("Enter your pin :"))
            p=passcodeencription(p)
            password1=userpin[username]
            if p==password1:
                cpass=input("Enter your current password :")
                cpass=passencript(cpass)
                if ((userdetails[username])==cpass):
                    new_pass=input("Enter your new password:")
                    new_pass=passencript(new_pass)
                    userdetails[username]=new_pass
                    print("New password updated")
                    return
                else:
                    print("You have entered wrong password")
                    return
            else:
                print("You have entered Worng pin")
                return
    except:
        print("invalid username")
        return
ATM()
print("END")
