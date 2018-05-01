"""Hash Table Testing Zone"""
from hash_table import HashTable as HT


def test_ht_set():
    """This tests to see that the inputted value gets put into a node
    as a dictionary"""
    ramon = HT()
    ramon._set('ramon', 1)
    assert type(ramon.buckets[ramon.hash_key('ramon')].head.val) is dict


def test_ht_get():
    """This tests to see that the value we input gets retrieved from the
    get method"""
    ramon = HT()
    ramon._set('ramon', 1)
    assert ramon.get('ramon') == 1
    ramon._set('mendoza', 2)
    assert ramon.get('mendoza') == 2


def test_ht_remove():
    ramon = HT()
    ramon._set('ramon', 1)
    assert ramon.get('ramon') == 1
    ramon.remove('ramon')
    assert ramon.get('ramon') == 'Key Not Found'
