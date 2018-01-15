# Time:  O(n)
# Space: O(1)
#
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
#

class Solution(object):
    def findCelebrity(self, n):
        res = 0
        # Find the candidate.
        for i in range(1, n):
            if knows(res, i):
                res = i
        # Verify the candidate.
        for i in range(n):
            if (i != res and knows(res, i)) or (not knows(i, res)):
                return -1
        return res
