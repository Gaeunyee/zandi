import sys
input = sys.stdin.readline

line = input().strip()
happy = 'HAPPY'
sad = "SAD"
h = 0
s = 0
for i in line:
    if i in happy:
        h += 1
    if i in sad:
        s += 1
def round_two_decimal(num):
    scaled_num = num * 100

    if scaled_num - int(scaled_num) >= 0.5:
        result = int(scaled_num) + 1
    else:
        result = int(scaled_num)
    return result / 100
if h == 0 and s == 0:
    print('50.00')
else:
    r = h*100/(h+s)
    print(f'{round_two_decimal(r):.2f}')
