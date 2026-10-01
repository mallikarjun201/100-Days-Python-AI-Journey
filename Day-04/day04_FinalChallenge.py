numbers = [12,45,8,67,23,90,34,11,56]

total = 0
largest = numbers[0]
smallest = numbers[0]

even = 0

for num in numbers:
  total += num
  if num > largest:
    
    largest = num
  if num < smallest:
    smallest = num
  if num % 2 == 0:
    even += 1
    
print("Total:",total)
print("Largest number:" , largest)
print("smallest number:",smallest)
print("Even count:", even)
