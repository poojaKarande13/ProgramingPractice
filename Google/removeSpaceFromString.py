def removeSpace(a):
    a = a.strip()

    flag = False
    b = ''
    for i in range(len(a)):
        if a[i] != ' ':
            flag = False
            b += a[i]
        else:
            if flag == False:
                b += a[i]
                flag = True
        i += 1

    return b

def removeSpaceEff(a):
    a = a.strip()
    i = 0
    

print(removeSpace("  pooja    kaar  ande  "))
