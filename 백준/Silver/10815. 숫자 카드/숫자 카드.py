import sys
input = sys.stdin.readline


N = int(input().strip())
lst = list(map(int, input().split()))

Q = int(input().strip())
query = list(map(int, input().split()))

lst.sort()
for q in query:
    l, r = 0, N-1
    f = 0
    while l <= r:
        m = (l+r)//2
        if lst[m] == q:
            f = 1
            break
        elif lst[m] < q:
            l = m+1
        else:
            r = m-1
    print(1 if f else 0, end=' ')

