import random
print("Hangman Game")
words =["banana", "car", "salt", "money", "race", "leave"]
randomWord = random.choice(words)
manhang= [
    """
    -----
    |
    |
    |
    |
    |
    -----
    """,
    """
    -----
    |   |
    |
    |
    |
    |
    -----
    """,
    """
    -----
    |   |
    |   0
    |
    |
    |
    -----
    """,
    """
    -----
    |   |
    |   0
    |   |
    |
    |
    -----
    """,
    """
    -----
    |   |
    |   0
    |  /|
    |   
    |
    -----
    """,
    """
    -----
    |   |
    |   0
    |  /|\\
    |   
    |
    -----
    """,
    """
    -----
    |   |
    |   0
    |  /|\\
    |  /
    |
    -----
    """,
    """
    -----
    |   |
    |   0
    |  /|\\
    |  / \\
    |
    -----
    """

]
def hangman():
    wrong_guesses = 0
    count = len(manhang) - 1
    dash = ['_' for _ in randomWord]
    print(dash)
    while wrong_guesses < count:
        print("\nWord is:",''.join(dash))
        guess = input("\nGuess a letter ").lower()
        if len(guess) != 1:
            print("Enter a single letter!")
            continue
        elif not guess.isalpha():
            print("Enter a valid letter") 
            continue
        if guess in randomWord:
            if guess in dash:
                print("Already guessed that one, Try again")
                continue
            else:
                for i in range(len(randomWord)):
                    if randomWord[i] == guess:
                        dash[i] = guess
                        print("Good guess!!")
                        print("You're on a roll")
        else:
            print("Wrong guess!!")
            print(manhang[wrong_guesses])
            print("You have" , {count - wrong_guesses}, "moves left")
            wrong_guesses = wrong_guesses + 1
        if wrong_guesses == count:
            print(manhang[wrong_guesses])
            print("Game Over!! The word was", randomWord)
        if '_' not in dash:
            print("You're right the word is: ", randomWord)
            break
hangman()

