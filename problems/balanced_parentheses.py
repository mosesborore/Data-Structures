def balanced_paranthesis(expression: str):
    stack = []
    for i in expression:
        if i == "(":
            stack.append(i)
        else: 
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) != 0:
        return False
    return True

def balanced_paranthesis_(expression: str):
    stack = []
    for symbol in expression:
        if symbol in "[{(":
            stack.append(symbol)
        else: 
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    return False
    if len(stack) != 0:
        return False
    return True


def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


print(balanced_paranthesis("(()()()())"))
print(balanced_paranthesis("(((())))"))
print(balanced_paranthesis("()))"))

print()
print(balanced_paranthesis_("{(){}{}[][[]]}[{()}]"))
print(balanced_paranthesis_("{(){}{}[][[]]}[{})]"))
