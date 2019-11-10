from Dictionary.Word import Word
from Math.Vector import Vector


class VectorizedWord(Word):

    __vector: Vector

    """
    A constructor of VectorizedWord class which takes a String and a Vector as inputs and calls its
    super class Word with name and also initializes vector variable with given input.

    PARAMETERS
    ----------
    name : str
        String input.
    vector : Vector
        Vector type input.
    """
    def __init__(self, name: str, vector: Vector):
        super().__init__(name)
        self.__vector = vector

    """
    Getter for the vector variable.

    RETURNS
    -------
    Vector
        the vector variable.
    """
    def getVector(self) -> Vector:
        return self.__vector
