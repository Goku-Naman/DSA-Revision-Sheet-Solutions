def solve():
    n = int(input())
    a = list(range(1, n+1))
    MOD = 10**9 + 7
    tar = 0 
    for i in range(n):
        tar += a[i]; 
    if(tar%2 == 1):
        print(-1)
    tar = tar // 2 
    dp = [0]*(tar+1)
    dp[0] = 1
    
    for i in range(1,n):
        for j in range(tar,i-1,-1):
            dp[j] += dp[j-i]
    
    print(dp[tar])

if __name__ == "__main__":
    solve()
