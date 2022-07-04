class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        from queue import Queue
        q = Queue()
        q.put(start)
        while not q.empty():
            pos = q.get()
            if arr[pos] == 0:
                return True
            if arr[pos] > 0:
                if arr[pos] + pos < len(arr):
                    q.put(arr[pos] + pos)
                if pos - arr[pos] >= 0:
                    q.put(pos - arr[pos])
                arr[pos] *= -1
        return False
