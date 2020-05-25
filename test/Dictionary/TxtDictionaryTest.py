import unittest

from Dictionary.TxtDictionary import TxtDictionary
from Dictionary.Word import Word


class TxtDictionaryTest(unittest.TestCase):

    dictionary : TxtDictionary

    def setUp(self) -> None:
        self.dictionary = TxtDictionary("../../turkish_dictionary.txt", "../../turkish_misspellings.txt")

    def test_GetCorrectForm(self):
        for i in range(self.dictionary.size()):
            self.assertTrue(len(self.dictionary.getCorrectForm(self.dictionary.getWordWithIndex(i).getName())) == 0)

    def test_PrepareTrie(self):
        trie = self.dictionary.prepareTrie()
        self.assertTrue(Word("ben") in trie.getWordsWithPrefix("bana"))
        self.assertTrue(Word("metin") in trie.getWordsWithPrefix("metni"))
        self.assertTrue(Word("ağız") in trie.getWordsWithPrefix("ağzı"))
        self.assertTrue(Word("ayır") in trie.getWordsWithPrefix("ayrıldı"))
        self.assertTrue(Word("buyur") in trie.getWordsWithPrefix("buyruldu"))
        self.assertTrue(Word("ahit") in trie.getWordsWithPrefix("ahdi"))
        self.assertTrue(Word("kayıp") in trie.getWordsWithPrefix("kaybı"))
        self.assertTrue(Word("kutup") in trie.getWordsWithPrefix("kutbu"))
        self.assertTrue(Word("ademelması") in trie.getWordsWithPrefix("ademelmaları"))
        self.assertTrue(Word("ağaçküpesi") in trie.getWordsWithPrefix("ağaçküpeleri"))
        self.assertTrue(Word("ağaçlık") in trie.getWordsWithPrefix("ağaçlığı"))
        self.assertTrue(Word("sumak") in trie.getWordsWithPrefix("sumağı"))
        self.assertTrue(Word("deveboynu") in trie.getWordsWithPrefix("deveboyunları"))
        self.assertTrue(Word("gökcismi") in trie.getWordsWithPrefix("gökcisimleri"))
        self.assertTrue(Word("gökkuşağı") in trie.getWordsWithPrefix("gökkuşakları"))
        self.assertTrue(Word("hintarmudu") in trie.getWordsWithPrefix("hintarmutları"))
        self.assertTrue(Word("hintpirinci") in trie.getWordsWithPrefix("hintpirinçleri"))
        self.assertTrue(Word("sudolabı") in trie.getWordsWithPrefix("sudolapları"))
        self.assertTrue(Word("ye") in trie.getWordsWithPrefix("yiyor"))
        self.assertTrue(Word("de") in trie.getWordsWithPrefix("diyor"))
        self.assertTrue(Word("depola") in trie.getWordsWithPrefix("depoluyor"))
        self.assertTrue(Word("dışla") in trie.getWordsWithPrefix("dışlıyor"))
        self.assertTrue(Word("fiyonk") in trie.getWordsWithPrefix("fiyongu"))
        self.assertTrue(Word("gonk") in trie.getWordsWithPrefix("gongu"))


if __name__ == '__main__':
    unittest.main()
