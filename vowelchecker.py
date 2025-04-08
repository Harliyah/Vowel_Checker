
vowels = ["a", "e", "i", "o", "u"]
count = 0
found = set()
while True:
    string = input("Enter a string ").lower()
    if not string.isalpha():
        print("Enter a valid string")
        continue
    else:
        for letter in string:
            if letter in vowels and letter not in found:
                print(letter)
                found.add(letter)
                count = count + 1
        if count == 0:
            print("There are no vowels in", string)
        elif count == 1:
            print("There is a single vowel in the word ", string)
        elif count > 1:
            print ("There are", count, "vowels in the word", string)
            break
