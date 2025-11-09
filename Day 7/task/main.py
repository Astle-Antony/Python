import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

chosen_word = random.choice(word_list)
print(chosen_word)
guessing = ""

for _ in chosen_word:
    guessing +=  "_"
print(guessing)

hangman_live = 6
correct_letters = []
game_over = False

while not game_over:
    display = ''
    guess = input("Guess the letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    #  Logic to reduce the hangman life
    if guess not in chosen_word:
        hangman_live -= 1
        if hangman_live == 0:
            game_over = True
            print("You Lost")

    #  To check whether you've found the correct word
    if "_" not in display:
        game_over = True
        print("You won!")






