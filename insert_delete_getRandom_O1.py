from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []
        self.map = {}  ###cuz we need constant time, so we set up hash table

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        self.set.append(val)
        self.map[val] = len(self.set) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        
        self.map[self.set[-1]] = self.map[val]    ###to ensure the constant time of deleting from list, put it in the end of list
        self.set[self.map[val]], self.set[-1] = self.set[-1], self.set[self.map[val]]
        
        self.map.pop(val)    ###delete the last element from a hash table
        self.set.pop()
        
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.set[randint(0, len(self.set) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
