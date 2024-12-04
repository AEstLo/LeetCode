class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False
        
        def getPrevChar(char):
            if char != 'a':
                return chr(ord(char) - 1)
            return 'z'


        str1_i = 0
        for c in str2:
            prev_c = getPrevChar(c)
            while str1_i < len(str1) and str1[str1_i] not in (c, prev_c):
                str1_i += 1
            if str1_i >= len(str1):
                return False
            str1_i += 1
        return True
