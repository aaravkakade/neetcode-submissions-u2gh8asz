class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in tokens:
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                total = int(a) + int(b)
                stack.append(total)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                total = int(b) - int(a)
                stack.append(total)
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                total = int(a) * int(b)
                stack.append(total)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                total = int(b / a)
                stack.append(total)
            else:
                stack.append(int(i))
        return int(stack[0])
            