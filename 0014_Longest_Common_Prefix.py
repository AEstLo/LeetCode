class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Being N the number of strings and K the number of characters of the shortest string
        # Time: O(N * K)
        # Space: O(K)
        if len(strs[0]) == 0:
            return ''
        index = 0
        result = []
        while True:
            if len(strs[0]) < index + 1:
                return ''.join(result)
            current_char = strs[0][index]
            for s in strs:
                if len(s) < index + 1 or current_char != s[index]:
                    return ''.join(result)
            result.append(current_char)
            index += 1
        return ''
