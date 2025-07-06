import sys
input = sys.stdin.readline

INF = 10**5
txt = input().strip()
N = int(input().strip())
dp = [INF]*(len(txt)+1)
dp[-1] = 0
word = []
for _ in range(N):
    word.append(input().strip())


def makeData(string):
    d = [0]*26
    for i in string:
        d[ord(i)-97] += 1
    return d


def eq(d1, d2, st):
    for i in range(26):
        if d1[i]-st[i] != d2[i]:
            return False
    return True


def score(word, idx):
    s = 0
    for i in range(len(word)):
        if word[i] != txt[idx+i]:
            s += 1
    return s


word_data = [makeData(word[i]) for i in range(N)]
txt_data = [makeData(txt[:i]) for i in range(1, len(txt)+1)]
txt_data.append([0]*26)
for i in range(len(txt)):
    for w in range(N):
        if i+1 < len(word[w]):
            continue
        if eq(txt_data[i], word_data[w], txt_data[i-len(word[w])]):
            dp[i] = min(dp[i], dp[i-len(word[w])] + score(word[w], i-len(word[w])+1))


print(dp[len(txt)-1] if dp[len(txt)-1] != INF else -1)

