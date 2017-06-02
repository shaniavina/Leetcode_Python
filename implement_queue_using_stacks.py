class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []  ####use two stacks

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
        if not self.B:
            for i in range(len(self.A)):
                self.B.append(self.A.pop())
        return self.B.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.B:
            for i in range(len(self.A)):
                self.B.append(self.A.pop())
        return self.B[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.A) == 0 and len(self.B) == 0

    
