#solution

vowels = "a, e, i, o, u"

user_input = str(input("Enter a word: "))
count = 0
for user_input in vowels:
    if user_input in vowels:
        count += 1
    else:
        print("No vowels found")
print ("The nmber of vowels", count)
