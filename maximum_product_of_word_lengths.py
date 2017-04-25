class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key = lambda x:len(x), reverse = True)
        bits = [0] * len(words)
        for i, word in enumerate(words):
            for c in word:
                bits[i] |= (1 << (ord(c) - ord('a')))
        max_product = 0
        for i in range(len(words) - 1):
            if len(words[i]) ** 2 <= max_product:
                break
            for j in range(i + 1, len(words)):
                if len(words[i]) * len(words[j]) <= max_product:
                    break
                if not (bits[i] & bits[j]):
                    max_product = len(words[i]) * len(words[j])
        return max_product
