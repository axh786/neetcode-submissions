import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        for token in tokens:
            if token in operations:
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = operations[token](operand1, operand2)
                stack.append(int(res))
            else:
                stack.append(int(token))
                
        return stack[0]
