import random

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

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(int((word_length)))


display = []
for _ in range(word_length):
    display += "_"

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for i in range(word_length):
        letter = chosen_word[i]

        # print(f"Current position: {position}\n current letter: {letter}\n Guessed letter: {guess} ")
        if guess == letter:
            display[i] = letter
    if guess not in  chosen_word:
        print(f"You guessed {guess},that's not in the word.  ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")

    # print("you lose")

    # print(f"{''.join(display)}")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("you win")




