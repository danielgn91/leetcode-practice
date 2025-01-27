class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m+n) % 2 != 0:
            return sorted(nums1+nums2)[(m+n)//2]
        else:
            nums = sorted(nums1+nums2)
            mid = (m+n)//2
            return float(nums[mid] + nums[mid-1])/2


slt = Solution()

#test: 1
nums1 = [1,2,3,4,5,6]
nums2 = [7,8,9,10]
print(slt.findMedianSortedArrays(nums1,nums2))

#test: 2
nums1 = [1,2,3,7,10,14]
nums2 = [7,8,9,11]
print(slt.findMedianSortedArrays(nums1,nums2))

#test: 3
nums1 = [1,2]
nums2 = [3,4]
print(slt.findMedianSortedArrays(nums1,nums2))