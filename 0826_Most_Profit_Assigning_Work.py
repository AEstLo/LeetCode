class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        m = len(worker)
        n = len(profit)
        tuples = [(p,d) for p,d in zip(profit, difficulty)]
        tuples.sort()
        tuples_idx = n - 1
        profit = 0
        for i in range(m - 1, -1, -1):
            j = tuples_idx
            while j >= 0 and tuples[j][1] > worker[i]:
                j -= 1
            tuples_idx = j
            if tuples_idx >= 0:
                profit += tuples[tuples_idx][0]
        return profit
