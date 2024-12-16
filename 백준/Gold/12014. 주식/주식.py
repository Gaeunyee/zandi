import sys
input = sys.stdin.readline


T = int(input().strip())
for i in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    lis = []
    backTrack = []
    for tmp in lst:
        if not lis or tmp > lis[-1]:
            lis.append(tmp)
            continue
        start, end = 0, len(lis)-1
        while start <= end:
            mid = (start+end)//2
            if lis[mid] >= tmp:
                end = mid-1
            else:
                start = mid+1
        lis[start] = tmp

    print(f'Case #{i}')
    if len(lis) >= K:
        print(1)
    else:
        print(0)

