class Solution:
    def findDuplicates(self,nums):
        nums.sort()
        res=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1] and nums[i] not in res:
                res.append(nums[i])
        return res