import sys
input = sys.stdin.readline

f = '(' + input().strip() + ')'


def execute(a, b, op):
    if op == '<':
        return min(a, b)
    elif op == '>':
        return max(a, b)
    elif op == '+':
        return a+b
    else:
        return a-b



tokens = []
i = 0
while i < len(f):
    if f[i] in '()+-<>?':
        tokens.append(f[i])
        i += 1
    elif f[i].isdigit():
        num = ''
        while i < len(f) and f[i].isdigit():
            num += f[i]
            i += 1
        tokens.append(num)



operand, operator = [], []
for i in tokens:
    if i == '?':
        continue
    if i == '(':
        operator.append(i)
    elif i == ')':
        while operator[-1] != '(':
            d2 = operand.pop()
            d1 = operand.pop()
            operand.append(execute(d1, d2, operator.pop()))
        operator.pop()
    elif i in ('+', '-'):
        while operator and (operator[-1] not in '()'):
            d2 = operand.pop()
            d1 = operand.pop()
            operand.append(execute(d1, d2, operator.pop()))
        operator.append(i)
    elif i in ('<', '>'):
        while operator and (operator[-1] not in '()+-'):
            d2 = operand.pop()
            d1 = operand.pop()
            operand.append(execute(d1, d2, operator.pop()))
        operator.append(i)
    else:
        operand.append(int(i))

print(operand[0])

