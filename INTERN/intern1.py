import random
words = ["apple", "tiger", "clock", "house", "zebra"]
word = random.choice(words)
display = ["_"] * len(word)
tries = 6
guessed = []
print("Hangman Game! You have 6 tries.")
while tries > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    letter = input("Guess a letter: ").lower()
    if letter in guessed:
        print("Already guessed.")
        continue
    guessed.append(letter)
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
        print("Correct!")
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)
if "_" not in display:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:",word)
