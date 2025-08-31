def median_arrays(a,b):
    n = len(a)
    m = len(b)

    i = 0
    j = 0

    m1 = -1
    m2 = -1

    c = m + n
    d = c // 2

    for f in range(d + 1):
        m2 = m1

        if i != n and j != m:
            if a[i] > b[j]:
                m1 = b[j]
                j += 1
            else:
                m1  = a[i]
                i += 1
        elif i < n:
            m1 = a[i]
            i += 1
        else:
            m1 = b[j]
            j += 1

    if c % 2 == 1:
        return (m1+m2)/2.0
    else:
        return float(m1)

a =[3,5,6,12,15]
b =[3, 4, 6, 10, 10, 12]
print(median_arrays(a,b))
