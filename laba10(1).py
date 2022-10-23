with open('input.txt', 'r') as file:
   text = file.read()
words = text.split()
words = set(words)
words = sorted(words)
with open('output.txt', 'w') as file:
   for word in words:
       file.write(word + ' ')

