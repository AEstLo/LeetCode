class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def is_solution(day):
            acum = 0
            _m = 0
            for bloom in bloomDay:
                if bloom <= day:
                    acum += 1
                else:
                    acum = 0
                if acum == k:
                    acum = 0
                    _m += 1
                    if _m >= m:
                        return True
            return False

        if len(bloomDay) < m * k:
            return -1
        d = max(bloomDay)
        l, r = 1, d
        result = d
        while l <= r:
            day = l + (r - l) // 2
            print(l, r, day, is_solution(day), result)
            if is_solution(day):
                result = min(result, day)
                r = day - 1
            else:
                l = day + 1
        return result
