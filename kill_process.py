class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        child = collections.defaultdict(list)
        for i in range(len(pid)):
            if ppid[i]:
                child[ppid[i]].append(pid[i])
        
        res, stk = [], [kill]
        while stk:
            tmp = stk.pop()
            res.append(tmp)
            stk.extend(child[tmp])
        return res
            
