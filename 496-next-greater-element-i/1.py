class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in findNums:
            nextEle = -1
            idx = nums.index(num)
            for i in nums[idx+1:]:
                if i > num:
                    nextEle = i
                    break
            res.append(nextEle)
        
        return res