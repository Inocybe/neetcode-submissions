class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:
            m = (l+r) // 2
            if nums[l] > nums[r]:
                if nums[m] > nums[r]:
                    l=m+1
                elif nums[m] < nums[r]:
                    r=m
            elif nums[l] < nums[r]:
                if nums[m] < nums[r]:
                    r=m
                elif nums[m] > nums[r]:
                    l=m+1
            else:
                return nums[m]
                
        return 0



