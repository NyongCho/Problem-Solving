_ = int(input())
arr = list(map(int, input().split()))
pre = arr[0]
ans = 1
for e in arr[1:]:
    if pre >= e:
        ans = 0
        break

    pre = e

print(ans)