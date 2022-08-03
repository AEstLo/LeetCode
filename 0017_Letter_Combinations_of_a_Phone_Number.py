class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Being n the length of digits
        # Time: O(4^n)
        # Space: O(4^n)
        map_digits = {}
        num = ord('2')
        letter = ord('a')
        seven_nine = (ord('7'), ord('9'))
        while num <= ord('9') and letter <= ord('z'):
            if num not in seven_nine:
                step = 3
            else:
                step = 4
            map_digits[chr(num)] = []
            for i in range(0, step):
                map_digits[chr(num)].append(chr(letter + i))
            letter += step
            num += 1

        def backtracking(index):
            if index < 0:
                return []
            if index == 0:
                return list(map_digits[digits[index]])
            ret = backtracking(index - 1)
            result = []
            for letter in map_digits[digits[index]]:
                for i in range(len(ret)):
                    result.append(ret[i] + letter)
            return result

        return backtracking(len(digits) - 1)

# Runtime: 37 ms, faster than 82.13% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14 MB, less than 31.70% of Python3 online submissions for Letter Combinations of a Phone Number.
