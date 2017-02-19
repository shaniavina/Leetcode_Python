class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort(), nums2.sort()
        res = []
        it1, it2 = 0, 0
        
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                res.append(nums1[it1])
                it1 += 1
                it2 +=1
        return res

    ##########second
    class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = {}
        count2 = {}
        res = []
        for i in range(len(nums1)):
            if nums1[i] in count1:
                count1[nums1[i]] += 1
            else:
                count1[nums1[i]] = 1
                
        for i in range(len(nums2)):
            if nums2[i] in count2:
                count2[nums2[i]] += 1
            else:
                count2[nums2[i]] = 1
        for key1 in count1:
            for key2 in count2:
                if key1 == key2:
                    min_count = min(count1[key1], count2[key2])
                    res.extend([key1] * min_count)
        return res
