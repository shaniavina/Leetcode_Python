class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.A.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        return self.A.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.A) == 0 and len(self.B) == 0

    
