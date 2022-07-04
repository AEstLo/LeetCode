class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.isMatchIndex(s, 0, p, 0, memo)
        
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in (s[0], '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatchIndex(self, s, i, p, j, memo):
        key = f'{i}-{j}'
        if key not in memo:
            if j >= len(p):
                memo[key] = i >= len(s)
            else:
                first_match = i < len(s) and p[j] in (s[i], '.')
                if j + 1 < len(p) and p[j + 1] == '*':
                    memo[key] = self.isMatchIndex(s, i, p, j + 2, memo) or first_match and self.isMatchIndex(s, i + 1, p, j, memo)
                else:
                    memo[key] = first_match and self.isMatchIndex(s, i + 1, p, j + 1, memo)
        return memo[key]
