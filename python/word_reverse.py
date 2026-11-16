#solution

word = input("Enter a word: ")

reversed_text = ""
for letter in word:
    reversed_text = letter + word
print("Reversed: ", reversed_text)