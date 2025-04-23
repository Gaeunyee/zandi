import sys
input = sys.stdin.readline

l = input().strip()
arr = [0]*26
for i in l:
    if ord(i) >= 97:
        arr[ord(i)-97] += 1
    else:
        arr[ord(i)-65] += 1

cnt = 0
res = -1
m = max(arr)
for i in range(26):
    if arr[i] == m:
        if cnt != 0:
            print('?')
            exit()
        cnt += 1
        res = chr(i+65)

print(res)
