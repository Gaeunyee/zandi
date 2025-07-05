import sys
from math import ceil, log
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.top = Node('')

    def insert(self, trace):
        t = self.top
        for i in trace:
            if i not in t.child:
                t.child[i] = Node(i)
            t = t.child[i]


class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}


def dfs(t, d):
    print('-' * (d * 2) + t.key)
    for n, node in sorted(t.child.items()):
        dfs(node, d+1)

N = int(input().strip())
trie = Trie()
for _ in range(N):
    n, *c = input().split()
    trie.insert(c)

for n, node in sorted(trie.top.child.items()):
    dfs(node, 0)

