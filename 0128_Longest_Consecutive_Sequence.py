class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = {}
        longest = 0
        for num in nums:
            if num not in numbers:
                if num + 1 in numbers and num - 1 in numbers:
                    # Case 1: I'm in the middle, join the ranges
                    numbers[num] = numbers[num - 1] + 1
                    i = num + 1
                    val = numbers[num] + 1
                    while i in numbers:
                        numbers[i] = val
                        i += 1
                        val += 1
                    val -= 1
                elif num + 1 in numbers:
                    numbers[num] = 1
                    i = num + 1
                    val = numbers[num] + 1
                    while i in numbers:
                        numbers[i] = val
                        i += 1
                        val += 1
                    val -= 1
                elif num - 1 in numbers:
                    numbers[num] = numbers[num - 1] + 1
                    val = numbers[num]
                else:
                    numbers[num] = 1
                    val = 1
                longest = max(val, longest)
        return longest
