import sys
from math import sqrt, ceil

input = sys.stdin.readline


N = int(input().strip())

def recursion(s, l, r):
    global c
    c += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(N):
    s = input().strip()
    c = 0
    print(isPalindrome(s), c)
    