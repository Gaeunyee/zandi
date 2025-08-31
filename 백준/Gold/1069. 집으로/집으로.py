import sys
input = sys.stdin.readline

X, Y, D, T = map(int, input().split())
d = (X**2 + Y**2)**(1/2)
t = (d//D)*T
diff = (d//D)*D

if D < T:
    t = d
elif t > 0:
    t += min(T, abs(d-diff))
else:
    t = min(d, abs(d-D)+T, 2*T)
print(t)