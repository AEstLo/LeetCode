class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            sum_numbers = numbers[start] + numbers[end]
            if sum_numbers == target:
                return [start + 1, end + 1]
            elif sum_numbers < target:
                start += 1
            else:
                end -= 1
                
        return [-1, -1]
