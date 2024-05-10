class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        while num >= 1000:
            result.append("M")
            num -= 1000
        
        multiply = 100
        substractors_map = {
            100: "C",
            10: "X",
            1: "I"
        }
        symbols_map = {
            100: "M",
            10: "C",
            1: "X"
        }
        five_map = {
            100: "D",
            10: "L",
            1: "V"
        }
        ten_map = {
            100: "C",
            10: "X",
            1: "I"
        }
        while num > 0:
            next_digit = num // multiply
            if next_digit not in (4, 9):
                if next_digit >= 5:
                    result.append(five_map[multiply])
                    next_digit -= 5
                while next_digit > 0:
                    result.append(ten_map[multiply])
                    next_digit -= 1
            else:
                result.append(substractors_map[multiply])
                if next_digit == 4:
                    result.append(five_map[multiply])
                else:
                    result.append(symbols_map[multiply])

            num = num % multiply
            multiply //= 10
        return ''.join(result)
