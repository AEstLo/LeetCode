class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        subsets = []

        def dfs(index, current_subset):
            if index == N:
                if current_subset:
                    return 1
                return 0
            # Do not include current element
            without_current = dfs(index + 1, current_subset)
            for num in current_subset:
                if abs(nums[index] - num) == k:
                    return without_current
            current_subset.append(nums[index])
            with_current = dfs(index + 1, current_subset)
            current_subset.pop()
            return without_current + with_current
        
        return dfs(0, [])
