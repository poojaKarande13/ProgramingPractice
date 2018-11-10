import unittest

# def change_possibilities(n, S):
#     # We need n+1 rows as the table is constructed
#     # in bottom up manner using the base case 0 value
#     # case (n = 0)
#     m = len(S)
#     table = [[0 for x in range(m)] for x in range(n+1)]
#
#     # Fill the entries for 0 value case (n = 0)
#     for i in range(m):
#         table[0][i] = 1
#
#     # Fill rest of the table entries in bottom up manner
#     for i in range(1, n+1):
#         for j in range(m):
#
#             # Count of solutions including S[j]
#             x = table[i - S[j]][j] if i-S[j] >= 0 else 0
#
#             # Count of solutions excluding S[j]
#             y = table[i][j-1] if j >= 1 else 0
#
#             # total count
#             table[i][j] = x + y
#
#     return table[n][m-1]

def change_possibilities(amount, denominations):
    if len(denominations) == 0:
        return 0
    table = [[0 for j in range(len(denominations))] for i in range(amount + 1)]

    for j in range(len(denominations)):
        table[0][j] = 1

    for j in range(len(denominations)):
        for i in range(1, amount + 1):
            x = table[(i - denominations[j])][j] if (i - denominations[j]) >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y

    return table[amount][len(denominations)-1]

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
