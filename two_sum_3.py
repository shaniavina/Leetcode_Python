class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = collections.defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.lookup[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.lookup:
            num = value - key
            if num in self.lookup and (self.lookup[num] > 1 or num != key):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
