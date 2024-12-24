import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
cmd = list(map(int, input().split()))

cost = 0
inq = [0]*(K+1)
plug = []
for id in range(K):
    i = cmd[id]
    if len(plug) < N and not inq[i]:
        plug.append((len(plug), i))
        inq[i] = 1
    elif not inq[i]:
        if not inq[i]:
            cost += 1
            max_d, max_v = -1, -1
            for idx, val in plug:
                d = 101
                for j in range(id+1, K):
                    if val == cmd[j]:
                        d = j
                        break
                if max_d < d:
                    max_d = d
                    max_v = idx
            inq[i] = 1
            inq[plug[max_v][1]] = 0
            plug[max_v] = (max_v, i)


print(cost)
