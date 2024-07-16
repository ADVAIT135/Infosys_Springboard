""" Write a python function find_common_characters(msg1,msg2) to display all the common characters between given two strings.
    Return -1 if there are no matching characters.
    Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.
    Example: msg1="I like Python", msg2="Java is a very popular language" output=lieyon
"""
def find_common_characters(msg1, msg2):
    msg1 = msg1.replace(" ", "")
    msg2 = msg2.replace(" ", "")

    common_chars = set(msg1) & set(msg2)
    
    common_chars = ''.join(sorted(common_chars))
    
    if common_chars:
        return common_chars
    else:
        return -1

msg1 = "I like Python"
msg2 = "Java is a very popular language"
output = find_common_characters(msg1, msg2)
print(output) 
