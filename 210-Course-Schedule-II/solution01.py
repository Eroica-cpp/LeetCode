#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 13, 2015
# Question: 210-Course-Schedule-II
# Link:     https://leetcode.com/problems/course-schedule-ii/
# ==============================================================================
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# 
# Some courses may have prerequisites, for example to take course 0 you have 
# to first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return 
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. 
# If it is impossible to finish all courses, return an empty array.
# 
# For example:
# 
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have 
# finished course 0. So the correct course order is [0,1]
# 
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have 
# finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
# ==============================================================================
# Method: DFS
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: Refer to question #207-Course-Schedule
# ==============================================================================

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        visitedInsideDFS = [False] * numCourses
        visitedCourse = [False] * numCourses
        order = []
        for course in xrange(numCourses):
            if not visitedCourse[course]:
                currentPath = []
                if self.dfs(graph, course, visitedInsideDFS, visitedCourse, order, currentPath):
                    order.append(currentPath)

        return order

    def dfs(self, graph, course, visitedInsideDFS, visitedCourse, order, currentPath):
        if visitedInsideDFS[course]:
            return False

        visitedInsideDFS[course] = True
        for nextNode in graph[course]:
            if self.dfs(graph, nextNode, visitedInsideDFS, visitedCourse, order, currentPath+[course]):
                return True
        visitedInsideDFS[course] = False
        visitedCourse[course] = True

        return False

if __name__ == '__main__':
    numCourses, prerequisites = 2, [[1,0]]
    # numCourses, prerequisites = 2, [[1,0],[0,1]]
    numCourses, prerequisites = 3, [[2,0],[2,1]]
    print Solution().findOrder(numCourses, prerequisites)