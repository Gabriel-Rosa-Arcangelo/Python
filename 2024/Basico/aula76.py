secret_word = 'monkey'
user_word = '******'
tentativa = 0


while user_word != secret_word:
    
    letter = input('Type a letter: ')

    if letter.isnumeric():
        print('Letter is numeric please type a string')
        
    elif len(letter) > 1:
        print('Only 1 letter at a time')
        
    else:
            
        new_user_word = ''
        for i in range(len(secret_word)):
            if letter == secret_word[i]:
                new_user_word += letter
            else:
                new_user_word += user_word[i]
                
        user_word = new_user_word
        print(user_word)

        
        if letter not in secret_word:
            tentativa += 1

print('Congratulations! You guessed the word:', secret_word)
print('Number of attempts:', tentativa)     
        
    