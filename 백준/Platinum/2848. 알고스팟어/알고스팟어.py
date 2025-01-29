import sys
from collections import deque
input = sys.stdin.readline
INF = 10**9+7


N = int(input().strip())
word = []
for _ in range(N):
    word.append(input().strip().ljust(10, '0'))

order = dict()

def setOrder(words):
    tr = words[0][0]
    buf = []
    for i in words:
        if i[0] not in order:
            order[i[0]] = []
        if tr not in order:
            order[tr] = []
        if i[0] != tr:
            if buf:
                setOrder(buf)
            if len(i) > 1:
                buf = [i[1:]]
            if i[0] not in order[tr]:
                order[tr].append(i[0])
            tr = i[0]
        else:
            if len(i) > 1:
                buf.append(i[1:])
    if buf:
        setOrder(buf)


setOrder(word)
deg = dict()
for k in order.keys():
    if k not in deg:
        deg[k] = 0
    if k == '0':
        continue
    for j in order[k]:
        if j not in deg:
            deg[j] = 0
        deg[j] += 1
qu = deque()
for key, d in deg.items():
    if key != '0' and not d:
        qu.append(key)
if deg['0'] != 0:
    print('!')
    exit()
res = ''
flag = True
while qu:
    if len(qu) >= 2:
        flag = False
    t = qu.popleft()
    res += t
    for j in order[t]:
        deg[j] -= 1
        if deg[j] == 0:
            qu.append(j)

if len(order)-1 != len(res):
    print('!')
elif not flag:
    print('?')
else:
    print(res)

