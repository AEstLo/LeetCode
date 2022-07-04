class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        return max(
            self.wiggleMaxLengthPosOrNeg(nums, True),
            self.wiggleMaxLengthPosOrNeg(nums, False)
        )

    def wiggleMaxLengthPosOrNeg(self, nums: List[int], startPositiveOrNegative: bool) -> int:
        N = len(nums)
        result = 1
        i = 1
        positive_or_negative = startPositiveOrNegative
        while i < N:
            if positive_or_negative:
                while i < N and nums[i] - nums[i - 1] <= 0:
                    i += 1
            else:
                while i < N and nums[i] - nums[i - 1] >= 0:
                    i += 1
            if i < N:
                result += 1
            positive_or_negative = not positive_or_negative
            i += 1
        return result
