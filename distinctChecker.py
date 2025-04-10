string = input("Enter a word ")
distinct_letters = set()
count =0
while True:
    if not string.isalpha():
        string= input("Please enter a valid string")
    else:
        for letter in string:
            if letter not in distinct_letters:
                print(letter)
                distinct_letters.add(letter)
                count = count +1
        print("There are", count, "distint letters in", string)
        break
