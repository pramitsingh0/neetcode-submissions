class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif t == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif t == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 / num1
                if res < 0: res = math.ceil(res)
                else: res = math.floor(res)
                stack.append(res)
            elif t == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            else:
                stack.append(int(t))
        return stack[0] if stack else 0
