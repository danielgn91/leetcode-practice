class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        last = 0
        charmap = {}
        for i, char in enumerate(s):
            if char not in s[last:i]:
                l = max(l,i-last+1)
            else:
                last = charmap[char]+1
            charmap[char] = i
            print("last = " + str(last))
        return l

slt = Solution()

#test 1:
s = "abcabcbb"
print(slt.lengthOfLongestSubstring(s))

#test 2:
s = "bbbbb"
print(slt.lengthOfLongestSubstring(s))

#test 3:
s = "pwwkew"
print(slt.lengthOfLongestSubstring(s))

#test 4:
s = "plaenawmdosm"
print(slt.lengthOfLongestSubstring(s))
