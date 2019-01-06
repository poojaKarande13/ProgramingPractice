'''
Given a string s contains lowercase alphabet, find the length of the Longest common Prefix of all substrings in O(n)

s = 'ababac'

Then substrings are as follow:

1: s(1, 6) = ababac
2: s(2, 6) = babac
3: s(3, 6) = abac
4: s(4, 6) = bac
5: s(5, 6) = ac
6: s(6, 6) = c

Now, The lengths of LCP of all substrings are as follow

1: len(LCP(s(1, 6), s)) = 6
2: len(LCP(s(2, 6), s)) = 0
3: len(LCP(s(3, 6), s)) = 3
4: len(LCP(s(4, 6), s)) = 0
5: len(LCP(s(5, 6), s)) = 1
6: len(LCP(s(6, 6), s)) = 0

String contains only lowercase alphabates.
'''
def LCP(s):
    for i in range(0, len(s)):
        
