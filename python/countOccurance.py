# Write code to find out a number of occurrence of a number in a sorted array ? 
# O(n)
def countOccurrence(my_list, num):
    count = 0
    for elem in my_list:
        if elem == num:
            count += 1
    return map

print(countOccurrence([1,1,1,1,2,2,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,5,5], 5))
