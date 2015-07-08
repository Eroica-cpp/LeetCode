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
// Method: use extra space to store appear times; map
// Time Complexity: O(n)
// Space Complexity: O(n)
// ==============================================================================

#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_map<int, int> counter;
        int size = nums.size();
        for (int i = 0; i < size; i ++) {
            if (counter.find(nums[i]) == counter.end()) counter[nums[i]] = 0;
        }

        int index = 0;
        for (int i = 0; i < size; i++) {
            if (counter[nums[i]] < 2) {
                nums[index++] = nums[i];
                counter[nums[i]] ++;
            }
        }
        return index;
    }
};

/* Unit Test */
int main(int argc, char const *argv[])
{
    Solution s;
    int tmp[6] = {1,1,1,2,2,3};
    vector<int> v(tmp, tmp+6);
    int len = s.removeDuplicates(v);
    for (int i = 0; i < v.size(); i ++) {
        cout << v[i] << endl;
    }
    cout << "length: " << len << endl;
    return 0;
}