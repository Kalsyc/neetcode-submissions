class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ('+', '-', '*', '/'):
                first_val = int(stack.pop())
                second_val = int(stack.pop())
                if i == '+':
                    stack.append(second_val + first_val)
                elif i == '-':
                    stack.append(second_val - first_val)
                elif i == '*':
                    stack.append(second_val * first_val)
                else:
                    stack.append(second_val / first_val)
            else:
                stack.append(i)
        return int(stack.pop())