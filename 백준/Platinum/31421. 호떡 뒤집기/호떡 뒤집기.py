import sys
input = sys.stdin.readline

N = int(input().strip())
cmd = input().strip()
change = []
for i in range(N-1):
    if cmd[i] != cmd[i+1]:
        change.append(i+1)

if len(change) == 0:
    if cmd[0] == 'B':
        print(-1)
    else:
        print(0)
elif len(change) == 1:
    if cmd[0] == 'W':
        print(-1)
    else:
        print(1)
        print(change[0])
else:
    print(len(change))
    for i in change[:-2]:
        print(i)
    if cmd[-1] == 'B':
        print(change[-1])
        print(change[-2])
    else:
        print(change[-2])
        print(change[-1])

