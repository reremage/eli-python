word = input("Give a word: ")
n = int(input("where do you wanna delete "))

def remove_chars(word, n):
    print(word[n:])
    
remove_chars(word, n)
