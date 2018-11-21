'''
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]
Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
'''
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        incr = 0
        decr = 0

        for i in range(1, len(A)):
            if A[i-1] < A[i] and decr == 0:
                incr += 1
            elif A[i-1] > A[i] and incr != 0:
                decr += 1
            else:
                return False
        if decr == 0 or incr == 0:
            return False
        return True
