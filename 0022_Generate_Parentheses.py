class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def genParenthesis(total, diff, result, results):
            if diff < 0:
                return
            if total == 0:
                if diff == 0:
                    results.append(result)
                return
            genParenthesis(total - 1, diff + 1, result + '(', results)
            genParenthesis(total - 1, diff - 1, result + ')', results)
        res = []
        genParenthesis(2*n, 0, '', res)
        return res
