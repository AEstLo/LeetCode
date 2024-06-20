class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def is_solution(distance):
            balls = 1
            prev_ball = 0
            for i in range(1, n):
                if position[i] - position[prev_ball] >= distance:
                    prev_ball = i
                    balls += 1
                if balls >= m:
                    return True
            return False
        
        l = 1
        r = ((position[-1] - position[0]) // (m - 1)) + 1
        max_distance = -1
        while l <= r:
            dist = l + (r - l) // 2
            if is_solution(dist):
                l = dist + 1
                max_distance = dist
            else:
                r = dist - 1
        return max_distance
