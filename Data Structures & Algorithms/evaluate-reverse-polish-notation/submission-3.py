class Solution:

    ops = ['+', '-', '*', '/']

    def operate(self, a, b, x):
        if x == '+':
            return a + b
        elif x == '-':
            return a - b
        elif x == '*':
            return a * b
        elif x == '/':
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        for x in tokens:
            if x in self.ops:
                b = stack.pop()
                a = stack.pop()
                res = self.operate(a, b, x)
                stack.append(int(res))
            else:
                stack.append(int(x))
            print(stack)
        
        return stack[-1]
