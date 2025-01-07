import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)


class Trie:
    def __init__(self):
        self.top = Node('')

    def find(self, string):
        ret = [0]
        tmp = self.top
        for key in string:
            if key not in tmp.next:
                break
            tmp = tmp.next[key]
            ret.append(tmp.size)
        return ret

    def insert(self, string):
        tmp = self.top
        for key in string:
            if key not in tmp.next:
                tmp.next[key] = Node(key)
            tmp = tmp.next[key]
            tmp.size += 1

        tmp.eos = True

    def delete(self, string):
        tmp = self.top
        for key in string:
            tmp = tmp.next[key]
            tmp.size -= 1

        tmp.eos = True


class Node:
    def __init__(self, key):
        self.key = key
        self.eos = False
        self.size = 0
        self.next = {}

Q = int(input().strip())
A = Trie()
B = Trie()

for _ in range(Q):
    C, *word = input().split()
    if C == 'add':
        if word[0] == 'A':
            A.insert(word[1])
        if word[0] == 'B':
            B.insert(reversed(word[1]))
    elif C == 'delete':
        if word[0] == 'A':
            A.delete(word[1])
        if word[0] == 'B':
            B.delete(reversed(word[1]))
    else:
        l = len(word[0])
        a = A.find(word[0])
        b = B.find(reversed(word[0]))
        size_a = len(a) - 1
        size_b = len(b) - 1
        res = 0
        i = min(l-1, size_a)
        j = l-i
        while i >= 1 and 1 <= j <= size_b:
            res += a[i]*b[j]
            i -= 1
            j += 1
        print(res)


