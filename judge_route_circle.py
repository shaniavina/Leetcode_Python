class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c = collections.Counter(moves)
        return c['R'] == c['L'] and c['U'] == c['D']
