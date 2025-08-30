class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        f, l = 0, len(nums)-1
        prev = 0
        if target > nums[l]:
            return len(nums)
        if target < nums[0]:
            return 0
        while f<=l:
            m = (f + l) // 2
            prev = m - 1
            # print(f, l , m, nums[m])
            if target == nums[m]:
                return m
            elif target < nums[m]:
                if nums[prev] < target:
                    # print(prev, nums[prev])
                    return m
                l = m - 1
            else:
                f = m + 1
            
            
        return m