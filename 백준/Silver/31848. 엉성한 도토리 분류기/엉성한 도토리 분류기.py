import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
hole = list(map(int, input().split()))
for i in range(N):
    hole[i] += i
Q = int(input().strip())
hq = []
dot = list(map(int, input().split()))
dotori = []
for i in range(Q):
    dotori.append((i, dot[i]))
dotori.sort(key=lambda x: x[1])

idx = 0
for i in range(Q):
    while dotori[i][1] > hole[idx]:
        idx += 1
    heapq.heappush(hq, (dotori[i][0], idx+1))
while hq:
    print(heapq.heappop(hq)[1], end=' ')
