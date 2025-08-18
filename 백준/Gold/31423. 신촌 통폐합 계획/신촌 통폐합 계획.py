import sys
input = sys.stdin.readline
INF = 10**6

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class Link:
    def __init__(self):
        self.start = None
        self.end = None

    def append(self, link):
        if self.start == None:
            self.start = link.start
            self.end = link.end
        else:
            self.end.next = link.start
            self.end = link.end

N = int(input())
lst = [Link() for _ in range(N+1)]

for i in range(1, N+1):
    k = input().strip()
    n = Node(k)
    lst[i].start = n
    lst[i].end = n

for i in range(N-1):
    a, b = map(int, input().split())
    lst[a].append(lst[b])
    lst[b] = Link()

for i in range(1, N+1):
    if lst[i].start:
        t = lst[i].start
        while t:
            print(t.key, end='')
            t = t.next

