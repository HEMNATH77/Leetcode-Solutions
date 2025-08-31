def gray_code(n):
  res = []
  for  i in range(1 << n):
    gray = i ^ (i >> 1)
    res.append(gray)
  return res

n = 2
print(gray_code(n))


#output : [0,1,3,2]
