class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        left2right = [1] * N
        right2left = [1] * N

        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
            else:
                left2right[i] = 1

        for i in range(N-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                right2left[i-1] = right2left[i] + 1
            else:
                right2left[i-1] = 1

        total = 0
        for i in range(N):
            total += max(left2right[i], right2left[i])

        return total
