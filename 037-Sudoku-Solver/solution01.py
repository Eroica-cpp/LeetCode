#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 2, 2015
# Question: 037-Sudoku-Solver
# Link:     https://leetcode.com/problems/sudoku-solver/
# ==============================================================================
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# Empty cells are indicated by the character '.'.
# 
# You may assume that there will be only one unique solution.
# ==============================================================================
# Method: Recursion 
# Time Complexity: Exp
# Space Complexity: Exp
# Note: 
# 1. Certain combinations are not solvable!!
# 2. Try to remove code redundancy and improve performance 
# ==============================================================================

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        board[:] = self.helper(0, 0, board)

    def helper(self, i, j, board):
        if not board:
            return []

        while i < 9 and j < 9 and board[i][j] != '.':
            j += 1
            i += j/9
            j %= 9

        if j >= 9 or i >= 9:
            return []

        res = []
        solutions = self.findSolutions(i, j, board)
        while solutions:
            new = []
            for k in board:
                new.append([l for l in k])
            new[i][j] = solutions.pop()
            
            if '.' not in "".join(["".join(k) for k in new]):
                return new

            res = self.helper(i+(j+1)/9, (j+1)%9, new)

            if len(res) <= 0:
                continue
            elif '.' not in "".join(["".join(k) for k in res]):
                return res

        return res

    def findSolutions(self, i, j, board):
        line = [board[i][k] for k in xrange(9)]
        row = [board[k][j] for k in xrange(9)]
        block = []
        for k in xrange(3):
            for l in xrange(3):
                block.append(board[i-i%3+l][j-j%3+k])

        solutions = set([str(k) for k in xrange(1,10)]) - set(line+row+block)
        return solutions

if __name__ == '__main__':
    board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."] # this combination is not sovalable
    board = ["534678912", "672195348", "198342567", "859761423", "426853791", "713924856", "961537284", "287419635", "345286179"]
    board = ["534678912", "672195348", "198342567", "859761423", "426853791", "713924856", "961537284", "2874196..", "345286179"]
    board = board[:-8] + ["........."] * 8
    board = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    board = [[i for i in j] for j in board]

    for i in board:
        print i
    Solution().solveSudoku(board)
    
    print "!!!!!!!!!!!!!"    
    for i in board:
        print i
