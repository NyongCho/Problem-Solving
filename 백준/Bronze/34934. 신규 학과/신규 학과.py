N = int(input())

dep, year = None, 0
for _ in range(N):
    d, y = input().split()
    y = int(y)

    if year < y:
        dep = d
        year = y

print(dep)