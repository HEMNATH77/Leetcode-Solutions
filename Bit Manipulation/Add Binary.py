def add_binary(a,b):
    c = int(a,2)
    d = int(b,2)

    total = c + d
    result = bin(total)[2:]
    return result

a = '1010'
b = '1011'
print(add_binary(a,b))