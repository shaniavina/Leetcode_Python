from random import randint
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []
        self.map = collections.defaultdict(list)  

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        
        self.set.append(val)
        self.map[val].append(len(self.set) - 1)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        
        self.map[self.set[-1]][-1] = self.map[val][-1]   
        self.set[self.map[val][-1]], self.set[-1] = self.set[-1], self.set[self.map[val][-1]]
        
        self.map[val].pop() 
        if not self.map[val]:   ####delete the 'val' key in the hash table if there is no other element in there
            self.map.pop(val)
        self.set.pop()
        
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        return self.set[randint(0, len(self.set) - 1)]  ####BUG BUG HERE! dont know why


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
