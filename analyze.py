# Analysis

import ch1text # Notice there is no .py

def count_syllables(words):
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count

    return count

def count_syllables_in_word(word):
    count = 0

    if len(word) <= 3:
        return 1

    vowels = 'aeiouAEIOU'
    for char in word:
        if char in vowels:
            count = count + 1
            
    return count

def count_sentences(text):
    count = 0

    terminals = '.;?!'
    for char in text:
         if char in terminals:
             count = count + 1
    return count

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)

    print(total_words, 'words')
    print(total_sentences, 'sentences')


compute_readability(ch1text.text)
