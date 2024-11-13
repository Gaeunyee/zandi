import sys
input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.top = Node('')

    def insert(self, string):
        tmp = self.top
        for key in string:
            if key == '1':
                tmp.size[1] += 1
            else:
                tmp.size[0] += 1
            if key not in tmp.next:
                tmp.next[key] = Node(key)
            tmp = tmp.next[key]
        tmp.eos = True

    def delete(self, string):
        tmp = self.top
        for key in string:
            if key == '1':
                tmp.size[1] -= 1
            else:
                tmp.size[0] -= 1
            tmp = tmp.next[key]

    def trav(self, string):
        tmp = self.top
        res = ""
        for key in string:
            if key == '1':
                if tmp.size[0] != 0:
                    tmp = tmp.next['0']
                    res += '1'
                else:
                    tmp = tmp.next['1']
                    res += '0'
            else:
                if tmp.size[1] != 0:
                    tmp = tmp.next['1']
                    res += '1'
                else:
                    tmp = tmp.next['0']
                    res += '0'
        return res



class Node:
    def __init__(self, key):
        self.key = key
        self.eos = False
        self.size = [0, 0]
        self.next = {}


M = int(input().strip())
trie = Trie()
trie.insert('0'*30)
for _ in range(M):
    c, x = map(int, input().split())
    if c == 1:
        trie.insert(str(bin(x))[2:].zfill(30))
    elif c == 2:
        trie.delete(str(bin(x))[2:].zfill(30))
    else:
        print(int(trie.trav(str(bin(x))[2:].zfill(30)), 2))

