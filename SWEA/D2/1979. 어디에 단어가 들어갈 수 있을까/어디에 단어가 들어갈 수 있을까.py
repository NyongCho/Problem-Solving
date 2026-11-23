def check_4_way(M:list, i:int, j:int):
    ways = []
    if (i-1 >= 0 and M[i-1][j] == 0) or i == 0:
        cnt = 1
        xi = i
        while (xi + 1 < len(M) and M[xi + 1][j] == 1):
            xi += 1
            cnt += 1

        if cnt > 1:
            ways.append(cnt)

    if (j-1 >= 0 and M[i][j-1] == 0) or j == 0:
        cnt = 1
        xj = j
        while (xj + 1 < len(M) and M[i][xj+1] == 1):
            xj += 1
            cnt += 1

        if cnt > 1:
            ways.append(cnt)

    return ways


def main():
    T = int(input())

    for t in range(T):
        N, K = map(int, input().split())
        M = [list(map(int, input().split())) for _ in range(N)]
        ans = [ 0 for _ in range(N+1)]

        for i in range(N):
            for j in range(N):
                # print(i ,j, M[i][j] ,check_4_way(M, i, j))
                if M[i][j] == 1:
                    ways = check_4_way(M, i, j)

                    for way in ways:
                        ans[way] += 1

        print(f'#{t+1} {ans[K]}')

if __name__ == "__main__":
    main()