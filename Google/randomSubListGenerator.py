# Question: Write a function that takes a list L and returns a random sublist of size N of that list. Assume that the indexes must be in increasing order. That is, you cannot go backwards.
#
# Example:
#
# L = [1, 2, 3, 4, 5]
# N = 3
#
# The function should return one of these lists:
#
# [1, 2, 3]
# [1, 2, 4]
# [1, 2, 5]
# [1, 3, 4]
# [1, 3, 5]
# [1, 4, 5]
# [2, 3, 4]
# [2, 3, 5]
# [2, 4, 5]
# [3, 4, 5]
import random
def randomSubListGenerator(L, N):
    M = len(L)
    if M == 0 or N == 0:
        return []

    i = random.randint(0, M-N)
    res = [L[i]]
    return res +  randomSubListGenerator(L[i+1:], N-1)

print(randomSubListGenerator([1, 2, 3, 4, 5], 3))
