#!/usr/bin/python
# ====================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 2, 2015
# Question: 036-Valid-Sudoku 
# Link:		https://leetcode.com/problems/valid-sudoku/
# ====================================================================
# 
# Determine if a Sudoku is valid, according to: 
# Sudoku Puzzles - The Rules: http://sudoku.com.au/TheRules.aspx
# 
# The Sudoku board could be partially filled, where empty cells are 
# filled with the character '.'.
# 
# A partially filled sudoku which is valid.
# 
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. 
# Only the filled cells need to be validated.
# ====================================================================

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        flag = True
        for i in range(9):
            line = self.isValid([board[i][j] for j in xrange(9)])
            row = self.isValid([board[j][i] for j in xrange(9)])
            block = self.isValid([board[3*(i%3)+j%3][3*(i/3)+(j/3)] for j in xrange(9)])
            flag = flag and line and row and block
            if not flag:
                return False
        return flag
    
    def isValid(self, strs):
        strs = [i for i in strs if i != '.']
        return len(strs) == len(set(strs))

if __name__ == '__main__':
    board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
    print "\n".join(board)
    print Solution().isValidSudoku(board)