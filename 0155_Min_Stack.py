class StackElement:
    def __init__(self, val, minimum):
        self.val = val
        self.minimum = minimum


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            minimum = val
        else:
            prev_minimum = self.stack[-1].minimum
            minimum = min(val, prev_minimum)
        self.stack.append(StackElement(val, minimum))

    def pop(self) -> None:
        if not self.stack:
            raise Exception("Empty stack!")
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise Exception("Empty stack!")
        return self.stack[-1].val

    def getMin(self) -> int:
        if not self.stack:
            raise Exception("Empty stack!")
        return self.stack[-1].minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
