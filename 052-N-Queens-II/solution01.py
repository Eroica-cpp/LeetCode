#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 3, 2015
# Question: 052-N-Queens-II
# Link:     https://leetcode.com/problems/n-queens-ii/
# ==============================================================================
# Follow up for N-Queens problem.
# 
# Now, instead outputting board configurations, return the total number of 
# distinct solutions.
# ==============================================================================
# Method: Recursion; DFS
# Time Complexity: Exp
# Space Complexity: Exp
# Note: 
# 1. use code from Question #051-N-Queens directly.
# 2. this solution's efficiency is below average.
# 3. have any direct mathematical formula for the answer ?
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        matrix = [['.' for i in xrange(n)] for j in xrange(n)] 
        solution = []
        self.dfs(solution, matrix, range(n), n)
        return len(solution)

    def dfs(self, solution, matrix, rest, n):
        if len(rest) <= 0:
            solution.append(["".join(i) for i in matrix])
            return            

        for i in rest:
            if not 'Q' in matrix[i]:
                for j in xrange(n):
                    if 'Q' in [matrix[k][j] for k in xrange(n)]:
                        continue
                    elif 'Q' in [matrix[i+k][j+k] for k in xrange(min(n-i,n-j))]:
                        continue
                    elif 'Q' in [matrix[i-k][j-k] for k in xrange(min(i+1,j+1))]:
                        continue
                    elif 'Q' in [matrix[i+k][j-k] for k in xrange(min(n-i,j+1))]:
                        continue
                    elif 'Q' in [matrix[i-k][j+k] for k in xrange(min(i+1,n-j))]:
                        continue

                    new = [k[:] for k in matrix]
                    new[i][j] = 'Q'
                    self.dfs(solution, new, list(set(rest)-{i}), n)