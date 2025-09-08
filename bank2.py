import time
import re
import datetime
#---------Amouont withdrawal--------
def Withdrawal(w):
    time.sleep(2)
    print(f"\u20B9 {w} has successfully Withdrawn")
#---------Amount Depositing --------
def Deposit(d):
    time.sleep(2)
    print(f"\u20B9 {d} has been successfully Deposited")
#---------- showing account balance------
def Show_Balance(a):
    print("Fetching Bank Balance")
    time.sleep(2)
    print("--------Bank Balance Fetched Successfully--------")
    print()
    time.sleep(2)
    print(f"\tTotal Amount Available :\u20B9 {a}")
    print()
    print("\tThank You. Have a Nice Day!!")
    print("-------------------------------------------------")
#--------Exiting from Program---------------
def Exit():
    time.sleep(2)
    print("Thank You. Have a Nice Day!!")

    exit()
#---------Pin reseting ----------------
def pin():
        x=input("Enter your Old Pin: ")
        y=input("Enter your New Pin: ")
        if x.isdigit():
           if y.isdigit():
              if x!=y:
                time.sleep(2)
                print("Pin Changed Successfully!!")
                print("\t\t\t To Access Your Account, Login Again!!")
                exit()
              else:
                print("New PIN should not be same as the old PIN")
                time.sleep(2)
                print("Set New Pin")
                pin()
           else:
              print("Pin should be Numeric:")
              pin()
        else:
            print("PIN should be Numeric: ")
            pin()
#----------Validating Card-----------
l=3
k=0
def card():
    global l,k
    p=input("Enter card No. (xxxx-xxxx-xxxx-xxxx):")
    pattern=r"^\d{4}-\d{4}-\d{4}-\d{4}$"
    if re.match(pattern,p):
        print("Thanks Welcome !!!")
        main()
    else:
        while k<=3:
              print("Invalid card number")
              k=k+1
              l=l-1
              print(f"----only {l} Attempt(s) left----")
              if k==3:
                print("\t\t\t\t---------------------------------")
                print("\t\t\t\t| Attempt Limit Exceeded        |")
                print("\t\t\t\t| Try Again After Some Time     |")
                print("\t\t\t\t---------------------------------")
                exit()
              else:
                card()
#-----vlaidating Pin----------
def Pass():
    
    global l,k
    p=input("Enter 4-Digit Pin :")
    pattern=r"^\d{4}$"
    if re.match(pattern,p):
            print("Thanks Welcome !!!")
            main()
    else:
       
        while k<=3:
            print(">>> PIN Should Be 4 digits")

            k=k+1
            l=l-1
            
            print(f"----only {l} Attempts left----")
            if k==3:
                print("\t\t\t\t---------------------------------")
                print("\t\t\t\t| Attempt Limit Exceeded        |")
                print("\t\t\t\t| Try Again After Some Time     |")
                print("\t\t\t\t---------------------------------")
                exit()
            else:
                Pass()
                  
a=100
temp=a
m=[]
j=[]
#------------Accessing Account ------------------
def main():
  global a,temp,m,j
  while True:
    print("-------------------------------------------------------------")
    print("\t\t WELCOME TO BANK OF INDIA")
    print("-------------------------------------------------------------")

    print("1.Withdrawal")
    print("2.Deposit")
    print("3.Show Balance")
    print("4.Mini Statement")
    print("5.Exit")
    n=int(input("Enter any Option from Above="))
    if n==1:
        print(f"Total Available Balance to be Withdrawal:\u20B9 {a}")
        w=float(input("Enter amount to be Withdrawal:\u20B9 "))
        if (w>=0) :
           if (w<a) :
              a-=w
              m.append(f"\u20B9 {w}\t is debited")
              j.append(a)
              Withdrawal(w)
           else:
              print("Insufficient Balance...") 
        else:
            print("Amount Should be Greater than 0 and Less than or equal to Available Amount")
            
    elif n==2:
        d=int(input("Enter amount to be Deposit:\u20B9 "))
        if d>0:
            a=a+d
            m.append(f"\u20B9 {d}\t is credited")
            j.append(a)
            Deposit(d)
        else:
            print("Invalid amount")
    elif n==3:
        Show_Balance(a)
    elif n==4:
        z=len(m)
        now=datetime.datetime.now()
        print("---------------------------Mini Statement----------------------------")
        if len(j) == 0:  # FIX: Prevent IndexError if no transaction happened
                print("No transactions yet.")
        else:
                print(f"\t\t\t\t\t Total Amount : \u20B9 {j[-1]}")
                print(f"\t\t\t\t\t Time : {now.strftime('%y-%m-%d %H:%M:%S')}")  # FIX: changed double to single quotes

                for i in range(0, z):
                    print(f"| \t {m[i]} \t Available : \u20B9 {j[i]}")
        print("---------------------------------------------------------------------")
       
    elif n==5:
        Exit()
    else:
        print("Invalid Enter Option bw 1-4: ")
#-------------Account Validation -----------------
print("-------------------------------------------------------------")
print("\t\t WELCOME TO BANK OF INDIA")
print("-------------------------------------------------------------")
print("\t\t\tHi Welcome!!!!")
print("Login Your Account with : ")
print(" 1.Pin \n 2.Card No. \n 3.Reset Pin")
r=int(input("select the option : "))
if r==1:
       Pass()
elif r==2:  
       card()
elif r==3:
       pin()
else:
       print("Invalid choice!!")