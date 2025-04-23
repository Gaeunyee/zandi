import sys
input = sys.stdin.readline

N = int(input().strip())
res = 0
for _ in range(N):
    l = input().strip()
    arr = [0]*26
    for s in range(len(l)):
        i = ord(l[s])-97
        if arr[i] == 0 or l[s-1] == l[s]:
            arr[i] += 1
            continue
        else:
            res -= 1
            break
    res += 1

print(res)
