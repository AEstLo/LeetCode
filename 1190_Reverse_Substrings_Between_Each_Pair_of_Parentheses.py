class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        queue = deque()
        for c in s:
            if c != ")":
                stack.append(c)
                continue
            while stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()
            while queue:
                stack.append(queue.popleft())
        return ''.join(stack[::])
