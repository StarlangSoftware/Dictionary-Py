import unittest

from Dictionary.Trie.Trie import Trie
from Dictionary.TxtDictionary import TxtDictionary
from Dictionary.Word import Word


class TrieTest(unittest.TestCase):
    simpleTrie : Trie
    complexTrie: Trie

    def setUp(self) -> None:
        self.simpleTrie = Trie()
        self.simpleTrie.addWord("azı", Word("azı"))
        self.simpleTrie.addWord("az", Word("az"))
        self.simpleTrie.addWord("ad", Word("ad"))
        self.simpleTrie.addWord("adi", Word("adi"))
        self.simpleTrie.addWord("adil", Word("adil"))
        self.simpleTrie.addWord("a", Word("a"))
        self.simpleTrie.addWord("adilane", Word("adilane"))
        self.simpleTrie.addWord("ısı", Word("ısı"))
        self.simpleTrie.addWord("ısıtıcı", Word("ısıtıcı"))
        self.simpleTrie.addWord("ölü", Word("ölü"))
        self.simpleTrie.addWord("ölüm", Word("ölüm"))
        self.simpleTrie.addWord("ören", Word("ören"))
        self.simpleTrie.addWord("örgü", Word("örgü"))
        self.complexTrie = Trie()
        dictionary = TxtDictionary("../../../turkish_dictionary.txt", "../../../turkish_misspellings.txt")
        for i in range(dictionary.size()):
            self.complexTrie.addWord(dictionary.getWordWithIndex(i).getName(), dictionary.getWordWithIndex(i))

    def test_GetWordsWithPrefixSimple(self):
        self.assertEqual({Word("a")}, self.simpleTrie.getWordsWithPrefix("a"))
        self.assertEqual({Word("a"), Word("ad")}, self.simpleTrie.getWordsWithPrefix("ad"))
        self.assertEqual({Word("a"), Word("ad"), Word("adi")}, self.simpleTrie.getWordsWithPrefix("adi"))
        self.assertEqual({Word("a"), Word("ad"), Word("adi"), Word("adil")}, self.simpleTrie.getWordsWithPrefix("adil"))
        self.assertEqual({Word("a"), Word("ad"), Word("adi"), Word("adilane"), Word("adil")}, self.simpleTrie.getWordsWithPrefix("adilane"))
        self.assertEqual({Word("ölü")}, self.simpleTrie.getWordsWithPrefix("ölü"))
        self.assertEqual({Word("ölü"), Word("ölüm")}, self.simpleTrie.getWordsWithPrefix("ölüm"))
        self.assertEqual({Word("ısı")}, self.simpleTrie.getWordsWithPrefix("ısı"))
        self.assertEqual({Word("ısıtıcı"), Word("ısı")}, self.simpleTrie.getWordsWithPrefix("ısıtıcı"))

    def test_GetWordsWithPrefixComplex(self):
        self.assertEqual({Word("a")}, self.complexTrie.getWordsWithPrefix("a"))
        self.assertEqual({Word("a"), Word("ad")}, self.complexTrie.getWordsWithPrefix("ad"))
        self.assertEqual({Word("a"), Word("ad"), Word("adi")}, self.complexTrie.getWordsWithPrefix("adi"))
        self.assertEqual({Word("a"), Word("ad"), Word("adi"), Word("adil")}, self.complexTrie.getWordsWithPrefix("adil"))
        self.assertEqual({Word("a"), Word("ad"), Word("adi"), Word("adilane"), Word("adil")}, self.complexTrie.getWordsWithPrefix("adilane"))
        self.assertEqual({Word("ölü"), Word("öl")}, self.complexTrie.getWordsWithPrefix("ölü"))
        self.assertEqual({Word("ölü"), Word("öl"), Word("ölüm")}, self.complexTrie.getWordsWithPrefix("ölüm"))
        self.assertEqual({Word("ı"), Word("ısı")}, self.complexTrie.getWordsWithPrefix("ısı"))
        self.assertEqual({Word("ı"), Word("ısıtıcı"), Word("ısıt"), Word("ısı")}, self.complexTrie.getWordsWithPrefix("ısıtıcı"))


if __name__ == '__main__':
    unittest.main()
