class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g = defaultdict(list)

        courses = prerequisites

        unvisited = 0
        visiting = 1
        visited = 2

        states = [unvisited] * numCourses

        for a, b in courses:
            g[a].append(b)

        def dfs(node):
            
            state = states[node]

            if state == visited:
                return True
            if state == visiting:
                return False
            
            states[node] = visiting

            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node] = visited
            return True




        
        for i in range(numCourses):
            if not dfs(i):
                return False

        

        return True

        



        