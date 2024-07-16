""" Write a Python function vowel_count(sentence) to return a dictionary with vowels, consonants, others as key
    and respective number of vowels, consonants, others characters as value.
    Note: Do case insensitive operations
    Example: sentence=“I love python and it so easy to learn”
    sample output={“vowels”:12,”consonants”:17, “others”:8}
"""

def vowel_count(sentence):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    counts = {"vowels": 0, "consonants": 0, "others": 0}
    
    for char in sentence.lower():
        if char in vowels:
            counts["vowels"] += 1
        elif char in consonants:
            counts["consonants"] += 1
        else:
            counts["others"] += 1
    
    print(counts)

vowel_count("I love python and it so easy to learn")