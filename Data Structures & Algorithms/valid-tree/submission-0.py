class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n-1):
            return False

        adj = defaultdict(set)

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        visit = set()

        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
        