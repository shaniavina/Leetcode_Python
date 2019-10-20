import collections

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        frq = collections.defaultdict(list)
        for key, cnt in collections.Counter(words).items():
            frq[cnt].append(key)
        res = []
        for times in reversed(range(len(words) + 1)):
            frq[times] = sorted(frq[times]) ### in case of ['aaa', 'aa', 'a']
            res.extend(frq[times])
            
            if len(res) >= k:
                return res[:k]
        return res[:k]
