class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda (h, k):(-h, k))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
