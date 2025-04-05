import sys
input = sys.stdin.readline


def solve():
    n = int(input().strip())
    stack = []
    nums = []
    res = []
    for _ in range(n):
        nums.append(int(input().strip()))
    counter = 0
    for tmp in nums:
        while counter < tmp:
            counter += 1
            stack.append(counter)
            res.append("+")

        if stack[-1] == tmp:
            stack.pop()
            res.append("-")
        else:
            print("NO")
            return
    for i in res:
        print(i)
    return


solve()
