#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 11, 2015
# Question: 204-Count-Primes
# Link:     https://leetcode.com/problems/count-primes/
# ==============================================================================
# Description:
# 
# Count the number of prime numbers less than a non-negative number, n.
# ==============================================================================
# Method: Sieve of Eratosthenes
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Note: Indexing with array is faster than dictionary
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0

        limit = int(n**0.5)+1
        isPrime = [False]*2 + [True]*(n-2)
        for i in xrange(2, limit):
            if isPrime[i]:
                for j in xrange(i*i, n, i):
                    isPrime[j] = False

        return sum(isPrime)

if __name__ == '__main__':
    n = 1000
    n = 499979 # 41537
    n = 999983 # 78497
    n = 1500000 # 114155
    print Solution().countPrimes(n)