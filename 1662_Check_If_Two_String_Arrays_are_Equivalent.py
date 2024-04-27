from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = 0
        w2 = 0
        w1_i = 0
        w2_i = 0
        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][w1_i] != word2[w2][w2_i]:
                return False
            w1_i += 1
            w2_i += 1
            if w1_i >= len(word1[w1]):
                w1_i = 0
                w1 += 1
            if w2_i >= len(word2[w2]):
                w2_i = 0
                w2 += 1
        return w1 >= len(word1) and w2 >= len(word2)
