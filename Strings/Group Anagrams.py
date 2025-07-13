def group_anagrams(s):
    anagram = {}

    for i in s:
        key = "".join(sorted(i))
        if key in anagram:
            anagram[key].append(i)
        else:
            anagram[key] = [i]
    return list(anagram.values())

s = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(s))