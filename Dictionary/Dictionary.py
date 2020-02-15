from bisect import bisect_left
from Dictionary.Word import Word


class Dictionary:

    words: list
    filename: str

    def __init__(self):
        """
        An empty constructor of Dictionary class.
        """
        self.words = []
        self.filename = ""

    def getWord(self, name: str) -> Word:
        """
        The getWord method takes a String name as an input and performs binary search within words list and assigns the
        result to integer variable middle. If the middle is greater than 0, it returns the item at index middle of words
        list, None otherwise.

        PARAMETERS
        ----------
        name : str
            String input.

        RETURNS
        -------
        Word
            the item at found index of words {@link ArrayList}, null if cannot be found.
        """
        word = Word(name)
        middle = bisect_left(self.words, word)
        if self.words[middle] == word:
            return self.words[middle]
        return None

    def getWordIndex(self, name: str) -> int:
        """
        The getWordIndex method takes a String name as an input and performs binary search within words list and assigns
        the result to integer variable middle. If the middle is greater than 0, it returns the index middle, -1
        otherwise.

        PARAMETERS
        ----------
        name : str
            String input.

        RETURNS
        -------
        int
            found index of words list, -1 if cannot be found.
        """
        word = Word(name)
        middle = bisect_left(self.words, word)
        if self.words[middle] == word:
            return middle
        return -1

    def removeWord(self, name: str):
        """
        RemoveWord removes a word with the given name

        PARAMETERS
        ----------
        name : str
            Name of the word to be removed.
        """
        index = self.getWordIndex(name)
        if index != -1:
            self.words.pop(index)

    def size(self) -> int:
        """
        The size method returns the size of the words list.

        RETURNS
        -------
        int
            The size of the words list.
        """
        return len(self.words)

    def getWordWithIndex(self, index: int) -> Word:
        """
        The getWordWithIndex method which takes an index as an input and returns the value at given index of words list.

        PARAMETERS
        ----------
        index : int
            index to get the value.

        RETURNS
        -------
        Word
            The value at given index of words list.
        """
        return self.words[index]

    def longestWordSize(self) -> int:
        """
        The longestWordSize method loops through the words list and returns the item with the maximum word length.

        RETURNS
        -------
        int
            The item with the maximum word length.
        """
        maxLength = 0
        for word in self.words:
            if len(word) > maxLength:
                maxLength = len(word)
        return maxLength

    def getWordStartingWith(self, _hash: str) -> int:
        """
        The getWordStartingWith method takes a String hash as an input and performs binary search within words list and
        assigns the result to integer variable middle. If the middle is greater than 0, it returns the index middle,
        -middle-1 otherwise.

        PARAMETERS
        ----------
        _hash : str
            String input.

        RETURNS
        -------
        int
            Found index of words list, -middle-1 if cannot be found.
        """
        word = Word(_hash)
        middle = bisect_left(self.words, word)
        if self.words[middle] == word:
            return middle
        else:
            return -middle - 1
