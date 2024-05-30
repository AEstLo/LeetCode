class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(operands[token](num2, num1))

        return stack[0]
