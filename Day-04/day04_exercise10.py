numbers = [12,43, 56, 78, 90, 121, 123, 145, 167, 189]
smallest = numbers[0]

for num in numbers:
  if num < smallest:
    smallest = num 
print(smallest)