class NumArray:
    # This is the implementation of a binary indexed tree or Fenwick tree

    def __init__(self, nums: List[int]):
        self.bit = [0] + nums
        self.nums = nums
        for idx in range(1, len(nums) + 1):
            idx2 = idx + (idx & -idx)
            if idx2 < len(nums) + 1:
                self.bit[idx2] += self.bit[idx]

    def add(self, index: int, val: int) -> None:
        i = index + 1
        while i < len(self.bit):
            self.bit[i] += val
            i += (i & -i)
        return

    def update(self, index: int, val: int) -> None:
        diff = self.nums[index] - val
        self.nums[index] = val
        self.add(index, -diff)
        return

    def sumRange(self, left: int, right: int) -> int:
        return self.sumPos(right + 1) - self.sumPos(left)

    def sumPos(self, index) -> int:
        i = index
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= (i & -i)
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# Runtime: 1752 ms, faster than 88.59% of Python3 online submissions for Range Sum Query - Mutable.
# Memory Usage: 30.9 MB, less than 82.91% of Python3 online submissions for Range Sum Query - Mutable.

# Very useful resource from Jakob Kogler:
# https://www.youtube.com/watch?v=v_wj_mOAlig&t=305s
# https://github.com/jakobkogler/Algorithm-DataStructures/blob/master/RangeQuery/BinaryIndexedTree.py
