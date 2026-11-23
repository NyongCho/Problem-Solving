N = int(input())

ingres = list(map(int, input().split()))

s = ingres[0]
m = ingres[0]

for i in range(1, N):
    if ingres[i] > m:
        m = ingres[i]
    s += m

if s % 3 == 0:
    print("Delicious!")
else:
    print("Oh My God!")