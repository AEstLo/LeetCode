class Heap:
    def __init__(self, array):
        self.heap = []
        for num in array:
            self.add(num)

    def add(self, num):
        index = len(self.heap)
        self.heap.append(num)
        while index > 0:
            parent_index = self.getParentIndex(index)
            if self.heap[parent_index] >= self.heap[index]:
                return
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def getMaximum(self):
        if not self.heap:
            return None
        maximum = self.heap[0]
        if len(self.heap) > 1:
            num = self.heap.pop()
            self.heap[0] = num
        self.heapifyDown()
        return maximum

    def heapifyDown(self):
        index = 0
        size = len(self.heap)
        left_child = self.getLeftIndex(index)
        while left_child < size:
            smaller_child_index = left_child
            right_child = self.getRightIndex(index)
            if right_child < size and self.heap[left_child] < self.heap[right_child]:
                smaller_child_index = right_child
            if self.heap[smaller_child_index] <= self.heap[index]:
                break
            self.heap[smaller_child_index], self.heap[index] = self.heap[index], self.heap[smaller_child_index]
            index = smaller_child_index
            left_child = self.getLeftIndex(index)

        return

    @staticmethod
    def getLeftIndex(index):
        return (index * 2) + 1

    @staticmethod
    def getRightIndex(index):
        return (index * 2) + 2

    @staticmethod
    def getParentIndex(index):
        return (index - 1) // 2


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap(nums)
        i = 1
        while i <= k:
            val = heap.getMaximum()
            i += 1
        return val

# Runtime: 3559 ms, faster than 5.00% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 27.2 MB, less than 14.18% of Python3 online submissions for Kth Largest Element in an Array.
