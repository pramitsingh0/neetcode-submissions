class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.extend([int(num1), int(num2), (int(num1) + int(num2))])
            elif op == "C":
                stack.pop()
            elif op == "D":
                num = stack.pop()
                stack.extend([int(num), (int(num) * 2)])
            else:
                stack.append(int(op))
        sum = 0
        for n in stack:
            sum += n
        return sum

