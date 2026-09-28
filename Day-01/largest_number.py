num_1 = int(input("enter a num:"))
num_2 = int(input("enter a num:"))
num_3 = int(input("enter a num:"))

if num_1 > num_2 and num_1 > num_3:
  print("larger number :", num_1)
elif num_2 > num_1 and num_2 > num_3:
  print("larger number :", num_2)
else:
  print("larger number :", num_3)