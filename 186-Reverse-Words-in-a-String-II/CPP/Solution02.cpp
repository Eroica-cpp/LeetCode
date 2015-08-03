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
// Method: reverse in place; first reverse the whole string, then reverse single word
// Time Complexity: O(n)
// Space Complexity: O(1)
// ==============================================================================

#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    void reverseWords(string &s) {
        for (int i = 0; i < s.length() / 2; i ++)
            swap(s[i], s[s.length()-i-1]);

        int begin = 0, end = 0;
        for (int i = 0; i < s.length() + 1; i ++) {
            if (i == s.length() || s[i] == ' ') {
                end = i;
                reverse(s, begin, end);
                begin = end + 1;
            }
        }
    }

private:
    void reverse(string &s, int begin, int end) {
        for (int i = 0; i < (end - begin) / 2; i ++)
            swap(s[begin + i], s[end - i -1]);
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
