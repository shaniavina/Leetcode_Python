class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            ls = tuple(sorted(str))
            if ls not in dic:
                dic[ls] = []
            dic[ls].append(str)
        res = []
        for group in dic.values():
            res.append(group)
        return res
