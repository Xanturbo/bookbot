def num_words(book_text):
    return len(book_text.split())

def char_count(book_text):
    char = {}
    book_text = book_text.lower() #convert to lowercase
    for c in book_text: #loop through each character
        if c.isalpha():
            if c in char:
                char[c] += 1 #increment count if character already exists
            else:
                char[c] = 1 #add new character with count 1
    return char

def sort_char_count(char_dict):
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)