import math
from functools import cmp_to_key

from Math.Vector import Vector
from Dictionary.Dictionary import Dictionary
from Dictionary.VectorizedWord import VectorizedWord


class VectorizedDictionary(Dictionary):

    def __init__(self, comparator=None, fileName=None):
        """
        A constructor of VectorizedDictionary class which calls its super class Dictionary.
        """
        super().__init__(comparator)
        if fileName is not None:
            input_file = open(fileName, "r", encoding="utf8")
            lines = input_file.readlines()
            for line in lines:
                items = line.split()
                vector = Vector(0, 0)
                for i in range(1, len(items)):
                    vector.add(float(items[i]))
                current_word = VectorizedWord(items[0], vector)
                self.words.append(current_word)
            input_file.close()
            self.words.sort(key=cmp_to_key(self.comparator))

    def addWord(self, word: VectorizedWord):
        """
        The addWord method takes a VectorizedWord as an input and adds it to the words list.

        PARAMETERS
        ----------
        word : VectorizedWord
            VectorizedWord input.
        """
        self.words.append(word)

    def mostSimilarWord(self, name: str) -> VectorizedWord:
        """
        The mostSimilarWord method takes a String name as an input, declares a maxDistance as -1 and creates a
        VectorizedWord word by getting the given name from words list. Then, it loops through the words list and if the
        current word is not equal to given input it calculates the distance between current word and given word by using
        dot product and updates the maximum distance. It then returns the result VectorizedWord which holds the most
        similar word to the given word.

        PARAMETERS
        ----------
        name : str
            String input.

        RETURNS
        -------
        VectorizedWord
            VectorizedWord type result which holds the most similar word to the given word.
        """
        max_distance = -1
        result = None
        word = self.getWord(name)
        if word is None:
            return None
        for current_word in self.words:
            if current_word != word and isinstance(word, VectorizedWord):
                distance = word.getVector().dotProduct(current_word.getVector())
                if distance > max_distance:
                    max_distance = distance
                    result = current_word
        return result

    def makeComparator(self, comparedWord: VectorizedWord):
        def compare(wordA, wordB):
            v = comparedWord.getVector()
            vA = wordA.getVector()
            vB = wordB.getVector()
            result1 = v.dotProduct(vB) / math.sqrt(v.dotProductWithSelf() * vB.dotProductWithSelf())
            result2 = v.dotProduct(vA) / math.sqrt(v.dotProductWithSelf() * vA.dotProductWithSelf())
            if result1 < result2:
                return -1
            elif result1 > result2:
                return 1
            else:
                return 0
        return compare

    def mostSimilarKWords(self, name: str, k: int) -> list:
        """
        The mostSimilarKWords method takes a String name and an integer k as inputs, and creates an list resultWords
        of type VectorizedWord and a VectorizedWord word by getting the given name from words list. Then, it loops
        through the words list and adds current word to the resultWords. It then sort resultWords list and if the size
        of the list is greater than given input k, it removes items from the ending. Then, it returns resultWords list.

        PARAMETERS
        ----------
        name : str
            String input.
        k : int
            Integer input.

        RETURNS
        -------
        list
            list result.
        """
        result_words = []
        word = self.getWord(name)
        if word is None:
            return result_words
        for current_word in self.words:
            result_words.append(current_word)
        result_words.sort(key=self.makeComparator(word))
        return result_words[0: k]

    def kMeansClustering(self, iteration: int, k: int) -> list:
        """
        The kMeansClustering method takes an integer iteration and k as inputs. K-means clustering aims to partition n
        observations into k clusters in which each observation belongs to the cluster with the nearest mean.

        PARAMETERS
        ----------
        iteration : int
            Integer input.
        k : int
            Integer input.

        RETURNS
        -------
        list
            list result which holds the k-means clustered words.
        """
        result = []
        means = []
        vector_size = self.words[0].getVector().size()
        for i in range(k):
            result.append([])
            v = Vector()
            v.initAllSame(vector_size, 0)
            means.append(v)
        for i in range(len(self.words)):
            result[i % k].append(self.words[i])
            means[i % k].add(self.words[i]).getVector()
        for i in range(k):
            means[i].divide(len(result[i]))
            means[i].divide(math.sqrt(means[i].dotProductWithSelf()))
        for i in range(iteration):
            for j in range(k):
                result[j].clear()
            for vectorized_word in self.words:
                max_cluster_distance = means[0].dotProduct(vectorized_word.getVector())
                max_cluster_index = 0
                for j in range(1, k):
                    cluster_distance = means[j].dotProduct(vectorized_word.getVector())
                    if cluster_distance > max_cluster_distance:
                        max_cluster_distance = cluster_distance
                        max_cluster_index = j
                result[max_cluster_index].append(vectorized_word)
            for j in range(k):
                means[j].clear()
                for word in result[j]:
                    means[j].add(word.getVector())
                means[j].divide(len(result[j]))
                means[j].divide(math.sqrt(means[j].dotProductWithSelf()))
        return result
