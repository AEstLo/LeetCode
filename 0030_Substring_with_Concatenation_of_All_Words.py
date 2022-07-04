class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        len_w = len(words[0])
        ret = []
        words_dict = {}
        for word in words:
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
        for i in range(0, len(s) - (len_w * n) + 1):
            if self.findSubstringRec(s, i, words_dict, len_w):
                ret.append(i)
        return ret
    
    def findSubstringRec(self, s, s_start, words_dict, len_w):
        if not words_dict:
            return True
        str_to_review = s[s_start:s_start + len_w]
        if str_to_review in words_dict:
            if words_dict[str_to_review] <= 1:
                del words_dict[str_to_review]
            else:
                words_dict[str_to_review] -= 1
            ret = self.findSubstringRec(s, s_start + len_w, words_dict, len_w)
            if str_to_review in words_dict:
                words_dict[str_to_review] += 1
            else:
                words_dict[str_to_review] = 1
            return ret
        return False

