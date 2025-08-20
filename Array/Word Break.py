def word_break(s,word_dict):

    n = len(s)

    word_set = set(word_dict)

    dp = [False]*(n+1)
    dp[0] = True

    for i in range(1,n+1):
        for j in word_set:
            if len(j) <= i and dp[i - len(j)]:
                if s[i - len(j) : i] == j:
                    dp[i]  = True
                    break
    return dp[n]

s = "leetcode"
word_dict = ["leet","code"]
print(word_break(s,word_dict))
