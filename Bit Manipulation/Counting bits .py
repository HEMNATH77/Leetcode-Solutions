def Counting_bits(a):
  result = [0] * (a+1)
  for i in range(1, a+1):
    result[i] = result[i >> 1] + ( i & 1)
  return result
a = 2
print(Counting_bits(a)):
  
