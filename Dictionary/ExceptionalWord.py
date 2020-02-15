from Dictionary.Word import Word
from Dictionary.Pos import Pos


class ExceptionalWord(Word):

    __root: str
    __pos: Pos

    def __init__(self, name: str, root: str, pos: Pos):
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
        super().__init__(name)
        self.__root = root
        self.__pos = pos

    def getRoot(self) -> str:
        """
        Getter for the root variable.

        RETURNS
        -------
        str
            root variable.
        """
        return self.__root

    def getPos(self) -> Pos:
        """
        Getter for the pos variable.

        RETURNS
        -------
        Pos
            pos variable.
        """
        return self.__pos
