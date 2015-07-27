// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Jul 27, 2015
// Question: 001-Two-Sum
// Link:     https://leetcode.com/problems/two-sum/
// ==============================================================================
// Given an array of integers, find two numbers such that they add up to a 
// specific target number.
// 
// The function twoSum should return indices of the two numbers such that 
// they add up to the target, where index1 must be less than index2. Please 
// note that your returned answers (both index1 and index2) are not zero-based.
// 
// You may assume that each input would have exactly one solution.
// 
// Input: numbers={2, 7, 11, 15}, target=9
// Output: index1=1, index2=2
// ==============================================================================
// Method: Hash Table
// Time Complexity: O(n)
// Space Complexity: O(n)
// ==============================================================================

import java.util.*;

public class Solution01 {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i ++) {
            int x = nums[i];
            if (map.containsKey(target - x)) {
                return new int[] {map.get(target-x) + 1, i + 1};
            }
            map.put(x, i);
        }
        return new int[] {-1, -1};
    }
}