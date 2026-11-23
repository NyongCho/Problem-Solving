N = int(input())

ingres = list(map(int, input().split()))

for i in range(1, N):
    if ingres[i] < ingres[i-1]:
        ingres[i] = ingres[i-1]

V = sum(ingres)

if V % 3 == 0:
    print("Delicious!")
else:
    print("Oh My God!")