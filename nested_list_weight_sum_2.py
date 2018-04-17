###--------------------inverse weighted sum--------------------###
def inverseDepthSum(nested_list):
    weighted, unweighted = 0, 0
    while nested_list:
        next_level = []
        for n in nested_list:
            if n.isInteger():
                unweighted += n.getInteger()
            else:
                next_level += n.getList()
        weighted += unweighted
        nested_list = next_level
    return weighted

###recursion   
def InversedepthSum2(nested_list):
        res = []
        for n in nested_list:
            InversedepthSum2Recu(n, 0, res)
        sumi = 0
        for i in reversed(range(len(res))):
            sumi += res[i] * (len(res) - i)
        return sumi
def InversedepthSum2Recu(ls, depth, res):
    if len(res) < depth + 1:
        res.append(0)
    if ls.isInteger():
        res[depth] += ls.getInteger()
    else:
        for l in ls.getList():
            InversedepthSum2Recu(l, depth + 1)
