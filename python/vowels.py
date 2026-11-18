#solution

vowels = "a, e, i, o, u"

user_input = input("Enter a word: ")
count = 0
for letter in vowels:
    if letter in user_input:
        count += 1  
print ("The number of vowels: ", count)
    