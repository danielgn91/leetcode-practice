class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mem = dict()
        mem[nums[0]] = 0
        for i in range(1,len(nums)):
            print("i = " + str(i))
            try:
                j = mem[target - nums[i]]
                return [i, j]
            except:
                mem[nums[i]] = i
        print(mem)
        return None
            
#test 1:
nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))

#test 2:
nums = [3,2,4]
target = 6
print(Solution().twoSum(nums, target))

#test 3:
nums = [3,3]
target = 6
print(Solution().twoSum(nums, target))