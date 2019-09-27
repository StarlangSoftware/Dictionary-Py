class Syllable:

    """
    A constructor of Syllable class which takes a String as an input and initializes syllable variable with given input.

    PARAMETERS
    ----------
    syllable : str
        String input.
    """
    def __init__(self, syllable : str):
        self.syllable = syllable

    """
    Getter for the syllable variable.

    RETURNS
    -------
    str
        The syllable variable.
    """
    def getText(self) -> str:
        return self.syllable