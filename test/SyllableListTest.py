import unittest

from Syllibification.SyllableList import SyllableList


class SyllableListTest(unittest.TestCase):

    def test_SyllableList(self):
        syllableList = SyllableList("başöğretmen")
        self.assertEqual(syllableList.getSyllables(), ["ba", "şöğ", "ret", "men"])
        syllableList = SyllableList("fransa")
        self.assertEqual(syllableList.getSyllables(), ["fran", "sa"])
        syllableList = SyllableList("traktör")
        self.assertEqual(syllableList.getSyllables(), ["trak", "tör"])
        syllableList = SyllableList("kraker")
        self.assertEqual(syllableList.getSyllables(), ["kra", "ker"])
        syllableList = SyllableList("trake")
        self.assertEqual(syllableList.getSyllables(), ["tra", "ke"])
        syllableList = SyllableList("ilköğretim")
        self.assertEqual(syllableList.getSyllables(), ["il", "köğ", "re", "tim"])
        syllableList = SyllableList("semizotu")
        self.assertEqual(syllableList.getSyllables(), ["se", "mi", "zo", "tu"])
        syllableList = SyllableList("ali")
        self.assertEqual(syllableList.getSyllables(), ["a", "li"])
        syllableList = SyllableList("türk")
        self.assertEqual(syllableList.getSyllables(), ["türk"])
        syllableList = SyllableList("kırktürk")
        self.assertEqual(syllableList.getSyllables(), ["kırk", "türk"])
        syllableList = SyllableList("kardanadam")
        self.assertEqual(syllableList.getSyllables(), ["kar", "da", "na", "dam"])
        syllableList = SyllableList("çöpadam")
        self.assertEqual(syllableList.getSyllables(), ["çö", "pa", "dam"])
        syllableList = SyllableList("faal")
        self.assertEqual(syllableList.getSyllables(), ["fa", "al"])


if __name__ == '__main__':
    unittest.main()
