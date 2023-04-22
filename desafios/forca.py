import random

with open('gpt/palavras.txt','r',encoding='utf-8') as file:
    words = file.read().split()
    
selected_word = random.choice(words).lower()
secret_word = list(selected_word)
chances = 6
guessed_letters = []
current_word = ['_'] * len(secret_word)

game_over = False
while game_over:
    print('\nLives','\u2764  ' * chances)
    print(' '.join(current_word))
    letter = input('\nGuess a letter: ')

    if not letter.isalpha() or len(letter) != 1:
        print('Please enter a single letter.')
        continue

    if letter in guessed_letters:
        print('You already guessed that letter.')
        continue

    guessed_letters.append(letter)

    if letter.lower() in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                current_word[i] = letter
                
        if '_' not in current_word:
            print('You won!')
            game_over = True

    else:
        chances -= 1
        if chances == 0:
            print(f'\nThe correct word was: {selected_word}')
            game_over = True
    
    
    