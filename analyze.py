# Analysis

import ch1text # Notice there is no .py

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_words = len(words)

    print(words)
    print(total_words, 'words')

compute_readability(ch1text.text)
