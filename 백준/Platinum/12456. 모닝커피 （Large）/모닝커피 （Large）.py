import sys
from heapq import *
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    lst = [(0, 0, 0)]
    for _ in range(N):
        lst.append(tuple(map(int, input().split())))  # 수, 유통기한, 만족도
    lst.sort(key=lambda x: x[1], reverse=True)
    qu = []
    T = K
    res = 0
    for c, t, s in lst:
        time = T-t
        while qu and time > 0:
            ok, cnt = heappop(qu)
            ok *= -1
            if time < cnt:
                heappush(qu, (-ok, cnt - time))
                res += time * ok
                time = 0
                
            else:
                res += cnt * ok
                time -= cnt
        heappush(qu, (-s, c))
        T = t
    return res



T = int(input().strip())
for i in range(1, T+1):
    print(f'Case #{i}: {solve()}')


