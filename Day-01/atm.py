acc_no = int(input("Enter your account number:"))
balance = int(input("enter your balance:"))
with_drawl_amount = int(input("enter the amount to withdraw:"))

if with_drawl_amount > balance:
  print("Insufficient Balance")
else:
  balance = balance - with_drawl_amount
  print("Transaction Successful")
  print("Remaining Balance:", balance)