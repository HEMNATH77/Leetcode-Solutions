def single_number(a):
    result = 0
    for i in a:
        result ^= i
    return result
a =[1,2,2]
print(single_number(a))