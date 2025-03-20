import sys
input = sys.stdin.readline


N = int(input().strip())

print('SK' if N%2 == 1 else 'CY')
