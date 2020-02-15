from enum import Enum, auto


class Pos(Enum):
    """
    Parts of speech.
    """

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
