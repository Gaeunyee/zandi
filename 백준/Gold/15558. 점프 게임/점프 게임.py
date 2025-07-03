import sys
from collections import deque
input = sys.stdin.readline


N, k = map(int, input().split())
lst = [0]+[input().strip() for _ in range(2)]
qu = deque()
qu.append((1, 0, 0))
visited = [0, [0]*N, [0]*N]
flag = 0
while qu:
    t, x, time = qu.popleft()
    if x+1 < N and lst[t][x+1] == '1' and not visited[t][x+1]:
        qu.append((t, x+1, time+1))
        visited[t][x+1] = 1
    if x-1 < N and lst[t][x-1] == '1' and not visited[t][x-1] and x-1 >= time+1:
        qu.append((t, x-1, time+1))
        visited[t][x-1] = 1
    if x+k < N and lst[t*-1][x+k] == '1' and not visited[t*-1][x+k]:
        qu.append((t*-1, x+k, time+1))
        visited[t*-1][x+k] = 1
    if x+k >= N:
        flag = 1
        break

print(flag)
