import random
def select_random_word():
    words = ["python", "programming", "hangman", "challenge", "development"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return displayed_word

def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    print("Welcome to the Hangman Game!")
    print("Guess the word:")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess!  You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            print("Thank you for playing the Hangman Game")
            print("Designed by ADARSHA JASH")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was: {word}")
        print("Thank you for playing the Hangman Game")
        print("Designed by ADARSHA JASH")
if __name__ == "__main__":
    hangman()