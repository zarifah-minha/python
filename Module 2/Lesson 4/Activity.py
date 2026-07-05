word = input("Enter your word: ")
char = input("Enter your character: ")

i = 0
count = 0

while i < len(word):
    if word[i] == char:
        count = count + 1
    i = i + 1
print(f"Total occurance of {char} : {count}")
