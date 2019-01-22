
def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    stack = []
    sign = 1
    res = 0
    i = 0
    n = len(s)
    while i < n:
        print("res", res)
        print(stack)
        c = s[i]
        if c.isdigit():
            k = ""
            while i < n and s[i].isdigit():
                k += s[i]
                i += 1
            i -= 1
            print(k)
            res += sign * int(k)
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == '+':
            sign = 1
        elif s[i] == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif s[i] == ')':
            prevsign = stack.pop()
            prevres = stack.pop()
            res = (prevsign*res) + prevres
        i += 1
    return res

print(calculate("2-(0+0+7)"))
#print(calculate("5+3-4-(1+2-7+(10-1+3+5+(3-0+(8-(3+(8-(10-(6-10-8-7+(0+0+7)-10+5-3-2+(9+0+(7+(2-(2-(9)-2+5+4+2+(2+9+1+5+5-8-9-2-9+1+0)-(5-(9)-(0-(7+9)+(10+(6-4+6))+0-2+(10+7+(8+(7-(8-(3)+(2)+(10-6+10-(2)-7-(2)+(3+(8))+(1-3-8)+6-(4+1)+(6))+6-(1)-(10+(4)+(8)+(5+(0))+(3-(6))-(9)-(4)+(2))))))-1)))+(9+6)+(0))))+3-(1))+(7))))))))"))
