import sys
input = sys.stdin.readline

def Matching(x):
    visited[x] = True
    for next in adj[x]:
        if (pair[next] == -1 or
                ((not visited[pair[next]]) and Matching(pair[next]))):
                    pair[next] = x
                    return True
    return False


T = int(input().strip())
for _ in range(T):
    c, d, v = map(int, input().split())
    c_first = []
    d_first = []

    for _ in range(v):
        a, b = input().split()
        if a[0] == 'C':
            c_first.append((a, b))
        else:
            d_first.append((a, b))
    adj = []

    for i in range(len(c_first)):
        t = []
        for j in range(len(d_first)):
            if c_first[i][0] == d_first[j][1] or c_first[i][1] == d_first[j][0]:
                t.append(j)
        adj.append(t)

    pair = [-1]*(len(d_first))
    cnt = 0
    for l in range(len(adj)):
        visited = [False]*len(c_first)
        if Matching(l):
            cnt += 1
    print(v - cnt)


