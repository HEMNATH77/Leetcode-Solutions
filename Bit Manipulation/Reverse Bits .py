def reverse(a):
    result = 0
    for i in range(32):
        b = a & 1
        result = (result << 1) + b
        a >>= 1
    return result
a = int('1011')
print(reverse(a))
