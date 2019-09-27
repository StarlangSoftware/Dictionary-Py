from enum import Enum, auto
"""
Parts of speech.
"""
class Pos(Enum):
    """
    Adjective.
    """
    ADJECTIVE = auto()
    """
    Noun.
    """
    NOUN = auto()
    """
    Verb.
    """
    VERB = auto()
    """
    Adverb.
    """
    ADVERB = auto()
    """
    Conjunction.
    """
    CONJUNCTION = auto()
    """
    Interjection.
    """
    INTERJECTION = auto()
    """
    Preposition.
    """
    PREPOSITION = auto()
    """
    Pronoun.
    """
    PRONOUN = auto()
