// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Jul 31, 2015
// Question: 125-Valid-Palindrome
// Link:     https://leetcode.com/problems/valid-palindrome/
// ==============================================================================
// Given a string, determine if it is a palindrome, considering only 
// alphanumeric characters and ignoring cases.

// For example,
// "A man, a plan, a canal: Panama" is a palindrome.
// "race a car" is not a palindrome.

// Note:
// Have you consider that the string might be empty? This is a good question 
// to ask during an interview.

// For the purpose of this problem, we define empty string as valid palindrome.
// ==============================================================================
// Method: Two passes
// Time Complexity: O(n)
// Space Complexity: O(n)
// ==============================================================================

import java.lang.*;
import java.util.*;

public class Solution01 {
    public static boolean isPalindrome(String s) {
        ArrayList<Character> charArray = new ArrayList<Character> ();
        for (int i = 0; i < s.length(); i ++)
            if (Character.isLetterOrDigit(s.charAt(i)))
                charArray.add(s.charAt(i));

        for (int i = 0; i < charArray.size()/2; i ++)
            if (Character.toLowerCase(charArray.get(i)) != Character.toLowerCase(charArray.get(charArray.size()-i-1)))
                return false;

        return true;
    }

    public static void main(String[] args) {
        String s = new String("121");
        System.out.println(isPalindrome(s));
    }
}