import unittest
from collections import Counter

from .data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""

    with open(DICTIONARY) as f:
        lines = f.readlines()

    return [x.strip() for x in lines]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    values = [ LETTER_SCORES[x] if x in LETTER_SCORES else 0 for x in word.upper()]
    return sum(values)


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()

    return max(words, key=lambda x: calc_word_value(x))






