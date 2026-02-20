def solve():
    n = int(input())
    a = list(map(int, input().split()))

    totalSum = sum(a)

    dp = [[False] * (totalSum + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    if a[0] <= totalSum:
        dp[0][a[0]] = True

    for i in range(1, n):
        for j in range(totalSum + 1):
            dp[i][j] = dp[i-1][j]

            if j >= a[i] and dp[i-1][j - a[i]]:
                dp[i][j] = True

    for j in range(1, totalSum + 1):
        if dp[n-1][j]:
            print(j, end=" ")


if __name__ == "__main__":
    solve()
