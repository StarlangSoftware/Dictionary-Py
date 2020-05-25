import unittest

from Syllibification.SyllableList import SyllableList


class SyllableListTest(unittest.TestCase):

    def test_SyllableList(self):
        syllableList = SyllableList("başöğretmen")
        self.assertEquals(syllableList.getSyllables(), ["ba", "şöğ", "ret", "men"])
        syllableList = SyllableList("fransa")
        self.assertEquals(syllableList.getSyllables(), ["fran", "sa"])
        syllableList = SyllableList("traktör")
        self.assertEquals(syllableList.getSyllables(), ["trak", "tör"])
        syllableList = SyllableList("kraker")
        self.assertEquals(syllableList.getSyllables(), ["kra", "ker"])
        syllableList = SyllableList("trake")
        self.assertEquals(syllableList.getSyllables(), ["tra", "ke"])
        syllableList = SyllableList("ilköğretim")
        self.assertEquals(syllableList.getSyllables(), ["il", "köğ", "re", "tim"])
        syllableList = SyllableList("semizotu")
        self.assertEquals(syllableList.getSyllables(), ["se", "mi", "zo", "tu"])
        syllableList = SyllableList("ali")
        self.assertEquals(syllableList.getSyllables(), ["a", "li"])
        syllableList = SyllableList("türk")
        self.assertEquals(syllableList.getSyllables(), ["türk"])
        syllableList = SyllableList("kırktürk")
        self.assertEquals(syllableList.getSyllables(), ["kırk", "türk"])
        syllableList = SyllableList("kardanadam")
        self.assertEquals(syllableList.getSyllables(), ["kar", "da", "na", "dam"])
        syllableList = SyllableList("çöpadam")
        self.assertEquals(syllableList.getSyllables(), ["çö", "pa", "dam"])
        syllableList = SyllableList("faal")
        self.assertEquals(syllableList.getSyllables(), ["fa", "al"])


if __name__ == '__main__':
    unittest.main()
