class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sorted_happiness = sorted(happiness, reverse=True)
        happiness_factor = 0
        result = 0
        i = 0
        while i < len(happiness) and k > 0:
            result += max(sorted_happiness[i] - happiness_factor, 0)
            i += 1
            happiness_factor += 1
            k -= 1
        return result
