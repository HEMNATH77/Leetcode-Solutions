def non_repeating(s):

  freq = {}
  for i in s:
    freq[i] = freq.get(i,0)+1
  for i in s:
    if freq[i] == 1:
      return i
  return '$'

s = "geeksforgeeks"
print(non_repeating(s))

# output = f
