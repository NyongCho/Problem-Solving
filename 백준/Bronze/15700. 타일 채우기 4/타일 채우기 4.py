import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if N % 2 == 1 and M % 2 == 1:
    print((N//2)*M + (M//2))
else:
    print((N*M)//2)