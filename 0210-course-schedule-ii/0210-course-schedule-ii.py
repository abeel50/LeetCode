class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Map each course with it's prerequisites
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # keep track detection of cycle
        # keep track of visited courses
        visited, cycle = set(), set()
        
        res = []
        
        # Recursive DFS
        def dfs(course):
            #if there's cycle i.e. [1,0],[0,1]
            if course in cycle:
                return False
            
            # if course is already done
            if course in visited:
                return True
            
            cycle.add(course)
            
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visited.add(course)
            cycle.remove(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course): return []
            
        return res
        