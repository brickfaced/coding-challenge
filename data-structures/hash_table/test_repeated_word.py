from repeated_word import repeated_word as RW
import pytest


def test_invalid_input():
    with pytest.raises(TypeError):
        assert RW(123) == 'Please Enter A String'


def test_text_with_no_repeated_words():
    assert RW('Yo Sup Wassup Que Pasa') == 'There are no repeated words'


def test_text_with_repeated_words():
    assert RW('Yo Wassup Yo') == 'Yo'
    assert RW('Wassup Yo Yo') == 'Yo'
    assert RW('Yo a b c d e f g h Yo') == 'Yo'
