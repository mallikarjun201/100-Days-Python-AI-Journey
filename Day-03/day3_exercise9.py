text = "python is a powerful programming language"

longest_word = ""
vowel_count = 0

for word in text.split():
  if len(word) > len(longest_word):
    longest_word = word

for char in text:
  if char in "aeiou":
    vowel_count += 1

print("Longest Word:", longest_word)
print("Number of Words:", len(text.split()))
print("Number of Vowels:", vowel_count)