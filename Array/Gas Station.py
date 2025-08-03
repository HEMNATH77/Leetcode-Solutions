def gas_station(gas,cost):
    n = len(gas)

    total = 0
    current = 0
    start = 0

    for i  in range(n):
        total = total + gas[i] - cost[i]
        current = total + gas[i] - cost[i]

        if current < 0 :
            start = i + 1
            current = 0
    if total >= 0:
        return start
    else:
        return -1

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(gas_station(gas,cost))