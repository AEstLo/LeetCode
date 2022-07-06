class Solution:
    def isValid(self, s: str) -> bool:
        # being n the length of s
        # Time: O(n)
        # Space: O(n) -- the stack
        stack = []
        dict_brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        for c in s:
            if c in dict_brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                c_pop = stack.pop()
                if dict_brackets[c_pop] != c:
                    return False
        return not stack
