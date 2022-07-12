class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N = len(matchsticks)
        matchsticks.sort(reverse=True)
        # Time: O(4^N)
        # Space: O(N)
        square_sides = [0, 0, 0, 0]
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        square_border_size = total // 4

        def isSquare(index):
            if index == N:
                return square_sides[0] == square_sides[1] == square_sides[2] == square_border_size
            for i in range(4):
                if square_sides[i] + matchsticks[index] <= square_border_size:
                    square_sides[i] += matchsticks[index]
                    if isSquare(index + 1):
                        return True
                    square_sides[i] -= matchsticks[index]
            return False

        return isSquare(0)
