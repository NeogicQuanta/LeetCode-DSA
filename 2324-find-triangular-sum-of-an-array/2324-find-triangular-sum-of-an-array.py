class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = []
        for i in range(len(nums)-1):
            dp.append((nums[i] + nums[i+1]) % 10)
        
        return self.triangularSum(dp)