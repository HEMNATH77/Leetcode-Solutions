def longest_palindrome(s):
    freq = {}

    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    length = 0
    odd = False

    for j in freq.values():
        if j % 2 == 0:
            length += j
        else:
            length += j-1
            odd =True
    if odd:
        length += 1
    return length

s = "geeks"
print(longest_palindrome(s))
