numbers = [10,45,23,67,89,12,34,56,78,90]
largest = numbers[0]

for num in numbers:
  if num > largest:
    largest = num
print(largest)