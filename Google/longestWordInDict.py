def longestWordFromDic(dict, characters):
    counter = {}
    count = 0
    for char in characters:
        count += 1
        if char not in counter:
            counter[char] = 0
        counter[char] += 1

    dict = sorted(dict, key=len, reverse=True)
    for word in dict:
        if len(word) <= count:
            flag = True
            parse = {}
            for char in word:
                if char not in parse:
                    parse[char] = 0
                parse[char] += 1
            for char in parse:
                if char not in counter or parse[char] != counter[char]:
                    flag = False
                    continue
            if flag == True:
                return word

    return False

print(longestWordFromDic(['apple', 'ball','bally', 'zoo', 'cat', 'a', 'b', 'c'], "random"))
