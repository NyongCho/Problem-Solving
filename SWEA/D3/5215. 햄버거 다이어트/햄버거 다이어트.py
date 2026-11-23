def main():
    T = int(input())

    for t in range(T):
        N, L = map(int, input().split())
        info = []

        for _ in range(N):
            score, kcal = map(int, input().split())
            info.append((score, kcal))

        dp = [0 for _ in range(L+1)]

        for s, k in info:
            for i in range(L, k-1, -1):
                if i - k >=0:
                    dp[i] = max(dp[i], dp[i - k] + s)

        print(f'#{t+1} {dp[L]}')


if __name__ == "__main__":
    main()