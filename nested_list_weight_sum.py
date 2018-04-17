# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

###--------------weighted sum------------------###
def depthSum(nested_list):
    if not nested_list:
        return 0
    res, depth = 0, 1
    while nested_list:
        next_level = []
        for n in nested_list:
            if n.isInteger():
                res += depth * n.getInteger()
            else:
                next_level += n.getList()
        depth += 1
        nested_list = next_level
    return res

###recursion
def depthSum2(nested_list):
    return depthSum2Recu(1, nested_list)
def depthSum2Recu(depth, nested_list):
    res = 0
    for n in nested_list:
        if n.isInteger():
            res += depth * n.getInteger()
        else:
            res += depthSum2Recu(depth + 1, n.getList())
    return res
