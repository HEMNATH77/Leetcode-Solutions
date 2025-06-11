def Highest_Altitude(gain):
    n = len(gain)
    maximum = 0
    current = 0
    for i in range(0,n):
        current = current + gain[i]
        maximum = max(maximum,current)
    return maximum

gain = [-5,1,5,0,-7]
print(Highest_Altitude(gain))