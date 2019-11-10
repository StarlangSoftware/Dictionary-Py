from bisect import bisect_left
from Dictionary.Trie.Trie import Trie
from Dictionary.Dictionary import Dictionary
from Dictionary.TxtWord import TxtWord


class TxtDictionary(Dictionary):

    __misspelledWords: dict

    """
    Constructor of TxtDictionary class which takes a String filename as input. And calls its super class
    Dictionary, assigns given filename input to the filename variable. Then, it calls loadFromText method with given
    filename.

    PARAMETERS
    ----------
    filename : str
        String input.
    """
    def __init__(self, fileName=None, misspelledFileName=None):
        super().__init__()
        if fileName is None:
            fileName = "resources/turkish_dictionary.txt"
        self.filename = fileName
        self.loadFromText(self.filename)
        self.__misspelledWords = {}
        if misspelledFileName is not None:
            self.loadMisspelledWords(misspelledFileName)

    """
    The addNumber method takes a String name and calls addWithFlag method with given name and IS_SAYI flag.

    PARAMETERS
    ----------
    name : str
        String input.
    """
    def addNumber(self, name : str):
        self.addWithFlag(name, "IS_SAYI")

    """
    The addRealNumber method takes a String name and calls addWithFlag method with given name and IS_REELSAYI flag.

    PARAMETERS
    ----------
    name : str
        String input.
    """
    def addRealNumber(self, name : str):
        self.addWithFlag(name, "IS_REELSAYI")

    """
    The addFraction method takes a String name and calls addWithFlag method with given name and IS_KESIR flag.

    PARAMETERS
    ----------
    name : str
        String input.
    """
    def addFraction(self, name: str):
        self.addWithFlag(name, "IS_KESIR")

    """
    The addTime method takes a String name and calls addWithFlag method with given name and IS_ZAMAN flag.

    PARAMETERS
    ----------
    name : str
        String input.
    """
    def addTime(self, name : str):
        self.addWithFlag(name, "IS_ZAMAN")

    """
    The addProperNoun method takes a String name and calls addWithFlag method with given name and IS_OA flag.

    PARAMETERS
    ----------
    name : str
        String input.

    RETURNS
    -------
    bool
        true if given name is in words list, false otherwise.
    """
    def addProperNoun(self, name : str)-> bool:
        return self.addWithFlag(name, "IS_OA")

    """
    The addNoun method takes a String name and calls addWithFlag method with given name and CL_ISIM flag.

    PARAMETERS
    ----------
    name : str
        String input.

    RETURNS
    -------
    bool
        true if given name is in words list, false otherwise.
    """
    def addNoun(self, name : str)-> bool:
        return self.addWithFlag(name, "CL_ISIM")

    """
    The addVerb method takes a String name and calls addWithFlag method with given name and CL_FIIL flag.

    PARAMETERS
    ----------
    name : str
        String input.

    RETURNS
    -------
    bool
        true if given name is in words list, false otherwise.
    """
    def addVerb(self, name: str)-> bool:
        return self.addWithFlag(name, "CL_FIIL")

    """
    The addAdjective method takes a String name and calls addWithFlag method with given name and IS_ADJ flag.

    PARAMETERS
    ----------
    name : str
        String input.

    RETURNS
    -------
    bool
        true if given name is in words list, false otherwise.
    """
    def addAdjective(self, name: str)-> bool:
        return self.addWithFlag(name, "IS_ADJ")

    """
    The addAdverb method takes a String name and calls addWithFlag method with given name and IS_ADVERB flag.

    PARAMETERS
    ----------
    name : str
        String input.

    RETURNS
    -------
    bool
        true if given name is in words list, false otherwise.
    """
    def addAdverb(self, name : str)-> bool:
        return self.addWithFlag(name, "IS_ADVERB")

    """
    The addPronoun method takes a String name and calls addWithFlag method with given name and IS_ZM flag.

    PARAMETERS
    ----------
    name : str
        String input.

    RETURNS
    -------
    bool
        true if given name is in words list, false otherwise.
    """
    def addPronoun(self, name: str)-> bool:
        return self.addWithFlag(name, "IS_ZM")

    """
    The addWithFlag method takes a String name and a flag as inputs. First it creates a TxtWord word, then if
    given name is not in words list it creates new TxtWord with given name and assigns it to
    the word and adds given flag to the word, it also add newly created word to the words list's index
    found by performing a binary search and return true at the end. If given name is in words list,
    it adds it the given flag to the word.

    PARAMETERS
    ----------
    name : str
        String input.
    flag : str
        String flag.
        
    RETURNS
    -------
    bool
        true if given name is in words list, false otherwise.
    """
    def addWithFlag(self, name: str, flag: str)-> bool:
        if self.getWord(name.lower()) is None:
            word = TxtWord(name.lower())
            word.addFlag(flag)
            middle = bisect_left(self.words, word)
            self.words.insert(middle, word)
            return True
        else:
            word = self.getWord(name.lower())
            if not word.containsFlag(flag):
                word.addFlag(flag)
        return False

    """
    The mergeDictionary method takes a String inputs; secondFileName and mergedFileName. It reads given files line by
    line and splits them according to spaces and write each word to file whichever comes first lexicographically and
    continue to read files till the end.

    PARAMETERS
    ----------
    secondFileName : str
        String input.
    mergedFileName : str
        String input.
    """
    def mergeDictionary(self, secondFileName : str, mergedFileName : str):
        firstFile = open(self.filename, "r")
        secondFile = open(secondFileName, "r")
        outFile = open(mergedFileName)
        firstLines = firstFile.readlines()
        firstFile.close()
        secondLines = secondFile.readlines()
        secondFile.close()
        i = 0
        j = 0
        while i < len(firstLines) and j < len(secondLines):
            st1 = firstLines[i]
            st2 = secondLines[j]
            word1 = st1.split()[0]
            word2 = st2.split()[0]
            if word1 < word2:
                print(st1, file=outFile)
                i = i + 1
            else:
                if word1 > word2:
                    print(st2, file=outFile)
                    j = j + 1
                else:
                    flag = st2.split()[1]
                    if flag in st1:
                        print(st1, file=outFile)
                    else:
                        print(st1 + " " + flag, file=outFile)
                    i = i + 1
                    j = j + 1
        while i < len(firstLines):
            st1 = firstLines[j]
            print(st1, file=outFile)
            i = i + 1
        while j < len(secondLines):
            st2 = secondLines[j]
            print(st2, file=outFile)
            j = j + 1
        outFile.close()

    """
    The loadFromText method takes a String filename as an input. It reads given file line by line and splits according 
    to space and assigns each word to the String array. Then, adds these word with their flags to the words list.
    At the end it sorts the words list.

    PARAMETERS
    ----------
    fileName : str
        File name input.
    """
    def loadFromText(self, fileName: str):
        input = open(fileName, "r")
        lines = input.readlines()
        for line in lines:
            list = line.split()
            if len(list) > 0:
                currentWord = TxtWord(list[0])
                for i in range(1, len(list)):
                    currentWord.addFlag(list[i])
                self.words.append(currentWord)
        self.words.sort()

    """
    The loadMisspellWords method takes a String filename as an input. It reads given file line by line and splits
    according to space and assigns each word with its misspelled form to the the misspelledWords hashMap.

    PARAMETERS
    ----------
    fileName : str
        File name input.
    """
    def loadMisspelledWords(self, fileName: str):
        input = open(fileName, "r")
        lines = input.readlines()
        for line in lines:
            list = line.split()
            if len(list) == 2:
                self.__misspelledWords[list[0]] = list[1]

    """
    The getCorrectForm returns the correct form of a misspelled word.

    PARAMETERS
    ----------
    misspelledWord : str
        Misspelled form.
        
    RETURNS
    -------
    str
        Correct form.
    """
    def getCorrectForm(self, misspelledWord: str) -> str:
        if misspelledWord in self.__misspelledWords:
            return self.__misspelledWords[misspelledWord]
        return ""

    """
    The saveAsTxt method takes a filename as an input and prints out the items of words list.

    PARAMETERS
    ----------
    filename : str
        String input.
    """
    def saveAsTxt(self, fileName: str):
        output = open(fileName, "w")
        for word in self.words:
            print(word, file=output)
        output.close()

    """
    The addWordWhenRootSoften is used to add word to Trie whose last consonant will be soften.
    For instance, in the case of Dative Case Suffix, the word is 'müzik' when '-e' is added to the word, the last
    char is drooped and root became 'müzi' and by changing 'k' into 'ğ' the word transformed into 'müziğe' as in the
    example of 'Herkes müziğe doğru geldi'.

    In the case of accusative, possessive of third person and a derivative suffix, the word is 'kanat' when '-i' is
    added to word, last char is dropped, root became 'kana' then 't' transformed into 'd' and added to Trie. The word is
    changed into 'kanadı' as in the case of 'Kuşun kırık kanadı'.

    PARAMETERS
    ----------
    trie : Trie
        the name of the Trie to add the word.
    last : chr
        the last char of the word to be soften.
    root : str
        the substring of the word whose last one or two chars are omitted from the word to bo softed.
    word : TxtWord
        the original word.
    """
    def addWordWhenRootSoften(self, trie: Trie, last: chr, root : str, word : TxtWord):
        if last == 'p':
            trie.addWord(root + 'b', word)
        elif last == 'ç':
            trie.addWord(root + 'c', word)
        elif last == 't':
            trie.addWord(root + 'd', word)
        elif last == 'k' or last == 'g':
            trie.addWord(root + 'ğ', word)
        else:
            pass

    """
    The prepareTrie method is used to create a Trie with the given dictionary. First, it gets the word from dictionary,
    then checks some exceptions like 'ben' which does not fit in the consonant softening rule and transforms into 'bana',
    and later on it generates a root by removing the last char from the word however if the length of the word is greater
    than 1, it also generates the root by removing the last two chars from the word.

    Then, it gets the last char of the root and adds root and word to the result Trie. There are also special cases 
    such as;
    lastIdropsDuringSuffixation condition, if it is true then addWordWhenRootSoften method will be used rather than 
    addWord.
    Ex : metin + i = metni
    isPortmanteauEndingWithSI condition, if it is true then addWord method with rootWithoutLastTwo will be used.
    Ex : ademelması + lar = ademelmaları
    isPortmanteau condition, if it is true then addWord method with rootWithoutLast will be used.
    Ex : mısıryağı + lar = mısıryağları
    vowelEChangesToIDuringYSuffixation condition, if it is then addWord method with rootWithoutLast will be used
    depending on the last char whether it is 'e' or 'a'.
    Ex : ye + iniz - yiyiniz
    endingKChangesIntoG condition, if it is true then addWord method with rootWithoutLast will be used with added 'g'.
    Ex : ahenk + i = ahengi

    RETURNS
    -------
    Trie
        the resulting Trie.
    """
    def prepareTrie(self) -> Trie:
        result = Trie()
        lastBefore = ' '
        for i in range(self.size()):
            word = self.getWordWithIndex(i)
            root = word.getName()
            length = len(root)
            if root == "ben":
                result.addWord("bana", word)
            rootWithoutLast = root[0:length - 1]
            if length > 1:
                rootWithoutLastTwo = root[0:length - 2]
            else:
                rootWithoutLastTwo = ""
            if length > 1:
                lastBefore = root[length - 2]
            last = root[length - 1]
            result.addWord(root, word)
            if word.lastIdropsDuringSuffixation() or word.lastIdropsDuringPassiveSuffixation():
                if word.rootSoftenDuringSuffixation():
                    self.addWordWhenRootSoften(result, last, rootWithoutLastTwo, word)
                else:
                    result.addWord(rootWithoutLastTwo + last, word)
            if word.isPortmanteauEndingWithSI():
                result.addWord(rootWithoutLastTwo, word)
            if word.rootSoftenDuringSuffixation():
                self.addWordWhenRootSoften(result, last, rootWithoutLast, word)
            if word.isPortmanteau():
                if word.isPortmanteauFacedVowelEllipsis():
                    result.addWord(rootWithoutLastTwo + last + lastBefore, word)
                else:
                    if word.isPortmanteauFacedSoftening():
                        if lastBefore == 'b':
                            result.addWord(rootWithoutLastTwo + 'p', word)
                        elif lastBefore == 'c':
                            result.addWord(rootWithoutLastTwo + 'ç', word)
                        elif lastBefore == 'd':
                            result.addWord(rootWithoutLastTwo + 't', word)
                        elif lastBefore == 'ğ':
                            result.addWord(rootWithoutLastTwo + 'k', word)
                        else:
                            pass
                    else:
                        result.addWord(rootWithoutLast, word)
            if word.vowelEChangesToIDuringYSuffixation() or word.vowelAChangesToIDuringYSuffixation():
                if last == 'e':
                    result.addWord(rootWithoutLast, word)
                elif last == 'a':
                    result.addWord(rootWithoutLast, word)
                else:
                    pass
            if word.endingKChangesIntoG():
                result.addWord(rootWithoutLast + 'g', word)
        return result