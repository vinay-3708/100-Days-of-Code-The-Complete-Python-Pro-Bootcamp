import random
import Hangman_data


chosen_word = random.choice(Hangman_data.word_list)
print(f"Chosen word is: {chosen_word}")

display = list("_"*len(chosen_word))
print(display)

end_game = False
lives = 6
while lives > 0 and not end_game:
    if '_' in display:
        guess = input('Guess a letter: ').lower()
        if guess in chosen_word:
            for letter_in_word in range(len(chosen_word)):
                if guess == chosen_word[letter_in_word]:
                    display[letter_in_word] = guess
            print(display)
        else:
            print(Hangman_data.hangman_pics[6-lives])
            lives -= 1
            if lives == 0:
                print("You lost all lives & You lose the game.")
            else:
                print(f"Nah!, You lost one life, You have {lives} more.")
    else:
        print(f"Yeah, The chosen word is {chosen_word}, You win !")
        end_game = True