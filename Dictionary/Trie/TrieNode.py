from __future__ import annotations
from Dictionary.Word import Word


class TrieNode:
    """
    A constructor of TrieNode class which creates a new children.
    """

    def __init__(self):
        self.children = {}
        self.words = set()

    """
    The addWord method takes a String word, an index, and a Word root as inputs. First it creates a TrieNode child
    and it directly adds it to the set when the given index is equal to the length of given word.

    Then, it extracts the character at given index of given word and if children dictionary contains a mapping for the
    extracted character, it assigns it to the TrieNode child, else it creates a new TrieNode and assigns it to the
    child. At the end, it recursively calls the addWord method with the next index of child and puts the character with
    the child into the children dictionary.

    PARAMETERS
    ----------
    word : str
        String input.
    index : int
        Integer index.
    root : Word
        Word input to add.
    """
    def addWord(self, word: str, root: Word, index=0):
        if index == len(word):
            self.words.add(root)
            return
        ch = word[index]
        if ch in self.children:
            child = self.children[ch]
        else:
            child = TrieNode()
        child.addWord(word, root, index + 1)
        self.children[ch] = child

    """
    The getChild method takes a character and gets its corresponding value from children dictionary.

    PARAMETERS
    ----------
    ch : chr
        Character input.
        
    RETURNS
    -------
    TreeNode
        the value from children dictionary.
    """
    def getChild(self, ch : chr) -> TrieNode:
        return self.children.get(ch)

    """
    The getWords method returns the words set.

    
    RETURNS
    -------
    set
        the words set.
    """
    def getWords(self) -> set:
        return self.words
