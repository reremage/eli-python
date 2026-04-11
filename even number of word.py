word = input("Give word: ")
print("Original string, " + word)
for i in range(len(word)):
    if i % 2 == 0:
        print(word[i])
