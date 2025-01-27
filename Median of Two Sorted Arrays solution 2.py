class Solution(object):
    def verifyMedianSortedArrays(self, nums1, nums2):
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

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print("function call with nums1 = {} and nums2 = {}".format(nums1, nums2))

        m = len(nums1)
        n = len(nums2)
        if min(m,n) <= 1:
            arr = []
            if m >= n:
                arr = nums1[max(0,(m//2-1)):min(m,(m//2 + m%2+1))] + nums2
            else:
                arr = nums2[max(0,(n//2-1)):min(n,(n//2 + n%2+1))] + nums1
            return self._median(sorted(arr))
        
        else:
            
            if m >= n:
                a = nums2[n//2] >= nums1[m//2]
                b = nums2[n//2-1+n%2] <= nums1[m//2-1+m%2]
                if a and b:
                    return float(nums1[m//2] + nums1[m//2-1+m%2])/2
                elif a:
                    return self.findMedianSortedArrays(nums1[n//2:m],nums2[0:n//2+n%2])
                elif b:
                    return self.findMedianSortedArrays(nums1[0:m-n//2],nums2[n//2:n])
                else:
                    return float(nums2[n//2] + nums2[n//2-1+n%2])/2
            else:
                a = nums1[m//2] >= nums2[n//2]
                b = nums1[m//2-1+m%2] <= nums2[n//2-1+n%2]
                if a and b:
                    return float(nums2[n//2] + nums2[n//2-1+n%2])/2
                elif a:
                    return self.findMedianSortedArrays(nums2[m//2:n],nums1[0:m//2+m%2])
                elif b:
                    return self.findMedianSortedArrays(nums2[0:n-m//2],nums1[m//2:m])
                else:
                    return float(nums1[m//2] + nums1[m//2-1+m%2])/2
    

    def _median(self, arr):
        n = len(arr)
        if n>0:
            return float(arr[n//2 + n%2 -1] + arr[n//2])/2
        return None

#def midIndex(n):
#    return n//2-1 + n % 2,n//2

slt = Solution()


#test: 1
nums1 = [1,2,3,4,5,6]
nums2 = [7,8,9,10]
print(slt.findMedianSortedArrays(nums1,nums2), slt.verifyMedianSortedArrays(nums1,nums2))

#test: 2
nums1 = [1,2,3,7,10,14]
nums2 = [7,8,9,11]
print(slt.findMedianSortedArrays(nums1,nums2), slt.verifyMedianSortedArrays(nums1,nums2))

#test: 3
nums1 = [1,2]
nums2 = [3,4]
print(slt.findMedianSortedArrays(nums1,nums2), slt.verifyMedianSortedArrays(nums1,nums2))

#test 4:
nums1 = [1,2,3,4,5,6,7,8,9,10]
nums2 = [11,12,13]
print(slt.findMedianSortedArrays(nums1,nums2) , slt.verifyMedianSortedArrays(nums1,nums2))

#test 5:
nums2 = [1,2,3,4,5,6,7,8,9,10]
nums1 = [11,12,13]
print(slt.findMedianSortedArrays(nums1,nums2) , slt.verifyMedianSortedArrays(nums1,nums2))

#test 5:
nums1 = [1,2,3,7,8,10,17,18,19,20]
nums2 = [11,12,13]
print(slt.findMedianSortedArrays(nums1,nums2) , slt.verifyMedianSortedArrays(nums1,nums2))
