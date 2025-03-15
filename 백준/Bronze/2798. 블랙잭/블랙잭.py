N, M = map(int, input().split())
lst = list(map(int, input().split()))
v = -1
for l in range(0, N-2):
    for m in range(l+1, N-1):
        for r in range(m+1, N):
            s = lst[l]+lst[m]+lst[r]
            if M>=s>v:
                v = s
                
print(v)