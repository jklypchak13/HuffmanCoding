
import pytest
import sys
import os
sys.path.append(os.path.abspath('src'))

from huffman.character_counter import CharacterCounter


@pytest.fixture
def counter():
    return CharacterCounter()


def test_initializer(counter):
    """
    Tests the Initializer to an Empty Dictionary
    """
    assert counter.characters == {}


def test_add_text(counter):
    """
    Tests adding a single element of text.
    """
    counter = counter
    counter.add_text('hello world')
    assert counter.occurences('h') == 1
    assert counter.occurences('l') == 3


def test_add_multiple_text(counter):
    """
    Tests adding a single element of text.
    """
    counter = counter
    counter.add_text('hello world')
    assert counter.occurences('l') == 3

    counter.add_text('is this long text?')
    assert counter.occurences('l') == 4


def test_get_characters(counter):
    """
    Tests getting the characters.
    """
    expected = {
        'h': 1,
        'e': 1,
        'l': 4,
        'o': 3,
        ' ': 1,
        'w': 1,
        'r': 1,
        'd': 1,
        'n': 1,
        'g': 1,
    }
    counter = counter
    counter.add_text('hello world')
    counter.add_text('long')
    assert counter.get_characters() == expected


def test_occurences_present(counter):
    """
    Tests getting the characters.
    """
    expected = 4
    counter = counter
    counter.add_text('hello world')
    counter.add_text('long')
    assert counter.occurences('l') == expected


def test_occurences_not_present(counter):
    """
    Tests getting the characters.
    """
    expected = 0
    counter = counter
    counter.add_text('hello world')
    counter.add_text('long')
    assert counter.occurences('z') == expected
