import sys
input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.top = Node('')

    def insert(self, string):
        tmp = self.top
        for key in string:
            if key not in tmp.next:
                tmp.next[key] = Node(key)
            tmp = tmp.next[key]
            if tmp.eos:
                return False
            tmp.size += 1

        tmp.eos = True
        return True


class Node:
    def __init__(self, key):
        self.key = key
        self.eos = False
        self.size = 0
        self.next = {}

Q = int(input().strip())


for _ in range(Q):
    N = int(input().strip())
    lst = []
    A = Trie()

    for _ in range(N):
        lst.append(input().strip())
    lst.sort(key=lambda x: len(x))
    res = 1
    for i in lst:
        if not A.insert(i):
            res = 0
            break
    if res:
        print("YES")
    else:
        print("NO")


