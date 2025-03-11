class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            for j in range(i+1):
                if self._isPalindrome(s[j:len(s)-i+j]):
                    return s[j:len(s)-i+j]
        

    
    def _isPalindrome(self,s):
        return s == s[::-1]


slt = Solution()
print(slt.longestPalindrome("asba"))
print(slt.longestPalindrome("asbaaabsanadjab"))
print(slt.longestPalindrome("asaloaskndpba"))
print(slt.longestPalindrome("asbwerigjnwla"))
print(slt.longestPalindrome("asbasihpwqerhnqa"))
print(slt.longestPalindrome("asbqwpeqiowpqa"))
print(slt.longestPalindrome("asbspdfiojwqpea"))
