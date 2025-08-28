import sys
input = sys.stdin.readline

N = int(input())
p = ['*']


def str(N):
    tri = []

    if N == 1:
        return p
    else:
        n = N // 5
        pre = str(N // 5)
        c = 0
        for i in pre:
            tri.append(' ' * n*2 + i + ' ' * n*2)
        for i in pre:
            tri.append(' ' * n*2 + i + ' ' * n*2)

        for i in pre:
            tri.append(i * 5)

        for i in pre:
            tri.append(' ' * n + i*3 + ' ' * n)

        for i in pre:
            tri.append(' ' * n + i + ' ' * n + i + ' ' * n)

        return tri


print('\n'.join(str(5**N)))