from multi_bracket_validation import multi_bracket_validation
import pytest


def test_multi_bracket_validation():
    assert multi_bracket_validation('sup()') is True
    assert multi_bracket_validation('sup)') is False
    assert multi_bracket_validation('sup(') is False


def test_multi_bracket_validation_input():
    with pytest.raises(TypeError):
        multi_bracket_validation(1)
