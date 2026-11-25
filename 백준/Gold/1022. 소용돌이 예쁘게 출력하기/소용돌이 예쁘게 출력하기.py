import sys
output = sys.stdout.write

r1, c1, r2, c2 = map(int, input().strip().split())
# r1, c1, r2, c2 = -3, -3, 2, 0
m = max(abs(r1), abs(c1), abs(r2), abs(c2))
lr, lc = r2-r1+1, c2-c1+1

def value(r,c):
    k = max(abs(r), abs(c))
    big = (2*k+1)**2

    if k == r:
        return big - (k-c)
    elif -k == c:
        return big -(2*k) - (k-r)
    elif -k == r:
        return big -(4*k) - (k+c)
    return big -(6*k) - (k+r)

ans = [[0 for _ in range(lc)] for _ in range(lr)]

_max = 0
for i in range(lr):
    for j in range(lc):
        ans[i][j] = value(i+r1, j+c1)
        # print(i+r1, j+c1)
        _max = max(_max, ans[i][j])

cnt = 0
while _max > 0:
    _max //= 10
    cnt += 1

for i in range(lr):
    for j in range(lc):
        output(str(ans[i][j]).rjust(cnt, ' '))
        output(' ')
    output('\n')