import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))

lst.sort(key=lambda x: x[1])
end = [0]*K
res = 0
for u, v in lst:
    for i in range(K):
        if end[i] < u:
            res += 1
            end[i] = v
            break

    end.sort(reverse=True)


print(res)

