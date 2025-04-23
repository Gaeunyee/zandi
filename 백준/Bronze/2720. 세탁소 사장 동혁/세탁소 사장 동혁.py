import sys
input = sys.stdin.readline


T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(N//25, end=' ')
    N %= 25
    print(N // 10, end=' ')
    N %= 10
    print(N // 5,  end=' ')
    N %= 5
    print(N // 1)


