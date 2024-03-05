import random

def random_number():
    rNum = random.randint(1, 10)
    return rNum

def game():
    while True:
        number = random_number()
        guessedNumbers = []
        attempts = 5
    
        print("\nI am thinking of a number between 1 and 10, can you guess what it is?")
        
        while True:
            guess = int(input("\nGuess a number: "))
            
            if guess > number:
                attempts -= 1
                print(f'The number {guess} is higher than the number I am thinking of.')
                print(f'You have {attempts} attempts left.')
                pass
            elif guess < number:
                attempts -= 1
                print(f'The number {guess} is lower than the number I am thinking of.')
                print(f'You have {attempts} attempts left.')
                pass
            elif guess == number:
                print('Correct! You win!!!!')
                break
            else:
                if attempts == 0:
                    print(f'Game over! The number was: {number}')
                    break
              
        playAgain = input('Would you like to play again? (yes/no)').lower()
        if playAgain != 'yes':
            break
        
if __name__ == '__main__':
   game()