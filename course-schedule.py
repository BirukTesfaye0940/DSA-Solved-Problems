from ast import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visistedNode = set()

        for cor, pre in prerequisites:
            preMap[cor].append(pre)
        
        def dfs(crs):
            if crs in visistedNode:
                return False
            if preMap[crs] == []:
                return True
            
            visistedNode.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visistedNode.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

            