
def getString(my_string, subString, k, result):
    if len(subString) == k:
        result.append(subString)

    for i in range(len(my_string)):
        getString(my_string[:i]+my_string[i+1:],subString+my_string[i], k, result)


def subString(my_string, k):
    result = []
    getString(my_string,"", k, result)
    return result

print(subString("PoojaKarande", 4))
