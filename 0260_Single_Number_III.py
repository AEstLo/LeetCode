class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        i = 1
        while not i & xor:
            i <<= 1
        a = i
        res1 = 0
        res2 = 0
        for num in nums:
            if num & a != 0:
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]
