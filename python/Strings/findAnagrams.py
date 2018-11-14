# Find position of all anagrams of p in s

MAX = 256

def findAnagrams(s, p):
    result = []
    countP = [0] * MAX
    countS = [0] * MAX

    for i in range(len(p)):
        print(ord(p[i]), ord(s[i]))
        countP[ord(p[i])] += 1
        countS[ord(s[i])] += 1

    n = len(s)
    m = len(p)

    for i in range(n-m+1):
        if i > 0:
            countS[ord(s[i-1])] -= 1
            countS[ord(s[i+m-1])] += 1
        if countP == countS:
            result.append(i)

    return result

txt = "BACDGABCDA"
pat = "ABCD"
print(findAnagrams(txt, pat))
