import sys
input = sys.stdin.readline


N, S = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
def backTrack(i, s):
    global res
    if i > 0 and s == S:
        res += 1
    for j in range(i, N):
        backTrack(j+1, s+arr[j])


backTrack(0, 0)
print(res)
