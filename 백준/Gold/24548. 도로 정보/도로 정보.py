import sys
input = sys.stdin.readline
mod = 10**9 + 7

N = int(input().strip())
l = input().strip()

lst = [[[[0]*3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
t = [0, 0, 0, 0]
g = 'TGFP'
lst[0][0][0][0] = 1
for i in l:
    t[g.find(i)] = (t[g.find(i)]+1)%3
    lst[t[0]][t[1]][t[2]][t[3]] += 1

res = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                res += lst[i][j][k][l]*(lst[i][j][k][l]-1)//2

print(res)




