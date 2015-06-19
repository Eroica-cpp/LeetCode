#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 19, 2015
# Question: 018-4Sum
# Link:     https://leetcode.com/problems/4sum/
# ==============================================================================
# Given an array S of n integers, are there elements a, b, c, and d in S such 
# that a + b + c + d = target? Find all unique quadruplets in the array which 
# gives the sum of target.
# 
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. 
# (ie, a <= b <= c <= d)
# 
# The solution set must not contain duplicate quadruplets.
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
# 
#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)
# ==============================================================================
# Method: Use "twoSum" method; enumerate the sum of any two numbers and store 
# them into a hash table, so four sum problem becomes a two sum problem
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        size = len(nums)
        nums.sort()
        twoSumDic = {}
        fourSumDic = {}
        counter = {}

        for i in xrange(size):
            counter[nums[i]] = counter.get(nums[i])+1 if counter.get(nums[i]) else 1

            for j in xrange(i+1,size):
                if not twoSumDic.get(nums[i]+nums[j]):
                    twoSumDic[nums[i]+nums[j]] = [[nums[i],nums[j]]]
                else:
                    twoSumDic[nums[i]+nums[j]].append([nums[i],nums[j]]) 

        keys = []
        for key,val in twoSumDic.items():
            times = 2 if len(val) >= 2 else 1
            keys += [key] * times
        pairs = self.twoSum(keys, target)
        
        for pair in pairs:
            for i in twoSumDic[pair[0]]:
                for j in twoSumDic[pair[1]]:
                    new = tuple(sorted(i+j))
                    flag = True
                    for k in new:
                        if new.count(k) > counter.get(k):
                            flag = False
                            break
                    if flag and not fourSumDic.get(new):
                        fourSumDic[new] = 1

        return fourSumDic.keys()

    def twoSum(self, nums, target):
        size = len(nums)
        nums.sort()
        i, j = 0, size-1
        res = []
        while i < j:
            if nums[i]+nums[j] == target:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif nums[i]+nums[j] > target:
                j -= 1
            elif nums[i]+nums[j] < target:
                i += 1

        return res

if __name__ == '__main__':
    nums, target = [1,0,-1,0,-2,2], 0
    nums, target = [-471,-434,-418,-395,-360,-357,-351,-342,-317,-315,-313,-273,-272,-249,-240,-216,-215,-214,-209,-198,-179,-164,-161,-141,-139,-131,-103,-97,-81,-64,-55,-29,11,40,40,45,64,87,95,101,115,121,149,185,230,230,232,251,266,274,277,287,300,325,334,335,340,383,389,426,426,427,457,471,494], 2705
    nums, target = [1,1,1,1], 4
    nums, target = [1,4,-3,0,0,0,5,0], 0
    print Solution().fourSum(nums, target)