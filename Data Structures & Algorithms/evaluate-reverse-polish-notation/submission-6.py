class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                total = b + a
                stack.append(total)

            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                total = b - a
                stack.append(total)

            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                total = b * a
                stack.append(total)

            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                total = int(b / a)   # truncate toward 0
                stack.append(total)

            else:
                stack.append(int(i))  # convert once, store ints only

        return stack[0]
