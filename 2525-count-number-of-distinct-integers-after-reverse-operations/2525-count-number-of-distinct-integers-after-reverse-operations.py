class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for x in nums[:]:
             nums.append(int(str(x)[::-1]))
        return len(set(nums))