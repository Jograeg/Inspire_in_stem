# write a program to withdraw both 25,000 if account balance is between ksh 100,000 to 200,000
#30% if acc balance is btwn 500,000 to 1m
#above 1m deduct 15,000

acc_bal = input("enter your acc_bal")
acc_bal=0
if (int(acc_bal) > 100,000 and int(acc_bal) < 200,000):
    acc_bal = acc_bal - 25,000
    print(" we have deducted ksh 25,000")   
elif (int(acc_bal) > 1,000,000 and int(acc_bal) < 6,000,000):
       acc_bal = acc_bal - (0.3*acc_bal)
       print(" we have deducted 30 percent from your account")
elif (int(acc_bal) > 1,000,000):
    acc_bal = acc_bal-15,000
    print("we have deducted ksh 15,000 from your account")
