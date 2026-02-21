def solve():
    n = int(input())
    a = list(map(int , input().split()))
    # create a dp of len n*n with dp[i][i] = a[i]
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]
    # ran a 2 for loops from i --> 1 to n-1 & then j = 1 to i+j
    # dp[j][j+i] = max(a[j] - dp[j+1][j+i], a[j+i] - dp[j][j+i-1])
    for i in range(1,n):
        for j in range(n-i):
            dp[j][j+i] = max(a[j] - dp[j+1][j+i], a[j+i] - dp[j][j+i-1])
    
    sum = 0
    for i in range(n):
        sum += a[i]
    ans = (dp[0][n-1] + sum)//2
    print(ans)

if __name__ == "__main__":
    solve()
