import sys
input = sys.stdin.readline

line = input().strip()
dp = [0, 1] + [3000]*len(line)


def isPalin(l):
    for i in range(len(l)//2):
        if l[i] == l[len(l)-i-1]:
            continue
        else:
            return False
    return True


for i in range(1, len(line)):
    for j in range(i, -1, -1):
        if line[i] == line[j] and dp[j] + 1 < dp[i+1] and isPalin(line[j:i+1]):
            dp[i+1] = dp[j] + 1
print(dp[len(line)])



