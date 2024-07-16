# Bilingual (English-Swedish) dictionary
bilingual_dict = {
    "merry": "god",
    "christmas": "jul",
    "and": "och",
    "happy": "gott",
    "new": "nytt",
    "year": "år" 
}

def translate(b_dict, list_words):
    translated_words = [b_dict.get(word.lower(), word) for word in list_words]
    return translated_words

# Example usage:
english_wish = ["Merry", "Christmas", "and", "Happy", "New", "Year"]
swedish_wish = translate(bilingual_dict, english_wish)
print(swedish_wish)
