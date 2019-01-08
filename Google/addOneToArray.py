# given a array of integers from 0 to 9
# for one integer and add one to it
# store the result in the orginal form
# example [1,2,3] -> [1,2,4]

def add_one(given_array):
    carry = 1
    N = len(given_array)
    result = [0 for i in range(N)]

    for i in range(N-1, -1, -1):
        elem = int(given_array[i])
        elem = (elem + carry)
        if elem > 9:
            carry = 1
            elem -= 10
        else:
            carry = 0
        result[i] = elem

    if carry == 1:
        result = [1] + result

    return result

print(add_one([1,2,3]))
print(add_one([1,2,9]))
print(add_one([9,9,9]))
