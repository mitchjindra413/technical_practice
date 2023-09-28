class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        memo = {}
        
        def explore(index):
            if index in memo: return memo[index]
            if index == len(graph) - 1: return [[index]]
            
            res = []
            
            for i in graph[index]:
                route = explore(i)
                for r in route:
                    res.append([index] + r)
                    
            memo[index] = res
            return res
        
        return explore(0)