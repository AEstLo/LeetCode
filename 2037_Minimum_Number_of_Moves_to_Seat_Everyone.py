class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        sorted_seats = [0] * n
        sorted_students = [0] * n

        buckets_seats = [0] * 101
        buckets_students = [0] * 101

        for i in range(n):
            buckets_seats[seats[i]] += 1
            buckets_students[students[i]] += 1
        
        seats_i = 0
        students_i = 0
        for i in range(1, 101):
            while buckets_seats[i] > 0:
                buckets_seats[i] -= 1
                sorted_seats[seats_i] = i
                seats_i += 1
            while buckets_students[i] > 0:
                buckets_students[i] -= 1
                sorted_students[students_i] = i
                students_i += 1
        result = 0
        for i in range(n):
            result += abs(sorted_seats[i] - sorted_students[i])
        return result
