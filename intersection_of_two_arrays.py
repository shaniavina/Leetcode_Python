class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = []
        it1, it2 = 0, 0
        
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                if not res or res[-1] != nums1[it1]:
                    res.append(nums1[it1])
                it1 += 1
                it2 += 1
                
        
        return res

    ####second

        set1  = set(nums1)
        set2  = set(nums2)
        res = set1.intersection(set2)
        res = list(res)
        return res

    ######hash table
            lookup = {}
        
        for num in nums1:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
        
        result = []
        for num in nums2:
            if num in lookup and lookup[num] > 0:
                result.append(num)
                lookup[num] = 0
        return result
