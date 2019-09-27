from Language.TurkishLanguage import TurkishLanguage
from Syllibification.Syllable import Syllable


class SyllableList:

    """
     A constructor of SyllableList class which takes a String word as an input. First it creates a syllable
     list and a sbSyllable. Then it loops i times, where i ranges from 0 to length of given word, first
     it gets the ith character of given word and checks whether it is a vowel and the last character of the word.

     If it is a vowel it appends it to the sbSyllable and if it is the last vowel it also appends the next character
     to the sbSyllable. Then, it adds the sbSyllable to the syllables list.

     If it is not a vowel, and the sbSyllable's length is 1 also the previous character is a consonant it gets the last
     item of syllables list since there cannot be a Turkish word which starts with two consonants. However, if it is
     two last characters of word, then it adds it to the syllablelist. At the end, it updates the syllables list.

    PARAMETERS
    ----------
    word : str
        String input.
    """
    def __init__(self, word : str):
        self.syllables = []
        sbSyllable = ""
        i = 0
        while i < len(word):
            c = word[i]
            isVowel = TurkishLanguage.isVowel(c)
            isLastChar = (i == len(word) - 1)
            if isVowel:
                sbSyllable += c
                #If it is the last vowel.
                if i == len(word) - 2:
                    sbSyllable += word[i + 1]
                    i = i + 1
                self.syllables.append(Syllable(sbSyllable))
                sbSyllable = ""
            else:
                # A syllable should not start with two consonants.
                tempSyl = sbSyllable
                if len(tempSyl) == 1:
                    # The previous character was also a consonant.
                    if not TurkishLanguage.isVowel(tempSyl[0]):
                        if len(self.syllables) == 0:
                            break
                        lastPos = len(self.syllables) - 1
                        str = self.syllables[lastPos].getText()
                        str = str + tempSyl
                        if isLastChar:
                            #If the last char is also a consonant, add it to latest syllable. Ex: 'park'.
                            str = str + c
                        # Update previous syllable.
                        self.syllables[lastPos] = Syllable(str)
                        sbSyllable = ""
                sbSyllable += c
            i = i + 1

    """
    The getSyllables method creates a new list syllables and loops through the globally defined syllables
    list and adds each item to the newly created syllables list.

    RETURNS
    -------
    list
        list syllables.
    """
    def getSyllables(self) -> list:
        syllables = []
        for syllable in self.syllables:
            syllables.append(syllable.getText())
        return syllables