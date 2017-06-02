class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.A.append(x)
        for i in range(len(self.A) - 1):
            self.A.append(self.A.popleft())
            

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.A.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.A[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.A) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
