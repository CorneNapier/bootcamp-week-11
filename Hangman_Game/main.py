import random

def choose_word():
    #list of words used in the hangman game
    words = ['foxglove', 'luxury', 'syndrome', 'transcript', 'python', 'javascript', 'halo', 'sims', 'vaporize', 'jinx', 'voodoo', 'wellspring', 'html', 'coding', 'programming', 'sphinx', 'jukebox', 'puzzling']
    #returns a random word from the list above
    return random.choice(words)

#_ _ _ adds this to display in terminal, _ changes to a letter if the letter is found in the word selected.
def display_word(word, guessedLetters):
    #sets displayWord to an empty string
    displayedWord = ''
    #if the letter is stored guessedLetters then add letter to displayedWord.
    for letter in word:
        if letter in guessedLetters:
            displayedWord += letter
        #if the letter is not in guessedLetters, then add '_' to displayedWord
        else:
            displayedWord += '_'
    return displayedWord

def hangman():
    while True:
        #choose_word function is stored in a variable
        word = choose_word()
        #guessedLetters is an empty list, for letters to be inserted during game
        guessedLetters = []
        #the amount of attempts before game over
        attempts = 8
        
        #display a welcome message
        print("Welcome to Hangman!")
        #display the randomly selected word as ______ for no letters have yet to be guessed
        print(display_word(word, guessedLetters))
        
        while True:
            #gets user input
            guess = input("Guess a letter: ").lower()
            
            #if letter has been stored in guessedLetters then print the message
            if guess in guessedLetters:
                print("You've already guessed that letter!")
            #if guessed letter is in the word, add to the guessedLetter variable and print message
            elif guess in word:
                guessedLetters.append(guess)
                print('Great guess!')
            #if the above conditions are not true, then reduce the value stored in attempts by 1
            else:
                attempts -= 1
                print(f'Wrong guess! You have {attempts} attempts left.')
                #if the value in the attempts variable reaches 0 then print message and break the loop
                if attempts == 0:
                    print(f'Game over! The word was: {word}')
                    break
            #this allows the word to be displayed after each guess, with the correct letters found in the word, or no letters if the guess is incorrect
            print(display_word(word, guessedLetters))
            
            #if all the letters in the word has been guessed correctly then print message and break the loop
            if all(letter in guessedLetters for letter in word):
                print("Congratulations, you won!")
                break
        #sets the playAgain variable to an input, asking user if they wish to play again   
        playAgain = input('Would you like to play again? (yes/no)').lower()
        #if the user inputs no then break the loop, otherwise restart the loop
        if playAgain != 'yes':
            break
if __name__ == '__main__':
    hangman()