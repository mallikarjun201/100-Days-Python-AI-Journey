# while loop to print numbers from 1 to 10

i = 1

while i <=10:
  print(i)
  i = i + 1

# ___________________________________
# for loop to print numbers from 1 to 5
for i in range(1,6):
  print(i)


# ------------------------------------------
#  for loop toprit even numbers
for i in range(1,11):
  if i %2 == 0:
    print(i)

# ------------------------------------------
# sum of numbers from 1 to 10
sum = 0

for i in range(1,11):
  
  sum = sum +i
print(sum)


# ------------------------------------------

# multiplication table

num  = int(input("enter a number: "))

for i in range(1,11):
  print(num, "x", i, "=",num*i)

# ------------------------------------------

# count even numbers

numbers = [10,15,20,25,30,35,40]

count = 0
for num in numbers:
  if num % 2 == 0:
    count += 1
print(count)

# ------------------------------------------

# reverse a number

num = 12345

reversed_num = 0

while num > 0:
  digit = num % 10
  reversed_num = reversed_num * 10 + digit
  num = num // 10
print(reversed_num)























