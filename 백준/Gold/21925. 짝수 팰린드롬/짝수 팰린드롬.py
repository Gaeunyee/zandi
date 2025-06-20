import sys
input = sys.stdin.readline


N = int(input().strip())
lst = list(map(int, input().split()))
m = []
for i in lst[:-1]:
    m.append(i)
    m.append('#')
m.append(lst[-1])


def Manacher(S):
    size = len(S)
    A = [0]*size
    r, c = -1, -1
    for i in range(size):
        if i <= r:
            A[i] = min(r - i, A[2*c-i])

        while i+A[i]+1 < size and i-A[i]-1 >= 0 and S[i-A[i]-1] == S[i+A[i]+1]:
            A[i] += 1

        if r < i+A[i]:
            r = i + A[i]
            c = i

    return A


size = Manacher(m)
end = 0
res = 0
for i in range(1, N, 2):
    if size[i+end] + 1 >= i-end + 1:
        end = i+1
        res += 1

print(res if end == N else -1)

