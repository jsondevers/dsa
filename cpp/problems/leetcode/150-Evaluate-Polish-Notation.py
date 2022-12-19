from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}

        for c in tokens:
            if c in operations:
                v1 = int(stack.pop())
                v2 = int(stack.pop())
                if c == "+":
                    stack.append(v2 + v1)
                elif c == "-":
                    stack.append(v2 - v1)
                elif c == "*":
                    stack.append(v2 * v1)
                elif c == "/":
                    stack.append(int(v2 / v1))

            else:
                stack.append(int(c))

        return stack.pop()
