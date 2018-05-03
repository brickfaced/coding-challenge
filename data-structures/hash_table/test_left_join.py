from left_join import left_join as LJ
from hash_table import HashTable


def test_same_keys_on_both_hts():
    ramon = HashTable()
    ramon.set('sup', 'yo')
    mendoza = HashTable()
    mendoza.set('sup', 'cya')
    assert ramon.get('sup') == ['yo']
    LJ(ramon, mendoza)
    assert ramon.get('sup') == ['cya', 'yo']


def test_different_keys_on_both_hts():
    ramon = HashTable()
    ramon.set('sup', 'yo')
    mendoza = HashTable()
    mendoza.set('eat', 'vomit')
    assert ramon.get('sup') == ['yo']
    assert mendoza.get('eat') == ['vomit']
    LJ(ramon, mendoza)
    assert ramon.get('sup') == [None, 'yo']
    assert ramon.get('eat') == [None, 'vomit']
