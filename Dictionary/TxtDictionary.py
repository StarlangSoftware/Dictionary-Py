from bisect import bisect_left
from functools import cmp_to_key

import pkg_resources

from Dictionary.Trie.Trie import Trie
from Dictionary.Dictionary import Dictionary
from Dictionary.TxtWord import TxtWord


class TxtDictionary(Dictionary):

    __misspelled_words: dict

    def __init__(self,
                 fileName=None,
                 misspelledFileName=None,
                 comparator=None,
                 morphologicalLexicon=None):
        """
        Constructor of TxtDictionary class which takes a String filename as input. And calls its super class
        Dictionary, assigns given filename input to the filename variable. Then, it calls loadFromText method with given
        filename.

        PARAMETERS
        ----------
        fileName : str
            String input.
        """
        super().__init__(comparator)
        self.__misspelled_words = {}
        if fileName is None:
            fileName = pkg_resources.resource_filename(__name__, 'data/turkish_dictionary.txt')
            self.__loadMisspelledWords(pkg_resources.resource_filename(__name__, 'data/turkish_misspellings.txt'))
        self.filename = fileName
        self.__loadFromText(self.filename)
        if fileName is None or morphologicalLexicon is None:
            self.__loadMorphologicalLexicon(pkg_resources.resource_filename(__name__, 'data/turkish_morphological_lexicon.txt'))
        if misspelledFileName is not None:
            self.__loadMisspelledWords(misspelledFileName)

    def addNumber(self, name: str):
        """
        The addNumber method takes a String name and calls addWithFlag method with given name and IS_SAYI flag.

        PARAMETERS
        ----------
        name : str
            String input.
        """
        self.addWithFlag(name, "IS_SAYI")

    def addRealNumber(self, name: str):
        """
        The addRealNumber method takes a String name and calls addWithFlag method with given name and IS_REELSAYI flag.

        PARAMETERS
        ----------
        name : str
            String input.
        """
        self.addWithFlag(name, "IS_REELSAYI")

    def addFraction(self, name: str):
        """
        The addFraction method takes a String name and calls addWithFlag method with given name and IS_KESIR flag.

        PARAMETERS
        ----------
        name : str
            String input.
        """
        self.addWithFlag(name, "IS_KESIR")

    def addTime(self, name: str):
        """
        The addTime method takes a String name and calls addWithFlag method with given name and IS_ZAMAN flag.

        PARAMETERS
        ----------
        name : str
            String input.
        """
        self.addWithFlag(name, "IS_ZAMAN")

    def addProperNoun(self, name: str) -> bool:
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
        return self.addWithFlag(name, "IS_OA")

    def addNoun(self, name: str) -> bool:
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
        return self.addWithFlag(name, "CL_ISIM")

    def addVerb(self, name: str) -> bool:
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
        return self.addWithFlag(name, "CL_FIIL")

    def addAdjective(self, name: str) -> bool:
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
        return self.addWithFlag(name, "IS_ADJ")

    def addAdverb(self, name: str) -> bool:
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
        return self.addWithFlag(name, "IS_ADVERB")

    def addPronoun(self, name: str) -> bool:
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
        return self.addWithFlag(name, "IS_ZM")

    def addWithFlag(self,
                    name: str,
                    flag: str) -> bool:
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
        if self.getWord(name.lower()) is None:
            word = TxtWord(name.lower())
            word.addFlag(flag)
            middle = bisect_left(self.words, word)
            self.words.insert(middle, word)
            return True
        else:
            word = self.getWord(name.lower())
            if isinstance(word, TxtWord) and not word.containsFlag(flag):
                word.addFlag(flag)
        return False

    def mergeDictionary(self,
                        secondFileName: str,
                        mergedFileName: str):
        """
        The mergeDictionary method takes a String inputs; secondFileName and mergedFileName. It reads given files line
        by line and splits them according to spaces and write each word to file whichever comes first lexicographically
        and continue to read files till the end.

        PARAMETERS
        ----------
        secondFileName : str
            String input.
        mergedFileName : str
            String input.
        """
        first_file = open(self.filename, "r", encoding="utf8")
        second_file = open(secondFileName, "r", encoding="utf8")
        out_file = open(mergedFileName, "w", encoding="utf8")
        first_lines = first_file.readlines()
        first_file.close()
        second_lines = second_file.readlines()
        second_file.close()
        i = 0
        j = 0
        while i < len(first_lines) and j < len(second_lines):
            st1 = first_lines[i]
            st2 = second_lines[j]
            word1 = st1.split()[0]
            word2 = st2.split()[0]
            if word1 < word2:
                print(st1, file=out_file)
                i = i + 1
            else:
                if word1 > word2:
                    print(st2, file=out_file)
                    j = j + 1
                else:
                    flag = st2.split()[1]
                    if flag in st1:
                        print(st1, file=out_file)
                    else:
                        print(st1 + " " + flag, file=out_file)
                    i = i + 1
                    j = j + 1
        while i < len(first_lines):
            st1 = first_lines[j]
            print(st1, file=out_file)
            i = i + 1
        while j < len(second_lines):
            st2 = second_lines[j]
            print(st2, file=out_file)
            j = j + 1
        out_file.close()

    def __loadFromText(self, fileName: str):
        """
        The loadFromText method takes a String filename as an input. It reads given file line by line and splits
        according to space and assigns each word to the String array. Then, adds these word with their flags to the
        words list. At the end it sorts the words list.

        PARAMETERS
        ----------
        fileName : str
            File name input.
        """
        input_file = open(fileName, "r", encoding="utf8")
        lines = input_file.readlines()
        for line in lines:
            word_list = line.split()
            if len(word_list) > 0:
                current_word = TxtWord(word_list[0])
                for i in range(1, len(word_list)):
                    current_word.addFlag(word_list[i])
                self.words.append(current_word)
        input_file.close()
        self.words.sort(key=cmp_to_key(self.comparator))

    def __loadMisspelledWords(self, fileName: str):
        """
        The loadMisspellWords method takes a String filename as an input. It reads given file line by line and splits
        according to space and assigns each word with its misspelled form to the the misspelledWords hashMap.

        PARAMETERS
        ----------
        fileName : str
            File name input.
        """
        input_file = open(fileName, "r", encoding="utf8")
        lines = input_file.readlines()
        for line in lines:
            word_list = line.split()
            if len(word_list) == 2:
                self.__misspelled_words[word_list[0]] = word_list[1]
        input_file.close()

    def __loadMorphologicalLexicon(self, fileName: str):
        """
        The loadMisspellWords method takes a String filename as an input. It reads given file line by line and splits
        according to space and assigns each word with its misspelled form to the the misspelledWords hashMap.

        PARAMETERS
        ----------
        fileName : str
            File name input.
        """
        input_file = open(fileName, "r", encoding="utf8")
        lines = input_file.readlines()
        for line in lines:
            word_list = line.split()
            if len(word_list) == 2:
                word = self.getWord(word_list[0])
                if word is not None and isinstance(word, TxtWord):
                    word.setMorphology(word_list[1])
        input_file.close()

    def getCorrectForm(self, misspelledWord: str) -> str:
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
        if misspelledWord in self.__misspelled_words:
            return self.__misspelled_words[misspelledWord]
        return ""

    def saveAsTxt(self, fileName: str):
        """
        The saveAsTxt method takes a filename as an input and prints out the items of words list.

        PARAMETERS
        ----------
        fileName : str
            String input.
        """
        output = open(fileName, "w", encoding="utf8")
        for word in self.words:
            print(word, file=output)
        output.close()

    def __addWordWhenRootSoften(self, trie: Trie, last: chr, root: str, word: TxtWord):
        """
        The addWordWhenRootSoften is used to add word to Trie whose last consonant will be soften.
        For instance, in the case of Dative Case Suffix, the word is 'müzik' when '-e' is added to the word, the last
        char is drooped and root became 'müzi' and by changing 'k' into 'ğ' the word transformed into 'müziğe' as in the
        example of 'Herkes müziğe doğru geldi'.

        In the case of accusative, possessive of third person and a derivative suffix, the word is 'kanat' when '-i' is
        added to word, last char is dropped, root became 'kana' then 't' transformed into 'd' and added to Trie. The
        word is changed into 'kanadı' as in the case of 'Kuşun kırık kanadı'.

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

    def prepareTrie(self) -> Trie:
        """
        The prepareTrie method is used to create a Trie with the given dictionary. First, it gets the word from
        dictionary, then checks some exceptions like 'ben' which does not fit in the consonant softening rule and
        transforms into 'bana', and later on it generates a root by removing the last char from the word however if the
        length of the word is greater than 1, it also generates the root by removing the last two chars from the word.

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
        endingKChangesIntoG condition, if it is true then addWord method with rootWithoutLast will be used with added
        'g'.
        Ex : ahenk + i = ahengi

        RETURNS
        -------
        Trie
            the resulting Trie.
        """
        result = Trie()
        last_before = ' '
        for i in range(self.size()):
            word = self.getWordWithIndex(i)
            if isinstance(word, TxtWord):
                root = word.getName()
                length = len(root)
                if root == "ben":
                    result.addWord("bana", word)
                if root == "sen":
                    result.addWord("sana", word)
                root_without_last = root[0:length - 1]
                if length > 1:
                    root_without_last_two = root[0:length - 2]
                else:
                    root_without_last_two = ""
                if length > 1:
                    last_before = root[length - 2]
                last = root[length - 1]
                result.addWord(root, word)
                if word.lastIdropsDuringSuffixation() or word.lastIdropsDuringPassiveSuffixation():
                    if word.rootSoftenDuringSuffixation():
                        self.__addWordWhenRootSoften(result, last, root_without_last_two, word)
                    else:
                        result.addWord(root_without_last_two + last, word)
                if word.isPortmanteauEndingWithSI():
                    result.addWord(root_without_last_two, word)
                if word.rootSoftenDuringSuffixation():
                    self.__addWordWhenRootSoften(result, last, root_without_last, word)
                if word.isPortmanteau():
                    if word.isPortmanteauFacedVowelEllipsis():
                        result.addWord(root_without_last_two + last + last_before, word)
                    else:
                        if word.isPortmanteauFacedSoftening():
                            if last_before == 'b':
                                result.addWord(root_without_last_two + 'p', word)
                            elif last_before == 'c':
                                result.addWord(root_without_last_two + 'ç', word)
                            elif last_before == 'd':
                                result.addWord(root_without_last_two + 't', word)
                            elif last_before == 'ğ':
                                result.addWord(root_without_last_two + 'k', word)
                            else:
                                pass
                        else:
                            result.addWord(root_without_last, word)
                if word.vowelEChangesToIDuringYSuffixation() or word.vowelAChangesToIDuringYSuffixation():
                    if last == 'e':
                        result.addWord(root_without_last, word)
                    elif last == 'a':
                        result.addWord(root_without_last, word)
                    else:
                        pass
                if word.endingKChangesIntoG():
                    result.addWord(root_without_last + 'g', word)
        return result

    def __repr__(self):
        return f"{self.words} {self.__misspelled_words}"
