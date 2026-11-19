#solution

user_input = input("Enter a sentence: ")
count = 0
word_count = ""
for word in user_input:
    count += 1
    word_count = word.split(word)
print("Number of words: ", count)