class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        expected_result = 0
        for num in nums:
            expected_result |= num
        
        n = len(nums)

        def isOrSubset(acumulated: int, index: int) -> int:
            if index >= n:
                return 1 if acumulated == expected_result else 0
            # Including current index
            total_subsets = isOrSubset(acumulated | nums[index], index + 1)
            # Not including current index
            total_subsets += isOrSubset(acumulated, index + 1)
            return total_subsets

        return isOrSubset(0, 0)
