class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Time: O(S)
        # Space: O(S)
        d_nextChar = collections.defaultdict(list)
        for word in words:
            d_nextChar[word[0]].append(word)
        result = 0
        for c in s:
            l = list(d_nextChar[c])
            d_nextChar[c] = []
            for word in l:
                if len(word) == 1:
                    result += 1
                else:
                    d_nextChar[word[1]].append(word[1:])
        return result

# Runtime: 890 ms, faster than 42.10% of Python3 online submissions for Number of Matching Subsequences.
# Memory Usage: 15.3 MB, less than 98.31% of Python3 online submissions for Number of Matching Subsequences.
