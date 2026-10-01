text = "Python programming is very interesting"
longest_word =""

for word in text.split():
  if len(word) > len(longest_word):
    longest_word = word

print(longest_word)
