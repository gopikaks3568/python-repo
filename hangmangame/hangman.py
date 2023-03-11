import hangman_words
import hangman_art
import random

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

guessletters = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print("*********************************************************")
    

    if guess in guessletters:
        print("Already guessed!!!, try another letter")
   
    guessletters.append(guess)
    print(guessletters)
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

   
    if guess not in chosen_word:
       
        print(f"{guess} not in the word")
        lives -= 1
        stages = hangman_art.stages
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
        
    print(f"{' '.join(display)}")

   
    if "_" not in display:
        end_of_game = True
        print("You win.")

 