def zigzag(s,n):
    if n == 1 or n >= len(s):
        return s
    row = [""] * n
    a  = 0
    b  = 1
    for i in s:
        row[a] += i
        if a == 0:
            b = 1
        elif a == n-1:
            b = -1
        a = a+b
    return "".join(row)

s = "Paybypaytm"
n = 3
print(zigzag(s,n))
