# Time:  push:    O(1)
#        pop:     O(n), there is no built-in SortedDict in python. If applied, it could be reduced to O(logn)
#        popMax:  O(n)
#        top:     O(1)
#        peekMax: O(1)
# Space: O(n), n is the number of values in the current stack
class maxStack(object):
    def __init__(self):
        self.stk = []
        self.maxStk = []
    def push(self, x):
        self.stk.append(x)
        if not self.maxStk:
            self.maxStk.append(x)
        else:
            self.maxStk.append(max(x, self.maxStk[-1]))
    def pop(self):
        self.maxStk.pop()
        return self.stk.pop()
    def peekMax(self):
        return self.maxStk[-1]
    def popMax(self):
        n = self.maxStk.pop()
        tmp = []
        while n!= self.stk[-1]:
            tmp.append(self.stk.pop())
        res = self.stk.pop()
        for i in reversed(range(len(tmp))):
            self.stk.push(tmp[i])
        return res
