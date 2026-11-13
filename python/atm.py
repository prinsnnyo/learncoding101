#solution

balance = int(input("Enter your balance: "))
withdraw = int(input("How much you want to withdraw? "))
if withdraw > balance:
     print("You do not have enough money in your account")
else:
    balance - withdraw
    print("you have successfully withdrawn:" , withdraw,  "your new balance is: ", balance - withdraw)
    
    remain = balance - withdraw
    