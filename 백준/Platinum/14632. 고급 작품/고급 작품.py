import sys
input = sys.stdin.readline

def solve():
    def find(x, y):
        if parent[x][y] == y:
            return y
        parent[x][y] = find(x, parent[x][y])
        return parent[x][y]

    def union(x, y1, y2):
        a = find(x, y1)
        b = find(x, y2)
        if a > b:
            a, b = b, a
        if a < b:
            parent[x][a] = b
            return 1
        return 0

    stamp = [[]]
    stamp_size = [(0, 0)]
    N, M = map(int, input().split())
    K = int(input().strip())
    paper = [['.']*M for _ in range(N)]
    painted = [[0]*M for _ in range(N)]
    parent = [[i for i in range(M)] for _ in range(N)]
    for _ in range(K):
        H, W = map(int, input().split())
        stamp_size.append((H, W))
        st = []
        for _ in range(H):
            st.append(input().strip())
        stamp.append(st)
    cmd = []
    Q = int(input().strip())
    for _ in range(Q):
        cmd.append(tuple(map(int, input().split())))

    for q in range(Q-1, -1, -1):
        k, x, y = cmd[q]
        xSize, ySize = min(N, x+stamp_size[k][0]), min(M, y+stamp_size[k][1])
        for i in range(x, xSize):
            j = y
            while j < ySize:
                if j-1 >= y:
                    union(i, j-1, j)
                if painted[i][j]:
                    j = find(i, j) + 1
                    continue
                paper[i][j] = stamp[k][i-x][j-y]
                painted[i][j] = 1

                j += 1
            if y > 0 and painted[i][y-1]:
                union(i, y-1, y)
            if ySize < M and painted[i][ySize]:
                union(i, ySize-1, ySize)

    for i in range(N):
        print(''.join(paper[i]))



solve()
