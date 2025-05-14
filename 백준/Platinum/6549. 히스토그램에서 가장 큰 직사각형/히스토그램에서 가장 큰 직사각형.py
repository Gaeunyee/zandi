import sys
input = sys.stdin.readline

while True:
    graph = list(map(int, input().split()))
    res = 0
    if graph[0] == 0:
        break
    graph.append(-1)
    st = []
    for i in range(1, len(graph)):
        while st and st[-1][1] > graph[i]:
            last = st.pop()
            t = (i-1) * last[1]
            if st:
                t = (i - st[-1][0] - 1) * last[1]
            if t > res:
                res = t
        st.append((i, graph[i]))

    print(res)

