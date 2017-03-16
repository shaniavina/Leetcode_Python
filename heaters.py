class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        min_radius = 0
        
        for house in houses:
            house_index = bisect.bisect_left(heaters, house)
            curr_radius = float('inf')
            if house_index != len(heaters):
                curr_radius = heaters[house_index] - house
            if house_index != 0:
                smaller = house_index - 1
                curr_radius = min(curr_radius, house - heaters[smaller])
            min_radius = max(min_radius, curr_radius)
        return min_radius
        
