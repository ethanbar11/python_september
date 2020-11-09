class Stack:
    def __init__(self):
        self.__lst = []

    def push(self, item):
        self.__lst.append(item)

    def is_empty(self):
        return len(self.__lst) == 0

    def pop(self):
        if not self.is_empty():
            x = self.__lst[-1]
            del self.__lst[-1]
            return x
        return "ERROR!"

    def top(self):
        if not self.is_empty():
            return self.__lst[-1]
        return "ERROR!"


def check_math_expression_is_valid(expression):
    # The expression is string.
    stack = Stack()
    opening_bracelets = ['{', '[', '(']
    closing_bracelets = ['}', ']', ')']
    for c in expression:
        if c in opening_bracelets:
            stack.push(c)
        elif c in closing_bracelets:
            opening = stack.pop()
            if opening == 'ERROR!':
                return False
            if opening_bracelets.index(opening) != closing_bracelets.index(c):
                return False
        else:
            pass
    if stack.is_empty():
        return True


expres='({5+9*[4/3]))+2'
print(check_math_expression_is_valid(expres))