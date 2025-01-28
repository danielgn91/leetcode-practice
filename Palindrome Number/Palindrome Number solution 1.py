class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        
        x = len(digits)
        for i in range(x//2):
            if digits[i] != digits[x-i-1]:
                return False
            
        return True