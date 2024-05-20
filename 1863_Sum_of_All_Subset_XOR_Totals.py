class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []

        def rec(position):
            if position >= len(nums):
                if not subset:
                    return 0
                result = subset[0]
                for i in range(1, len(subset)):
                    result ^= subset[i]
                return result
            solution = 0
            subset.append(nums[position])
            solution += rec(position + 1)
            subset.pop()
            solution += rec(position + 1)
            return solution
        
        return rec(0)
