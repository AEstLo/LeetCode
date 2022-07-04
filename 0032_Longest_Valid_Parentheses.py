class Solution:
    def longestValidParentheses(self, s: str) -> int:
        i = 0
        N = len(s)
        stack = [-1]
        longestValid = 0
        while i < N:
            if s[i] == '(':
                stack.append(i)
            else:  # ')'
                if stack:
                    stack.pop()
                    if not stack:
                        stack.append(i)
                    else:
                        ongoingLongestValid = i - stack[-1]
                        if ongoingLongestValid > longestValid:
                            longestValid = ongoingLongestValid
            i += 1
        return longestValid
