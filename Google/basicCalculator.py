
def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    stack = [] # 2 , -1,  2
    res = 0
    sign  = 1
    i = 0

    cur = 0

    for i in range(len(s)):
        # num
        if s[i] in ['0','1','2','3','4','5','6','7','8','9']:
            cur = cur * 10 + int(s[i])
        else:
            if cur != 0:
                stack.append(sign * cur)
                sign = sign & 1
            cur = 0
            if s[i] == '-':
                sign  = -1
            elif s[i] == '(':
                if sign == -1:
                    stack.append('-')
                stack.append('(')
                sign &= 1
            elif s[i] == ')':
                inter = 0
                print(stack)
                while stack[-1] != '(':
                    inter += stack.pop()
                stack.pop()

                if stack and stack[-1] == '-':
                    stack.pop()
                    stack.append(-1 * inter)
                else:
                    stack.append(inter)

    if cur != 0:
        stack.append(sign * cur)
        sign = sign & 1
    print(stack)
    while len(stack) > 0:
        res += stack.pop()

    return res

print(calculate("2-(0+0+7)"))
#print(calculate("5+3-4-(1+2-7+(10-1+3+5+(3-0+(8-(3+(8-(10-(6-10-8-7+(0+0+7)-10+5-3-2+(9+0+(7+(2-(2-(9)-2+5+4+2+(2+9+1+5+5-8-9-2-9+1+0)-(5-(9)-(0-(7+9)+(10+(6-4+6))+0-2+(10+7+(8+(7-(8-(3)+(2)+(10-6+10-(2)-7-(2)+(3+(8))+(1-3-8)+6-(4+1)+(6))+6-(1)-(10+(4)+(8)+(5+(0))+(3-(6))-(9)-(4)+(2))))))-1)))+(9+6)+(0))))+3-(1))+(7))))))))"))
