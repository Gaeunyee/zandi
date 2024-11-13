import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def round_two_decimal(num):
    scaled_num = num * 100

    if scaled_num - int(scaled_num) >= 0.5:
        result = int(scaled_num) + 1
    else:
        result = int(scaled_num)
    return result / 100


class Trie:
    def __init__(self):
        self.top = Node('')

    def insert(self, string):
        tmp = self.top
        for key in string:
            if key not in tmp.next:
                tmp.next[key] = Node(key)
                tmp.size += 1
            tmp = tmp.next[key]
        tmp.eos = True


def trav(node, d):
    global counter
    if node.eos:
        counter += d
    for n in node.next:
        if node.size > 1 or node.eos:
            trav(node.next[n], d+1)
        else:
            trav(node.next[n], d)


class Node:
    def __init__(self, key):
        self.key = key
        self.eos = False
        self.size = 0
        self.next = {}


while True:
    N = input().strip()
    if N == '':
        break
    dic = Trie()
    for _ in range(int(N)):
        s = input().strip()
        dic.insert(s)
    counter = 0
    if dic.top.size == 1:
        trav(dic.top, 1)
    else:
        trav(dic.top, 0)
    counter /= int(N)
    print(f'{round_two_decimal(counter):.2f}')
