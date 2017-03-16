class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for i in range(12):
            for j in range(60):
                if bin(i).count("1") + bin(j).count("1") == num:
                    tmp = str(i) + ":"
                    tmp += str(j) if j >= 10 else "0"+str(j)
                    res.append(tmp)

        return res