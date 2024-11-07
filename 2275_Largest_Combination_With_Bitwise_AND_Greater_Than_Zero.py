class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # n = len(candidates)
        # result = [0]
        # 
        # def backtrack(pos, and_acum, total_candidates):
        #     if and_acum == 0:
        #         return
        #     if pos >= n:
        #         result[0] = max(result[0], total_candidates)
        #         return
        #     backtrack(pos+1, and_acum, total_candidates)
        #     if pos < n - 1:
        #         backtrack(pos+1, candidates[pos+1] & and_acum, total_candidates + 1)
        #     return
        # 
        # for i, num in enumerate(candidates):
        #     backtrack(i, num, 1)
        # return result[0]
        total = [0] * 24
        for num in candidates:
            bit_repr = "{0:024b}".format(num)
            for i in range(24):
                if bit_repr[i] == '1':
                    total[i] += 1
        
        return max(total)
