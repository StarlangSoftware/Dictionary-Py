from Dictionary.Word import Word


class Dictionary:

    words: list
    filename: str

    def __init__(self, comparator=None):
        """
        An empty constructor of Dictionary class.
        """
        self.words = []
        self.filename = ""
        if comparator is None:
            self.comparator = Dictionary.turkishLowerCaseComparator
        else:
            self.comparator = comparator

    @staticmethod
    def turkishLowerCaseComparator(wordA: Word, wordB: Word):
        LOWERCASE_LETTERS = "abcçdefgğhıijklmnoöprsştuüvyz"
        for i in range(min(len(wordA.getName()), len(wordB.getName()))):
            firstChar = wordA.getName()[i:i + 1]
            secondChar = wordB.getName()[i:i + 1]
            if firstChar != secondChar:
                if firstChar in LOWERCASE_LETTERS and secondChar not in LOWERCASE_LETTERS:
                    return -1
                elif firstChar not in LOWERCASE_LETTERS and secondChar in LOWERCASE_LETTERS:
                    return 1
                elif firstChar in LOWERCASE_LETTERS and secondChar in LOWERCASE_LETTERS:
                    first = LOWERCASE_LETTERS.index(firstChar)
                    second = LOWERCASE_LETTERS.index(secondChar)
                    if first < second:
                        return -1
                    elif first > second:
                        return 1
        if len(wordA.getName()) < len(wordB.getName()):
            return -1
        elif len(wordA.getName()) > len(wordB.getName()):
            return 1
        else:
            return 0

    @staticmethod
    def turkishIgnoreCaseComparator(wordA: Word, wordB: Word):
        IGNORE_CASE_LETTERS = "aAbBcCçÇdDeEfFgGğĞhHıIiİjJkKlLmMnNoOöÖpPrRsSşŞtTuUüÜvVyYzZ"
        for i in range(min(len(wordA.getName()), len(wordB.getName()))):
            firstChar = wordA.getName()[i:i + 1]
            secondChar = wordB.getName()[i:i + 1]
            if firstChar != secondChar:
                if firstChar in IGNORE_CASE_LETTERS and secondChar not in IGNORE_CASE_LETTERS:
                    return -1
                elif firstChar not in IGNORE_CASE_LETTERS and secondChar in IGNORE_CASE_LETTERS:
                    return 1
                elif firstChar in IGNORE_CASE_LETTERS and secondChar in IGNORE_CASE_LETTERS:
                    first = IGNORE_CASE_LETTERS.index(firstChar)
                    second = IGNORE_CASE_LETTERS.index(secondChar)
                    if first < second:
                        return -1
                    elif first > second:
                        return 1
        if len(wordA.getName()) < len(wordB.getName()):
            return -1
        elif len(wordA.getName()) > len(wordB.getName()):
            return 1
        else:
            return 0

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
        middle = self.__getPosition(word)
        if middle >= 0:
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
        middle = self.__getPosition(word)
        if middle >= 0:
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
            if len(word.getName()) > maxLength:
                maxLength = len(word.getName())
        return maxLength

    def __getPosition(self, word: Word) -> int:
        lo = 0
        hi = len(self.words) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.comparator(self.words[mid], word) < 0:
                lo = mid + 1
            elif self.comparator(self.words[mid], word) > 0:
                hi = mid - 1
            else:
                return mid
        return -lo

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
        middle = self.__getPosition(word)
        if middle < 0:
            return -middle
        else:
            return middle
