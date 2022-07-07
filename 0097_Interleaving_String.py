class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)
        if len(s3) != len_s1 + len_s2:
            return False
        if len_s1 == 0 and len_s2 == 0 and len_s3 == 0:
            return True
        memo = {}
        return self.isInterleaveRecursive(s1, s2, s3, len_s1, len_s2, len_s3, 0, 0, 0, memo)

    def isInterleaveRecursive(self, s1: str, s2: str, s3: str, len_s1: int, len_s2: int, len_s3: int,
                              pos_s1: int, pos_s2: int, pos_s3: int, memo: dict) -> bool:
        k = f'{pos_s1},{pos_s2},{pos_s3}'
        if k in memo:
            return memo[k]
        if pos_s1 >= len_s1 and pos_s2 >= len_s2 and pos_s3 >= len_s3:
            return True
        if pos_s3 >= len_s3:
            memo[k] = False
            return False

        ret = False
        if pos_s1 < len_s1 and s3[pos_s3] == s1[pos_s1]:
            ret |= self.isInterleaveRecursive(
                s1, s2, s3, len_s1, len_s2, len_s3, pos_s1 + 1, pos_s2, pos_s3 + 1, memo)
        if pos_s2 < len_s2 and s3[pos_s3] == s2[pos_s2]:
            ret |= self.isInterleaveRecursive(
                s1, s2, s3, len_s1, len_s2, len_s3, pos_s1, pos_s2 + 1, pos_s3 + 1, memo)
        memo[k] = ret
        return ret
