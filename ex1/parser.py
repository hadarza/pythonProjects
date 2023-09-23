import re
from abc import ABC, abstractmethod
from numpy import double

class Expression(ABC):
    @abstractmethod
    def calc(self) -> double:
        pass

# Implement the classes here

class BinExp(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__()
        self.left = left
        self.right = right

class Num(Expression):
    def __init__(self, x):
        super().__init__()
        self.num = x

    def calc(self) -> double:
        return self.num

class Plus(BinExp):
    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__(left, right)

    def calc(self) -> double:
        return double(self.left.calc() + self.right.calc())

class Minus(BinExp):
    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__(left, right)

    def calc(self) -> double:
        return double(self.left.calc() - self.right.calc())

class Div(BinExp):
    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__(left, right)

    def calc(self) -> double:
        return double(self.left.calc() / self.right.calc())

class Mul(BinExp):
    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__(left, right)

    def calc(self) -> double:
        return double(self.left.calc() * self.right.calc())

# Implement the parser functions here

def infix_to_postfix(expression) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    # Use regular expressions to tokenize the expression
    tokens = minus_reducer(re.findall("[+/*()-]|\d+", expression))

    for token in tokens:
        if isAdigit(str(token)):
            output.append(str(token))
        elif token in precedence:
            while (stack and stack[-1] in precedence and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

def parser(infix_expression):
    postfix_expression = infix_to_postfix(infix_expression)
    stack = []
    try:
        for token in postfix_expression.split():
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid postfix expression")
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    if operand2 == 0:
                        raise ZeroDivisionError("Division by zero")
                    result = operand1 / operand2
                stack.append(result)
        if len(stack) == 1:
            return stack[0]
        else:
            raise ValueError("Invalid postfix expression")
    except (ValueError, ZeroDivisionError, IndexError):
        raise ValueError("Invalid postfix expression")
