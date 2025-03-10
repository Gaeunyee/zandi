import sys
input = sys.stdin.readline

TEAM = input().split()
p = {}
hash = {}
for t in range(4):
    p[TEAM[t]] = 0
    hash[TEAM[t]] = t
lst = []
for _ in range(6):
    t1, t2, *rate = input().split()
    lst.append((t1, t2)+tuple(map(float, rate)))


def f(rank):
    tmp = 0
    ret = []
    while tmp <= 3:
        c = [rank[tmp][1]]
        if tmp == 3:
            ret.append(c)
            break
        while rank[tmp][0] == rank[tmp + 1][0]:
            c.append(rank[tmp+1][1])
            tmp += 1
            if tmp == 3:
                ret.append(c)
                return ret
        ret.append(c)
        tmp += 1
    return ret



def solve(i, R, score):
    a, b, c, d = score
    if i == 6:
        winner = []
        rank = sorted([(a, TEAM[0]), (b, TEAM[1]), (c, TEAM[2]), (d, TEAM[3])], reverse=True)
        for r in f(rank):
            if len(winner) >= 2:
                break
            if len(r)+len(winner) <= 2:
                winner += r
                for name in r:
                    p[name] += R
            else:
                for name in r:
                    p[name] += R*(2-len(winner))/len(r)
                winner += r
        return
    win = score[:]
    lose = score[:]
    draw = score[:]
    win[hash[lst[i][0]]] += 3
    draw[hash[lst[i][0]]] += 1
    draw[hash[lst[i][1]]] += 1
    lose[hash[lst[i][1]]] += 3

    solve(i+1, lst[i][2]*R, win)
    solve(i + 1, lst[i][3] * R, draw)
    solve(i + 1, lst[i][4] * R, lose)

solve(0, 1, [0, 0, 0, 0])
print(*p.values())


