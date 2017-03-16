class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        dic1 = {}
        for i in range(12):
            counter = bin(i).count("1")
            if dic1.has_key(counter):
                dic1[counter].append(i)
            else:
                dic1[counter] = [i]

        dic2 = {}
        for i in range(60):
            counter = bin(i).count("1")
            if dic2.has_key(counter):
                dic2[counter].append(i)
            else:
                dic2[counter] = [i]

        res = []
        for h in range(5):
            m = num - h
            if dic1.has_key(h) and dic2.has_key(m):
                for i in dic1[h]:
                    for j in dic2[m]:
                        text = str(i) + ":"
                        text += "0"+str(j) if j<10 else str(j)
                        res.append(text)
                
        return res
