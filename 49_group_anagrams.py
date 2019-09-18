class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in dic:
                dic.get(key).append(word)
            else:
                dic[key] = [word]
        return dic.values()
