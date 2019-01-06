'''Can you write code in Java or C++ to find the power set of a given set?
For example if S={a,b} the power set is P={{},{a},{b},{a,b}}
a,b,c
{}, {a}, {b}, {a,b}, {c}, {a, c}, {b, c}, {a,b,c}
( you can also choose any of your favorite programming language)'''

def powerSet(S):
    res  = [set()]

    for elem in S: # a, b, c
        newSet = []
        for index in range(len(res)):
            newSet.append(res[index].union(elem))
        res = res + newSet

    print(res)

powerSet(['a', 'b', 'c'])
