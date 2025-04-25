import sys
input = sys.stdin.readline

def solve(x, y):
    w = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
         "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
    b = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB",
         "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
    s1 = 0
    for i in range(8):
        for j in range(8):
            if graph[x+i][y+j] != w[i][j]:
                s1 += 1
    s2 = 0
    for i in range(8):
        for j in range(8):
            if graph[x+i][y+j] != b[i][j]:
                s2 += 1

    return min(s1, s2)


N, M = map(int, input().split())
graph = []
res = 100
for _ in range(N):
    graph.append(input().strip())
for i in range(N-7):
    for j in range(M-7):
        res = min(res, solve(i, j))

print(res)
