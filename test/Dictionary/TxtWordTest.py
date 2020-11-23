import unittest

from Dictionary.TxtDictionary import TxtDictionary


class TxtWordTest(unittest.TestCase):

    dictionary: TxtDictionary

    def setUp(self) -> None:
        self.dictionary = TxtDictionary("../../turkish_dictionary.txt", "../../turkish_misspellings.txt")

    def test_VerbType(self):
        verbs = {}
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            verbType = word.verbType()
            if verbType in verbs:
                verbs[verbType] = verbs[verbType] + 1
            else:
                verbs[verbType] = 1
        self.assertEqual(5, verbs["F2P1-NO-REF"])
        self.assertEqual(1, verbs["F3P1-NO-REF"])
        self.assertEqual(1, verbs["F4P1-NO-REF"])
        self.assertEqual(14, verbs["F4PR-NO-REF"])
        self.assertEqual(2, verbs["F4PL-NO-REF"])
        self.assertEqual(67, verbs["F4PW-NO-REF"])
        self.assertEqual(10, verbs["F5PL-NO-REF"])
        self.assertEqual(111, verbs["F5PR-NO-REF"])
        self.assertEqual(1, verbs["F5PW-NO-REF"])
        self.assertEqual(2, verbs["F1P1"])
        self.assertEqual(11, verbs["F2P1"])
        self.assertEqual(4, verbs["F3P1"])
        self.assertEqual(1, verbs["F4P1"])
        self.assertEqual(1, verbs["F5P1"])
        self.assertEqual(7, verbs["F6P1"])
        self.assertEqual(2, verbs["F2PL"])
        self.assertEqual(49, verbs["F4PL"])
        self.assertEqual(18, verbs["F5PL"])
        self.assertEqual(173, verbs["F4PR"])
        self.assertEqual(808, verbs["F5PR"])
        self.assertEqual(1396, verbs["F4PW"])
        self.assertEqual(13, verbs["F5PW"])

    def test_IsNominal(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isNominal():
                count = count + 1
        self.assertEqual(30601, count)

    def test_IsPassive(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isPassive():
                count = count + 1
        self.assertEqual(10, count)

    def test_IsAbbreviation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isAbbreviation():
                count = count + 1
        self.assertEqual(102, count)

    def test_IsInterjection(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isInterjection():
                count = count + 1
        self.assertEqual(104, count)

    def test_IsDuplicate(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isInterjection():
                count = count + 1
        self.assertEqual(104, count)

    def test_IsAdjective(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isAdjective():
                count = count + 1
        self.assertEqual(9679, count)

    def test_IsPronoun(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isPronoun():
                count = count + 1
        self.assertEqual(49, count)

    def test_IsQuestion(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isQuestion():
                count = count + 1
        self.assertEqual(4, count)

    def test_IsVerb(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isVerb():
                count = count + 1
        self.assertEqual(5042, count)

    def test_IsPortmanteau(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isPortmanteau():
                count = count + 1
        self.assertEqual(1294, count)

    def test_IsDeterminer(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isDeterminer():
                count = count + 1
        self.assertEqual(13, count)

    def test_IsConjunction(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isConjunction():
                count = count + 1
        self.assertEqual(51, count)

    def test_IsAdverb(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isAdverb():
                count = count + 1
        self.assertEqual(1849, count)

    def test_IsPostP(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isPostP():
                count = count + 1
        self.assertEqual(49, count)

    def test_IsPortmanteauEndingWithSI(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isPortmanteauEndingWithSI():
                count = count + 1
        self.assertEqual(178, count)

    def test_IsPortmanteauFacedVowelEllipsis(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isPortmanteauFacedVowelEllipsis():
                count = count + 1
        self.assertEqual(25, count)

    def test_IsPortmanteauFacedSoftening(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isPortmanteauFacedSoftening():
                count = count + 1
        self.assertEqual(348, count)

    def test_IsSuffix(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isSuffix():
                count = count + 1
        self.assertEqual(3, count)

    def test_IsProperNoun(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isProperNoun():
                count = count + 1
        self.assertEqual(19012, count)

    def test_IsPlural(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isPlural():
                count = count + 1
        self.assertEqual(398, count)

    def test_IsNumeral(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isNumeral():
                count = count + 1
        self.assertEqual(33, count)

    def test_NotObeysVowelHarmonyDuringAgglutination(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.notObeysVowelHarmonyDuringAgglutination():
                count = count + 1
        self.assertEqual(315, count)

    def test_ObeysAndNotObeysVowelHarmonyDuringAgglutination(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.obeysAndNotObeysVowelHarmonyDuringAgglutination():
                count = count + 1
        self.assertEqual(5, count)

    def test_RootSoftenDuringSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.rootSoftenDuringSuffixation():
                count = count + 1
        self.assertEqual(5529, count)

    def test_RootSoftenAndNotSoftenDuringSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.rootSoftenAndNotSoftenDuringSuffixation():
                count = count + 1
        self.assertEqual(14, count)

    def test_VerbSoftenDuringSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.verbSoftenDuringSuffixation():
                count = count + 1
        self.assertEqual(87, count)

    def test_NounSoftenDuringSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.nounSoftenDuringSuffixation():
                count = count + 1
        self.assertEqual(5443, count)

    def test_EndingKChangesIntoG(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.endingKChangesIntoG():
                count = count + 1
        self.assertEqual(26, count)

    def test_IsExceptional(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.isExceptional():
                count = count + 1
        self.assertEqual(31, count)

    def test_DuplicatesDuringSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.duplicatesDuringSuffixation():
                count = count + 1
        self.assertEqual(36, count)

    def test_DuplicatesAndNotDuplicatesDuringSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.duplicatesAndNotDuplicatesDuringSuffixation():
                count = count + 1
        self.assertEqual(4, count)

    def test_LastIdropsDuringSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.lastIdropsDuringSuffixation():
                count = count + 1
        self.assertEqual(167, count)

    def test_LastIDropsAndNotDropDuringSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.lastIDropsAndNotDropDuringSuffixation():
                count = count + 1
        self.assertEqual(4, count)

    def test_TakesRelativeSuffixKi(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.takesRelativeSuffixKi():
                count = count + 1
        self.assertEqual(16, count)

    def test_TakesRelativeSuffixKu(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.takesRelativeSuffixKu():
                count = count + 1
        self.assertEqual(4, count)

    def test_LastIdropsDuringPassiveSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.lastIdropsDuringPassiveSuffixation():
                count = count + 1
        self.assertEqual(11, count)

    def test_VowelAChangesToIDuringYSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.vowelAChangesToIDuringYSuffixation():
                count = count + 1
        self.assertEqual(1300, count)

    def test_VowelEChangesToIDuringYSuffixation(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.vowelEChangesToIDuringYSuffixation():
                count = count + 1
        self.assertEqual(2, count)

    def test_TakesSuffixIRAsAorist(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if not word.takesSuffixIRAsAorist():
                count = count + 1
        self.assertEqual(51, count)

    def test_TakesSuffixDIRAsFactitive(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if not word.takesSuffixDIRAsFactitive():
                count = count + 1
        self.assertEqual(197, count)

    def test_ShowsSuRegularities(self):
        count = 0
        for i in range(self.dictionary.size()):
            word = self.dictionary.getWordWithIndex(i)
            if word.showsSuRegularities():
                count = count + 1
        self.assertEqual(5, count)


if __name__ == '__main__':
    unittest.main()
