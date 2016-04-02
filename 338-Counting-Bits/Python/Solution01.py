class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in xrange(num+1):
            res.append(bin(i).count("1"))
        return res
