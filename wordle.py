import os

def list_to_dict(wordbank):
    dict = {}
    for word in wordbank:
        dict[word] = 0
    return dict

def contains_letter(wordbank, letter):
    dict = {}
    for word in wordbank:
        if letter in word:
            dict[word] = 0
    return dict

def does_not_contain_letter(wordbank, letter):
    dict = {}
    for word in wordbank:
        if letter not in word:
            dict[word] = 0
    return dict

def letter_at_position(wordbank,letter,index):
    dict = {}
    for word in wordbank:
        if letter == word[index]:
            dict[word] = 0
    return dict

def letter_not_at_position(wordbank,letter,index):
    dict = {}
    for word in wordbank:
        if letter != word[index]:
            dict[word] = 0
    return dict

'''
Import New York Times' wordbank
'''
words = open("wordbank.txt","r") #opens text file for reading
wordbank = words.read() #stores contents of txt file in variable
wordbank = wordbank.split() #place words into a list.

wordbank = list_to_dict(wordbank)
os.system('clear')
for i in range(6):
    
    guess = input("Enter your guess:  ").lower()
    score = input(f"Enter the how {guess} scored (G - green, Y - yellow, X - gray):  ")
    for index, letter in enumerate(score.upper()):
        print(index,letter)
        if letter == "G":
            wordbank = letter_at_position(wordbank, guess[index], index)
            print(f'\nRound: {i}\nLetter: {letter}\nWords in wordbank: {len(wordbank)}')
        elif letter == "Y":
            wordbank = contains_letter(wordbank, guess[index])
            print(f'\nRound: {i}\nLetter: {letter}\nWords in wordbank: {len(wordbank)}')
            wordbank = letter_not_at_position(wordbank, guess[index], index)
            print(f'Round: {i}\nLetter: {letter}\nWords in wordbank: {len(wordbank)}')
        else:
            wordbank = does_not_contain_letter(wordbank, guess[index])
            print(f'\nRound: {i}\nLetter: {letter}\nWords in wordbank: {len(wordbank)}')

    os.system('clear')
    for word in wordbank:
        print(word)