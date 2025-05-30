def coin_change(amount,coins):
  if amount < 1:
    return amount
  dp = [amount + 1]*(amount+1)
  dp[0] = 0
  for i in range(1,amount + 1):
    for c in coins:
      if c <= i:
        dp[i] = min(dp[i],(dp[i - c] + 1)
  return -1 if dp[amount] > amount else  dp[amount]                  
