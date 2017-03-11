class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.allUpper(word) or self.allLower(word) or self.firstUpper(word)
        
    def allUpper(self, word):
        flag = True
        for c in word:
            flag = flag and c.isupper()
        return flag
        
    def allLower(self, word):
        flag = True
        for c in word:
            flag = flag and c.islower()
        return flag

    def firstUpper(self, word):
        flag = word[0].isupper()
        for c in word[1:]:
            flag = flag and c.islower()
        return flag
      
        