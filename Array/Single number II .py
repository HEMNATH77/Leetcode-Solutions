def single_number2(a):
    one = 0
    two = 0

    for i in a:
        one ^= i & ~two
        two ^= i & ~one
    return one

a = [0,1,0,1,0,1,99]
print(single_number2(a))