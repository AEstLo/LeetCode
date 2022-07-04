class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = Counter(t)
        window = Counter()
        # Length of the result, start and end positions
        result = [float("infinity"), -1, -1]
        have, need = 0, len(countT)
        l = 0

        for r in range(len(s)):
            c = s[r]
            if c in countT:
                window[c] += 1

                if window[c] == countT[c]:
                    have += 1

                while have == need:
                    # we have a result
                    currentResult = r - l + 1
                    if currentResult < result[0]:
                        result[0] = currentResult
                        result[1] = l
                        # +1 because we need to include this character
                        result[2] = r + 1

                    # At this point, we try to remove elements from the left
                    if s[l] in countT:
                        window[s[l]] -= 1
                        if window[s[l]] < countT[s[l]]:
                            have -= 1
                    l += 1
        return s[result[1]:result[2]] if result[0] != float("infinity") else ""
