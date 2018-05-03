"""Whiteboard Challenge 31: Repeated Word"""
from hash_table import HashTable


def repeated_word(text):
    """
    Function returns the first repeated word.
    First thing it does is splits the inputted string
    into a list and for each word in that list it checks
    if that word is already in the hash table, if it isn't it adds
    word to the hash table. If it is it'll return that word and
    complete the problem domain. If it goes through the entire word list
    and there is no repeat words it'll return a informative output
    """
    if type(text) is not str:
        raise TypeError('Please Enter A String')

    words = text.split(' ')
    word_hasher = HashTable()
    for word in words:
        if word_hasher.get(word) == [word]:
            return word

        word_hasher.set(word, word)

    return 'There are no repeated words'
