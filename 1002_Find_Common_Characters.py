class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = Counter(words[0])
        for word in words[1:]:
            s &= Counter(word)
        ret = []
        for char, count in s.items():
            for _ in range(count):
                ret.append(char)
        return ret
