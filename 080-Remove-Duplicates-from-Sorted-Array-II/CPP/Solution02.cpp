// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Jul 8, 2015
// Question: 080-Remove-Duplicates-from-Sorted-Array-II
// Link:     https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
// ==============================================================================
// Follow up for "Remove Duplicates":
// What if duplicates are allowed at most twice?
// 
// For example,
// Given sorted array nums = [1,1,1,2,2,3],
// 
// Your function should return length = 5, with the first five elements of nums 
// being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
// ==============================================================================
// Method: one pass, without extra space
// Time Complexity: O(n)
// Space Complexity: O(1)
// ==============================================================================

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = nums.size();
        if (length <= 2) return length;

        int index = 2;
        for (int i = 2; i < length; i ++) {
            if (nums[i] != nums[index-2])
                nums[index++] = nums[i];
        }
        return index;
    }
};

/* Unit Test */
#define N 3
int main(int argc, char const *argv[])
{
    Solution s;
    int tmp[N] = {1,2,3};
    vector<int> v(tmp, tmp+N);
    int len = s.removeDuplicates(v);
    for (int i = 0; i < v.size(); i ++) {
        cout << v[i] << endl;
    }
    cout << "length: " << len << endl;
    return 0;
}