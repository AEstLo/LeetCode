class Solution:
    def numDecodings(self, s: str) -> int:
        # Tabular dp
        N = len(s)
        dp = [0] * (N + 1)
        dp[0] = 1
        if s[0] != '0':
            if s[0] != '*':
                dp[1] = 1
            else:
                dp[1] = 9

        one_to_nine = {str(i) for i in range(1, 10)}
        zero_to_six = {str(i) for i in range(7)}
        zero_to_six_asterisk = {str(i) for i in range(7)}
        zero_to_six_asterisk.add('*')

        for i in range(2, N + 1):
            # One step jump
            if s[i-1] in one_to_nine:  # (2)
                dp[i] += dp[i - 1]
            elif s[i - 1] == '*':
                dp[i] += dp[i - 1] * 9

            # Two step jump
            if s[i - 2] == '1':
                if s[i - 1] == '*':
                    dp[i] += dp[i - 2] * 9
                else:
                    dp[i] += dp[i - 2]
            elif s[i - 2] == '2' and s[i - 1] in zero_to_six_asterisk:
                if s[i - 1] == '*':
                    dp[i] += dp[i - 2] * 6
                else:
                    dp[i] += dp[i - 2]
            elif s[i - 2] == '*':
                if s[i - 1] == '*':
                    dp[i] += dp[i - 2] * 15
                elif s[i - 1] in zero_to_six:
                    dp[i] += dp[i - 2] * 2
                else:
                    dp[i] += dp[i - 2]
            dp[i] %= (10**9 + 7)
        return dp[len(s)]

    def numDecodingsMemo(self, s: str) -> int:
        # Time: O(N)  -- without memoization O(N^N)
        # Space: O(N) -- without memoization O(1)

        N = len(s)
        valid_chars_second_element = {str(i) for i in range(0, 7)}
        valid_chars_second_element_with_asterisk = {
            str(i) for i in range(0, 7)}
        valid_chars_second_element_with_asterisk.add('*')

        memo = {}

        def getNumDecodings(index):
            if index >= N:
                return 1
            if s[index] == '0':
                return 0
            if index in memo:
                return memo[index]

            total = getNumDecodings(index + 1)
            if s[index] == '*':
                total *= 9

            if (index < N - 1 and
                        (s[index] == '1' or
                         (s[index] == '2' and s[index + 1] in valid_chars_second_element_with_asterisk) or
                         s[index] == '*')
                    ):
                new_total = getNumDecodings(index + 2)
                if new_total > 0:
                    if s[index] == '1':
                        if s[index + 1] == '*':
                            total += new_total * 9
                        else:
                            total += new_total
                    elif s[index] == '2':
                        if s[index + 1] == '*':
                            total += new_total * 6
                        else:
                            total += new_total
                    else:  # s[index] == '*'
                        if s[index + 1] == '*':
                            total += new_total * 15
                        elif s[index + 1] in valid_chars_second_element:
                            total += new_total * 2
                        else:
                            total += new_total

            memo[index] = total
            return total

        ret = getNumDecodings(0) % (10**9 + 7)
        return ret
