def reverse_words(s):
  a = s.split()
  n = len(a)
  new =[]
  for i in range(n -1,-1,-1):
    new.append(a[i])
  return ' '.join(new)  
