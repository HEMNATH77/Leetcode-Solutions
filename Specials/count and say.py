from itertools import count


def count_and_say(n):
    result =""

    for i in range(n):
        current = ""
        i = 0

        while i < len(result):
            count = 1
            while i+1 < len(result) and result[i] == result[i+1]:
                count += 1
                i += 1
            current += str(count) + result[i]
        result = current
        i += 1
    return result

n = 4
print(count_and_say(n))
