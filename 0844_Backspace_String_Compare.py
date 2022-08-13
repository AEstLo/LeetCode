class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_i = len(s) - 1
        t_i = len(t) - 1
        while s_i >= 0 and t_i >= 0:
            diff_s = 0
            while s_i >= 0 and s[s_i] == '#':
                diff_s += 1
                s_i -= 1
            while s_i >= 0 and diff_s > 0:
                s_i -= 1
                if s[s_i] != '#':
                    diff_s -= 1
                else:
                    diff_s += 1

            diff_t = 0
            while t_i >= 0 and t[t_i] == '#':
                diff_t += 1
                t_i -= 1
            while t_i >= 0 and diff_t > 0:
                t_i -= 1
                if t[t_i] != '#':
                    diff_t -= 1
                else:
                    diff_t += 1

            if s_i >= 0 and t_i >= 0 and s[s_i] != t[t_i]:
                return False
            s_i -= 1
            t_i -= 1

        diff_s = 0
        while s_i >= 0 and s[s_i] == '#':
            diff_s += 1
            s_i -= 1
        while s_i >= 0 and diff_s > 0:
            s_i -= 1
            if s[s_i] != '#':
                diff_s -= 1
            else:
                diff_s += 1

        diff_t = 0
        while t_i >= 0 and t[t_i] == '#':
            diff_t += 1
            t_i -= 1
        while t_i >= 0 and diff_t > 0:
            t_i -= 1
            if t[t_i] != '#':
                diff_t -= 1
            else:
                diff_t += 1

        return s_i == t_i

# Runtime: 41 ms, faster than 72.62% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 14 MB, less than 24.07% of Python3 online submissions for Backspace String Compare.
