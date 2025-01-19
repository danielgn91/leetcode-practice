class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i+1,len(nums),1):
                if nums[i] + nums[j] == target:
                    return [i,j]

#test 1:
nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))

#test 2:
nums = [2,3,4]
target = 6
print(Solution().twoSum(nums, target))

#test 3:
nums = [3,3]
target = 6
print(Solution().twoSum(nums, target))