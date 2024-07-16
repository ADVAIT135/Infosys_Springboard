""" Write a python function, encrypt_sentence(msg) which accepts a message and encrypts it based on rules given below
    and returns the encrypted message.
    
    Words at odd position -> Reverse It
    Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change
    Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
          Perform case sensitive string operations wherever necessary.

    Example: msg=the sun rises in the east    output=eht snu sesir ni eht stea
"""

def encrypt_sentence(msg):
    def is_vowel(char):
        return char.lower() in 'aeiou'

    def rearrange_word(word):
        consonants = ''.join([char for char in word if not is_vowel(char)])
        vowels = ''.join([char for char in word if is_vowel(char)])
        return consonants + vowels

    words = msg.split()
    encrypted_words = []

    for i, word in enumerate(words):
        if (i + 1) % 2 == 1:  # Odd position
            encrypted_words.append(word[::-1])
        else:  # Even position
            encrypted_words.append(rearrange_word(word))

    print(' '.join(encrypted_words))

encrypt_sentence('The sun rises in the east')
encrypt_sentence('The sun sets in the west')
encrypt_sentence('I am a Python Developer')
