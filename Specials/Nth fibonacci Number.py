def Nth_fibonacci_number(n):
  if n == 1:
    return [0]
  dp = [0]*n
  dp[0] = 0
  dp[1] = 1
  for i in range(2,n):
    dp[i] = dp[i -1] + dp[i-2]
  return dp

n = 5
print(Nth_fibonacci_number(n))
