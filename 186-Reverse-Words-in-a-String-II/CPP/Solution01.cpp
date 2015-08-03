// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Aug 3, 2015
// Question: 186-Reverse-Words-in-a-String-II
// Link:     https://leetcode.com/problems/reverse-words-in-a-string-ii/
// ==============================================================================
// Given an input string, reverse the string word by word. A word is defined as 
// a sequence of non-space characters.

// The input string does not contain leading or trailing spaces and the words 
// are always separated by a single space.

// For example,
// Given s = "the sky is blue",
// return "blue is sky the".

// Could you do it in-place without allocating extra space?

// Related problem: Rotate Array
// ==============================================================================
// Method: use extra space
// Time Complexity: O(n)
// Space Complexity: O(n)
// Note: LeetCode OJ dont support boost.
// ==============================================================================

#include <vector>
#include <string>
#include <iostream>
#include <boost/algorithm/string.hpp>
using namespace std;
using namespace boost;

class Solution {
public:
    void reverseWords(string &s) {
        vector<string> v;
        split(v, s, is_any_of(" "));
        string s2;
        for (int i = v.size() - 1; i > 0; i --)
            s2 += v[i] + " ";
        s2 += v[0];
        s = s2;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    string s1("the sky is blue");
    s.reverseWords(s1);
    cout << s1 << endl;

    return 0;
}