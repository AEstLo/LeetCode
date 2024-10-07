class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        FIVE = 0
        TEN = 1
        TWENTY = 2
        money = [0, 0, 0]
        for bill in bills:
            if bill == 5:
                money[FIVE] += 1
            elif bill == 10:
                money[TEN] += 1
                money[FIVE] -= 1
                if money[FIVE] < 0:
                    return False
            else:  # bill == 20
                money[TWENTY] += 1
                money[FIVE] -= 1
                if money[TEN] > 0:
                    money[TEN] -= 1
                else:
                    money[FIVE] -= 2
                if money[FIVE] < 0:
                    return False
        return True
