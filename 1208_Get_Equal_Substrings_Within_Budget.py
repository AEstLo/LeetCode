class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def getCost(index):
            return abs(ord(s[index])-ord(t[index]))
        
        max_length = 0
        cost_accumulated = 0
        q = deque()
        for i in range(len(s)):
            cost = getCost(i)
            cost_accumulated += cost
            q.append(cost)
            while cost_accumulated > maxCost:
                left = q.popleft()
                cost_accumulated -= left
            max_length = max(max_length, len(q))
        return max_length
