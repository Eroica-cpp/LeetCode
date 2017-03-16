class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        
        dic1 = {}
        for i in nums1:
            dic1[i] = dic1[i]+1 if dic1.has_key(i) else 1

        dic2 = {}
        for i in nums2:
            dic2[i] = dic2[i]+1 if dic2.has_key(i) else 1

        for k in dic1.keys():
            if dic2.has_key(k):
                res += [k] * min(dic1[k], dic2[k])
                
        return res