import sys
input = sys.stdin.readline

l = input().strip()
lib = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
st = []
res = 0
i = 0
while i < len(l):
    if l[i:i+2] in lib:
        i += 1
    elif l[i:i+3] == 'dz=':
        i += 2
    res += 1
    i += 1
print(res)

