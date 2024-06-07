class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []
        dict_set = set(dictionary)
        l = 0
        r = 1
        while r < len(sentence) + 1:
            if sentence[l:r] in dict_set or r == len(sentence) or sentence[r] == ' ':
                result.append(sentence[l:r])
                while r < len(sentence) and sentence[r] != ' ':
                    r += 1
                l = r + 1
                r = l
            r += 1
        return ' '.join(result)
