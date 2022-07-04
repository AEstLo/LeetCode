class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_elements = sum(nums)
        if sum_elements % k != 0:
            return False
        nums.sort(reverse=True)
        n = len(nums)
        used = [False] * n
        targetSum = sum_elements // k
        
        def canPartitionBT(index, currentSum, current_k, memo):
            if current_k == 0:
                return True
            if currentSum < 0:
                return False
            if currentSum == 0:
                return canPartitionBT(0, targetSum, current_k - 1, memo)
            
            for i in range(index, n):
                if not used[i]:
                    used[i] = True
                    if canPartitionBT(i + 1, currentSum - nums[i], current_k, memo):
                        return True
                    used[i] = False
            return False
            
        return canPartitionBT(0, targetSum, k, memo)

