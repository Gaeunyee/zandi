import sys
input = sys.stdin.readline

N = int(input().strip())
lst = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    lst[i] += lst[i-1]

m = 10**15 + 7
K = -1
for k in range(N//2+1, 0, -1):
    for i in range(1, N-k+1):
        s = lst[i+k-1]-lst[i-1]
        for j in range(i+k, N-k+2):
            t = abs((lst[j + k - 1] - lst[j - 1]) - s)
            if m > t:
                m = t
                K = k
print(K)
print(m)
