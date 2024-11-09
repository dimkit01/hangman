import random

list_of_words = ['main', 'hurt', 'truth', 'deliver', 'killer', 'elephant', 'python']

chosen_word = random.choice(list_of_words)

used_letters = []
attempts = 0
max_attempts = 6

hangman_stages = [
    '''
     -----
     |   |
         |
         |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\  |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    ''',
]

display_world = ""
for letter in chosen_word:
    display_world += "_"

while True:
    print(hangman_stages[attempts])
    print(f"Word {display_world}")
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        if guess in used_letters:
            print(f"You already guessed {guess}")
            print(f"Word {display_world}")
            continue
        else:
            print(f"Correct! You guessed {guess}!")
            used_letters.append(guess)
            display_world_list = list(display_world)
            index = 0
            loose_point = 0
            for letter in chosen_word:
                if letter == guess:
                    display_world_list[index] = f"{guess}"
                if display_world_list[index] == "_":
                    loose_point += 1
                index += 1

            new_display_world = "".join(display_world_list)
            display_world = new_display_world
            print(f"Word {new_display_world}")
            if loose_point == 0:
                print("You win! You already guessed the word!")
                break
    else:
        print(f"Wrong, the world don't have {guess}!")
        print(f"Word {display_world}")
        used_letters.append(guess)
        attempts += 1
        if attempts == max_attempts:
            print(hangman_stages[attempts])
            print(f"You loosed. You have {max_attempts} attempts left.")
            print(f"The word is {chosen_word}")
            break