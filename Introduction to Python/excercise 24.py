# Write a Python program to find the numbers of words present in the given sentence.

def sentence_num_words():
    user_string = input("Enter the sentence in which you want to find the number of words present in it: ")
    words = user_string.split()
    num_words = 0
    for i in words:
        if not i.isdigit():
            num_words += 1
        else:
            num_words += 0
    print("The number of words present in the string/sentence '",user_string,"' is : ",num_words)
    
sentence_num_words()
                