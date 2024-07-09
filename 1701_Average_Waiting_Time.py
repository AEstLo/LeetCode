class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_finish = -1
        total = 0
        for arrival, time in customers:
            if arrival < current_finish:
                additional_time = current_finish - arrival
            else:
                additional_time = 0
            current_finish = arrival + time + additional_time
            total += time + additional_time
        return total / len(customers)
