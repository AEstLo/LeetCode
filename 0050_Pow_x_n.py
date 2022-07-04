class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = self.myPowPositive(x, abs(n))
        return result if n >= 0 else 1/result

    def myPowPositive(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        partialPow = self.myPow(x, n // 2)
        result = partialPow * partialPow
        if n % 2 != 0:
            result *= x 
        return result
