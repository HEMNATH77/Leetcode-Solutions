s = input("Enter a string romans : ")
r ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

total = 0
previous =  0

for i in s[::-1]:
    value = r[i]
    if value < previous:
        total -= value
    else:
        total += value
    previous = value
print(total)






