def Tribonacci(n):
    if n < 1:
        return 0
    if n <= 2:
        return 1
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n+1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i -1]
    return dp[n]

n = 6
print(Tribonacci(n))