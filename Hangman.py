import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


from hangman_words import word_list

chosen_word = random.choice(word_list)
# print(chosen_word)

life = 6
end_game = False

# creating blanks
display = []
for _ in range(len(chosen_word)):
    display += "_"
# print(display)


while not end_game:
    guess = (input("Guess a letter = ")).lower()
    # print(guess)

    if guess in display:
        print(f"you have already guessed {guess}")

    # checking guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # print(display)

    if guess not in chosen_word:
        life -= 1
        if life == 0:
            end_game = True
            print("You Lose!!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You Win!!")

    print(stages[life])
