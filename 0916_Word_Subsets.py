from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Being W1 the elements in words1
        # Being W2 the elements in words2
        # Being W1K the max. length of a word in words1
        # Being W2K the max. length of a word in words2
        # Time: O(W2*W2K) + O(W1 * W1K)
        # Space: O(W1K + W2K)
        subsets = []

        w2_counter = collections.Counter()
        for word2 in words2:
            c = collections.Counter(word2)
            for k in c:
                w2_counter[k] = max(w2_counter[k], c[k])

        def isUniversal(word1):
            w1_counter = collections.Counter(word1)
            for k in w2_counter:
                if w2_counter[k] > w1_counter[k]:
                    return False
            return True

        for word1 in words1:
            if isUniversal(word1):
                subsets.append(word1)
        return subsets

# Runtime: 831 ms, faster than 86.33% of Python3 online submissions for Word Subsets.
# Memory Usage: 18.8 MB, less than 38.67% of Python3 online submissions for Word Subsets.
