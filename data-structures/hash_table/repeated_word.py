from hash_table import HashTable


def repeated_word(text):
    """Function returns the first repeated word"""
    words = text.split(' ')
    word_hasher = HashTable()
    for word in words:
        word_hasher.append(word)
