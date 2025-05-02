import sys
input = sys.stdin.readline


N = int(input().strip())
dist = list(map(int, input().split()))
s_dist = [0]*N
for i in range(1, N):
    s_dist[i] = s_dist[i-1]+dist[i-1]
cost = list(map(int, input().split()))
cost = [(cost[i], s_dist[i]) for i in range(N)]
t = sum(dist)
res = 0
cost.sort()
for c, d in cost:
    if t > d:
        res += (t-d)*c
        t = d

print(res)



