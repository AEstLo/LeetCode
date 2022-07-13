class Solution:
    def numDecodings(self, s: str) -> int:
        # Time: O(N)  -- without memoization O(2^N)
        # Space: O(N) -- without memoization O(1)

        N = len(s)
        valid_chars_second_element = {str(i) for i in range(0, 7)}

        memo = {}

        def getNumDecodings(index):
            if index >= N:
                return 1
            if s[index] == '0':
                return 0
            if index in memo:
                return memo[index]

            total = getNumDecodings(index + 1)

            if index < N - 1 and (s[index] == '1' or (s[index] == '2' and s[index + 1] in valid_chars_second_element)):
                total += getNumDecodings(index + 2)

            memo[index] = total
            return total

        return getNumDecodings(0)
