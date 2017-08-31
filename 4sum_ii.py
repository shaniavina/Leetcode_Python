class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # AB = collections.Counter(a+b for a in A for b in B)
        # return sum(AB[-c-d] for c in C for d in D)
        
        ###second
        lookup = {}
        for a in A:
            for b in B:
                if a+b in lookup:
                    lookup[a+b] += 1
                else:
                    lookup[a+b] = 1
        count = 0
        for c in C:
            for d in D:
                if -c-d in lookup:
                    count += lookup[-c-d]
        return count
