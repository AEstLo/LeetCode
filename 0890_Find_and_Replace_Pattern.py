class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # Being w the number of words and p the length of each
        # Time: O(w*p)
        # Space: O(w*p)
        ret = []
        len_word = len(pattern)  # constraint
        for word in words:  # O(w)
            map_chr = {}
            used_keys = set()
            add_word = True
            for i in range(len_word):  # O(p)
                if word[i] not in map_chr:
                    if pattern[i] not in used_keys:
                        map_chr[word[i]] = pattern[i]
                        used_keys.add(pattern[i])
                    else:
                        add_word = False
                        break
                elif map_chr[word[i]] != pattern[i]:
                    add_word = False
                    break
            if add_word:
                ret.append(word)

        return ret

# Runtime: 41 ms, faster than 81.21% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 14 MB, less than 29.59% of Python3 online submissions for Find and Replace Pattern.
