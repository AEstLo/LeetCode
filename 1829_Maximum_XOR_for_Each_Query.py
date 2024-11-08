class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        answer = []
        for num in reversed(nums):
            i = 0
            max_number = 0
            while i < maximumBit:
                if not ((1 << i) & xor):
                    max_number |= 1 << i
                i += 1
            answer.append(max_number)
            xor ^= num
        return answer
