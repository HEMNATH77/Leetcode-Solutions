from collections import deque


def letter_combination(a):
    if not a:
        return []

    phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    queue = deque([''])

    for i in a:
        letter = phone[i]

        for j in range(len(queue)):
            combine = queue.popleft()

            for k in letter:
                queue.append(combine + k)
    return list(queue)

a = '24'
print(letter_combination(a))