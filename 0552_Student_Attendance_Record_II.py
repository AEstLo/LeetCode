class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        memo = {}

        def backtracking2(i):
            result = 0
            if i ==0:
                return 0
            prev = [
                # 0-L, 1-L, 2-L
                [1, 1, 0], # 0-A
                [1, 0, 0], # 1-A
            ]
            for iii in range(1, i):
                aux = [[0,0,0], [0,0,0]]
                # +P
                for k in range(3):
                    aux[0][0] += prev[0][k] % MOD
                    aux[1][0] += prev[1][k] % MOD
                
                # +L
                aux[0][1] += prev[0][0] % MOD
                aux[0][2] += prev[0][1]%MOD
                aux[1][1] += prev[1][0] % MOD
                aux[1][2] += prev[1][1]%MOD
                # +A
                for k in range(3):
                    aux[1][0] += prev[0][k] %MOD
                prev = aux
            result = 0
            for j in range(2):
                for k in range(3):
                    result = (result + prev[j][k]) % MOD
            return result

        def backtracking(i, totalA, consecutiveL):
            if totalA > 1:
                return 0
            if consecutiveL > 2:
                return 0
            if i < 1:
                return 1
            if (i, totalA, consecutiveL) in memo:
                return memo[(i, totalA, consecutiveL)]

            # add an A
            total = backtracking(i - 1, totalA + 1, 0)
            # add a L
            total += backtracking(i - 1, totalA, consecutiveL + 1)
            # add a P
            total += backtracking(i - 1, totalA, 0)

            memo[(i, totalA, consecutiveL)] = total % MOD
            return total % MOD
        # return backtracking(n, 0, 0)
        return backtracking2(n)
