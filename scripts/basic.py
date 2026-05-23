# li = [1,5, 6, 7]

# for x in li:
#     print(x)

# print("Hello, World!")

sentence = "the cat in the hat"
words = sentence.split()
print(words)
freq = {}
for word in words:
    print(freq.get(word))
    freq[word] = freq.get(word, 0) + 1
print(freq)
