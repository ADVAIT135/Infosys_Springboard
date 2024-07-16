""" Write a Python function words_count(sentence) to return a dictionary with the length of words as key and number words with such length as value.
    Example: sentence=“I love python and it so easy to learn” sample output={1:1,4:2,6:1,3:1,2:4,5:1}
"""
def words_count(sentence):
    words = sentence.split()
    length_count = {}
    
    for word in words:
        length = len(word)
        if length in length_count:
            length_count[length] += 1
        else:
            length_count[length] = 1
    
    print(length_count)
    
words_count("I love python and it is so easy to learn")


    