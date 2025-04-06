import sys
from collections import deque
input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.top = Node()
        self.idx = [0, 2, 6, 19]

    def insert(self, string):
        tmp = self.top
        for key in string:
            if not tmp.next[key]:
                tmp.next[key] = Node(key)
            tmp = tmp.next[key]
        tmp.eos = True

    def trav(self, string):
        tmp = self.top
        ret = 0
        for key in string:
            key = ord(key)-65
            if tmp.next[key]:
                tmp = tmp.next[key]
            else:
                while not tmp.next[key]:
                    if tmp == self.top:
                        break
                    tmp = tmp.fail
                if tmp.next[key]:
                    tmp = tmp.next[key]
            if tmp.eos:
                ret += 1
        return ret

    def setFail(self):
        qu = deque()
        qu.append(self.top)
        self.top.fail = self.top
        while qu:
            tmp = qu.popleft()
            for i in self.idx:
                nxt = tmp.next[i]
                if not nxt:
                    continue
                tr = tmp.fail
                if tmp == self.top:
                    nxt.fail = self.top
                    qu.append(nxt)
                    continue
                while not tr.next[nxt.key]:
                    if tr == self.top:
                        break
                    tr = tr.fail
                if tr.next[nxt.key]:
                    nxt.fail = tr.next[nxt.key]
                else:
                    nxt.fail = tr
                if nxt.fail.eos:
                    nxt.eos = True
                qu.append(nxt)


class Node:
    def __init__(self, key=''):
        self.key = key
        self.eos = False
        self.next = [0]*20
        self.fail = None


T = int(input().strip())


def solve():
    N, M = map(int, input().split())
    trie = Trie()
    dna = input().strip()
    marker = input().strip()
    marker = list(map(lambda x: ord(x)-65, marker))
    trie.insert(marker)
    for i in range(M-1):
        for j in range(i+1, M):
            trie.insert(marker[:i] + marker[i:j+1][::-1] + marker[j+1:])

    trie.setFail()
    print(trie.trav(dna))


for _ in range(T):
    solve()
