class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Time: O(N*2^N)
        # Space: O(N*2^N)
        result = []
        nums.sort()

        def backtrack(index, subset):
            if index == len(nums):
                result.append(list(subset))
                return

            # subsets that include the number
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()

            # subsets that don't include the number
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1, subset)
            return

        backtrack(0, [])
        return result

# Runtime: 49 ms, faster than 72.32% of Python3 online submissions for Subsets II.
# Memory Usage: 14.1 MB, less than 48.82% of Python3 online submissions for Subsets II.
