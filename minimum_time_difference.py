class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        minutes = map(convert, timePoints)
        minutes.sort()
        
        return min((y - x) % (24 * 60) for x, y in zip(minutes, minutes[1:] + minutes[:1]))
        
        ##The required minimum difference must be a difference between two adjacent elements in the circular array (so the last element is "adjacent" to the first.)
