import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in operations:
                num2 = stack.pop()
                num1 = stack.pop()

                resultado = operations[token](num1, num2)
                stack.append(resultado)
            else:
                stack.append(int(token))

        return stack[-1]

        