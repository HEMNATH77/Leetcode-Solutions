#Define two integers as follows:
# num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
# num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
# Return the integer num1 - num2.

def divisibility(m,n):
    a = []
    b = []

    for i in range(1,n + 1):
        if i % m == 0:
            b.append(i)
        else:
            a.append(i)
    return sum(a) - sum(b)

n = 10
m = 3
print(divisibility(m,n))