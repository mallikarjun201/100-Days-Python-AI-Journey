
Balance = 1000

while True:
  

  choice = input("Enter your choice (1-4): ")
  if choice == '1':
    print(f"Balance: ${Balance}")
  elif choice =='2':
    amount = float(input("enter amount: "))
    Balance += amount
    print(f"Balance: ${Balance}")
  elif choice == '3':
    amount = float(input("enter amount:"))
    if amount > Balance:
      print("Insufficient funds.")
    else:
      Balance -= amount
      print(f"Balance: ${Balance}")
  elif choice == '4':
    print("Thank you !")
    break
  
    
