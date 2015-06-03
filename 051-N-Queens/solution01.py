#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 3, 2015
# Question: 051-N-Queens
# Link:     https://leetcode.com/problems/n-queens/
# ==============================================================================
# The n-queens puzzle is the problem of placing n queens on an n*n chessboard 
# such that no two queens attack each other.
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens' 
# placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
# 
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
# 
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# ==============================================================================
# Method: Recursion; DFS
# Time Complexity: Exp
# Space Complexity: Exp
# Note: 
# 1. Refer to question #037-Sudoku-Solver
# 2. Note the difference between value reference and its copy in python language
# 3. Rule for N-Queens: not in same row/column/diagonal
# 4. diagonal cases are tricky
# 5. need to improve efficiency
# ==============================================================================

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        matrix = [['.' for i in xrange(n)] for j in xrange(n)] 
        solution = []
        self.dfs(solution, matrix, range(n), n)
        return solution

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
                return

if __name__ == '__main__':
    n = 4
    solutions = Solution().solveNQueens(n)
    print len(solutions)
    print solutions
    for solution in solutions:
        print "\n".join(solution)
        print