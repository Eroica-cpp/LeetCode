class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1: return True
        
        if word[0].isupper():
            for c in word[1:]:
                if c.islower() != word[1].islower(): return False
        else:
            for c in word[1:]:
                if not c.islower(): return False
                
        return True
