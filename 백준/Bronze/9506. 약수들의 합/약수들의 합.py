import sys
input = sys.stdin.readline


while True:
    N = int(input().strip())
    if N == -1:
        break
    lst = []
    for i in range(1, N):
        if N % i == 0:
            lst.append(i)
    if sum(lst) == N:
        print(N, "=", ' + '.join(map(str, lst)))
    else:
        print(N, 'is NOT perfect.')

