```
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
```
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visit = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(node):
            if visit[node] == -1:
                return False # cycle
            visit[node] = -1
            for dep in graph[node]:
                if visit[dep] != 1:
                    if dfs(dep) == False:
                        return False
            visit[node] = 0
            return True

        for i in range(numCourses):
            if visit[i] != 1:
                if dfs(i) == False:
                   return False
                visit[i] = 1
        return True
