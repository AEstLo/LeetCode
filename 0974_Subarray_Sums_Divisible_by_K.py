class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixes = {0: 1}

        total = 0
        result = 0
        for num in nums:
            total += num
            rem = total % k
            if rem in prefixes:
                result += prefixes[rem]
                prefixes[rem] += 1
            else:
                prefixes[rem] = 1
        return result
