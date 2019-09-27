from Dictionary.Word import Word
from Dictionary.Pos import Pos

class ExceptionalWord(Word):

    """
    A constructor of ExceptionalWord class which takes a Pos as a  part of speech and two Strings; name
    and root as inputs. Then, calls its super class Word with given name and initialises root and pos variables
    with given inputs.

    PARAMETERS
    ----------
    name : str
        String input.
    root : str
        String input.
    pos : Pos
        Pos type input.
    """
    def __init__(self, name : str, root : str, pos : Pos):
        super().__init__(name)
        self.root = root
        self.pos = pos

    """
    Getter for the root variable.

    RETURNS
    -------
    str
        root variable.
    """
    def getRoot(self) -> str:
        return self.root

    """
    Getter for the pos variable.

    RETURNS
    -------
    Pos
        pos variable.
    """
    def getPos(self) -> Pos:
        return self.pos