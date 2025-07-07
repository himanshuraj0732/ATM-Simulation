Total_balance = 90000
choice = input("What you would like to do?\n Check balance Deposit Withdrwal (C or D or W): ").upper()

if choice == "C":
    print(f"Your balance is {Total_balance}")

elif choice == "D":
    deposit= int(input("Enter the amount you want to deposit in your bank: "))
    Total_balance +=deposit 
    print(f"you have deposit {deposit} in your bank , Now your balance is now {Total_balance} ")   

elif choice == "W":
    withdraw= int(input("Enter the amount you want to withdraw from your bank: "))
    if withdraw > Total_balance:
        print("This is insuffisiant amount , please enter again")  

    else:
        Total_balance -= withdraw
        print(f"you have withdraw {withdraw} from your bank now your bank has {Total_balance}") 

else:
    print("Oops, Something wrong please try again!!")           