def maximum_product(a):

    if not a:
        return 0

    max_prod = min_prod = result = a[0]

    for i in a[1:]:

        if i < 0:
            max_prod,min_prod = min_prod,max_prod

        max_prod = max(i , i * max_prod)
        min_prod = min(i , i * min_prod)

        result = max(result,max_prod)

    return result

a = [2,3,-2,4]
print(maximum_product(a))